"""
체리피커(Cherry Picker) 경향 구분 — 통계(분위·랭크)만 사용, 별도 ML 모델 없음.

정의(운영 가정):
  혜택(쿠폰·캐시백) 대비 주문이 적지 않게 높게 쓰는 유형을 '프로모 의존'으로 본다.
  `Promo_Sensitivity`, `CashbackPerOrder`(또는 원본에서 동일 식으로 복원)의
  기준 분포 대비 상대 위치로 0~1 점수와 구간 라벨을 부여한다.

입력:
  - `OutlierControl` 이후·`FeatureCreate` 이전: Tenure_log, DaySinceLastOrder_clip,
    CashbackAmount_clip, OrderCount, CouponUsed
  - 또는 `FeatureCreate` 이후: Promo_Sensitivity, CashbackPerOrder, MonthlyOrderFreq 등
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd

SegmentLabel = Literal["cherry_picker", "mixed", "promo_light"]


@dataclass
class CherryPickerConfig:
    """기준 분포 없이 호출할 때 쓰는 분위수 컷(0~1 점수 기준)."""

    cherry_min: float = 0.72
    mixed_max: float = 0.40


def _denom_order(s: pd.Series) -> pd.Series:
    return s + 1.0


def _ensure_promo_cashback_features(df: pd.DataFrame) -> pd.DataFrame:
    """필요 시 주문·쿠폰·캐시백으로 파생 지표를 채운다."""
    out = df.copy()
    oc = out.get("OrderCount")
    if oc is None:
        raise KeyError("OrderCount 컬럼이 필요합니다.")
    denom = _denom_order(oc.astype(float))
    if "Promo_Sensitivity" not in out.columns and "CouponUsed" in out.columns:
        out["Promo_Sensitivity"] = out["CouponUsed"].astype(float) / denom
    if "CashbackPerOrder" not in out.columns:
        if "CashbackAmount_clip" not in out.columns:
            raise KeyError("CashbackPerOrder 또는 CashbackAmount_clip 이 필요합니다.")
        out["CashbackPerOrder"] = out["CashbackAmount_clip"].astype(float) / denom
    return out


def _percentile_rank_vs_reference(
    x: pd.Series, reference: pd.Series
) -> pd.Series:
    """reference 분포에서 x의 값이 높을수록 1에 가까워지는 경험적 CDF 랭크."""
    ref = np.sort(reference.astype(float).values)
    xv = x.astype(float).values
    ranks = np.searchsorted(ref, xv, side="right") / max(len(ref), 1)
    return pd.Series(np.clip(ranks, 0.0, 1.0), index=x.index)


def cherry_picker_score(
    df: pd.DataFrame,
    reference_df: pd.DataFrame | None = None,
    *,
    promo_weight: float = 0.55,
    cashback_weight: float = 0.45,
) -> pd.Series:
    """
    0~1 스칼라 점수. 높을수록 프로모/캐시백 의존(체리피커 경향)이 큼.

    reference_df: 전체 고객 등 '기준 집단'(예: train). None이면 df 자기 자신으로 랭크.
    """
    if not 0 <= promo_weight <= 1 or not 0 <= cashback_weight <= 1:
        raise ValueError("weights must be in [0, 1]")
    wsum = promo_weight + cashback_weight
    promo_weight /= wsum
    cashback_weight /= wsum

    d = _ensure_promo_cashback_features(df)
    ref = reference_df if reference_df is not None else d
    ref = _ensure_promo_cashback_features(ref)

    r_promo = _percentile_rank_vs_reference(
        d["Promo_Sensitivity"], ref["Promo_Sensitivity"]
    )
    r_cb = _percentile_rank_vs_reference(
        d["CashbackPerOrder"], ref["CashbackPerOrder"]
    )
    score = promo_weight * r_promo + cashback_weight * r_cb
    return score.astype(float)


def cherry_picker_segment(
    score: pd.Series,
    config: CherryPickerConfig | None = None,
) -> pd.Series:
    """점수 구간 → 라벨."""
    cfg = config or CherryPickerConfig()
    labels: list[SegmentLabel] = []
    for v in score:
        if v >= cfg.cherry_min:
            labels.append("cherry_picker")
        elif v <= cfg.mixed_max:
            labels.append("promo_light")
        else:
            labels.append("mixed")
    return pd.Series(labels, index=score.index, dtype="object")


def classify_cherry_picker(
    df: pd.DataFrame,
    reference_df: pd.DataFrame | None = None,
    config: CherryPickerConfig | None = None,
) -> pd.DataFrame:
    """
    한 번에 점수·세그먼트까지 붙인 프레임 반환.

    반환 컬럼: cherry_score, cherry_segment
    """
    s = cherry_picker_score(df, reference_df)
    seg = cherry_picker_segment(s, config)
    out = df.copy()
    out["cherry_score"] = s
    out["cherry_segment"] = seg
    return out
