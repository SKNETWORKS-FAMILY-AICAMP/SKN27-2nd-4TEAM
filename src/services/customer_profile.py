"""
이탈(MLP 확률) + 체리피커(통계 점수)를 같은 고객 행에 붙이기.

- Churn: 학습된 MLP의 predict_proba[:, 1] (이탈=1)
- Cherry: `cherry_picker` 모듈의 분위 기반 점수(별도 라벨 없이 운영 정의)
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.services.cherry_picker import CherryPickerConfig, classify_cherry_picker


def churn_cherry_profile(
    df: pd.DataFrame,
    churn_proba: np.ndarray | pd.Series,
    *,
    reference_df: pd.DataFrame | None = None,
    cherry_config: CherryPickerConfig | None = None,
) -> pd.DataFrame:
    """
    `df`: FeatureCreate 직후 등, `cherry_picker`에 필요한 컬럼이 있는 DataFrame.
    `churn_proba`: 이탈(양성) 확률, `df`와 **같은 행 순서·길이**.
    `reference_df`: 체리 점수 분위의 기준 집단(예: train). None이면 `df` 내부 랭크.

    반환: 원본 컬럼 + cherry_score, cherry_segment, churn_proba
    """
    p = np.asarray(churn_proba, dtype=float).reshape(-1)
    if len(df) != len(p):
        raise ValueError("df와 churn_proba 행 수가 같아야 합니다.")

    out = classify_cherry_picker(df, reference_df=reference_df, config=cherry_config)
    out["churn_proba"] = p
    return out
