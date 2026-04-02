# 피처 정의 (`FeatureCreate`)

**대상:** `src/pipeline/features.py`의 `FeatureCreate` 및 선행 단계 `OutlierControl`  
**연계 문서:** `doc/columns.md` (컬럼·스키마 상세)

**목적:** 모델에 들어가기 전에 **어떤 파생 컬럼을 왜 만들었는지** 
---

## 1. 파이프라인에서의 위치

`FeatureCreate`는 아래가 끝난 뒤 호출된다.

1. **결측 처리** (`CJ_MissingValue`, `JH_MissingValue`)
2. **이상치·스케일 완화** (`OutlierControl`)  
   - 예: `Tenure` 등 → `Tenure_log` (`log1p`)  
   - `DaySinceLastOrder` → `DaySinceLastOrder_clip` (고정 상한 clip)  
   - `CashbackAmount` → `CashbackAmount_clip` (고정 구간 clip)  
   - 일부 원본 수치는 이 단계에서 제거될 수 있음

이후 `FeatureCreate`는 `Tenure_log`, `DaySinceLastOrder_clip`, `CashbackAmount_clip`, `OrderCount` 등을 입력으로 쓴다.

---

## 2. 중간 계산값 (별도 컬럼으로 남기지 않음)

| 이름 | 정의 | 왜 쓰는지 |
|------|------|-----------|
| `actual_tenure` | `expm1(Tenure_log)` 후 하한 clip | 로그 역변환으로 “가입·이용 기간”을 되살림. 0 나눗셈 방지 |
| `denom_order` | `OrderCount + 1` | 주문 횟수로 나눌 때 0 방지 |
| `avg_interval` | `actual_tenure / denom_order` (하한 clip) | **평균 주문 간격** 대용 — “평소 얼마나 자주 샀는지” |
| `DaySinceLastOrder_clip` | `OutlierControl` 결과 | 극단값을 줄인 **최근 미주문 기간** |

---

## 3. 파생 컬럼별 목적 (왜 만들었는지)

| 컬럼명 | 의도 (비즈니스·모델 관점) | 계산 요지 |
|--------|---------------------------|-----------|
| **Dormancy_Shock** | 평소 주문 리듬 대비, **지금 공백이 얼마나 비정상적으로 긴지**를 한 숫자로 본다. 값이 클수록 “갑작스러운 휴면”에 가깝다. | `DaySinceLastOrder_clip / (avg_interval + 1)` |
| **Recency_Tenure_Ratio** | 가입 기간 대비 **최근 공백이 차지하는 비중**. 짧은 이력 고객의 이탈 신호를 잡기 쉽다. | `DaySinceLastOrder_clip / actual_tenure` |
| **MonthlyOrderFreq** | 기간 대비 **얼마나 자주 주문했는지** (이름은 “월”이지만, 실제 단위는 `Tenure` 정의에 따른 기간당 빈도). | `OrderCount / actual_tenure` |
| **IssueIndex** | **불만 제기 여부**를 명시적 이진 플래그로 둔다. | `Complain` 정수화 |
| **Satisfaction_Per_Order** | 주문 건수 대비 **만족도 효율** — 건당 체감 만족. | `SatisfactionScore / denom_order` |
| **Silent_Killer** | 불만은 없는데 만족도만 낮은 **묵은 불만·잠재 이탈** 후보를 표시한다. | 불만 0 & 만족도 ≤ 2 |
| **CashbackPerOrder** | **건당 캐시백** — 혜택 체감을 주문 규모에 맞춰 본다. | `CashbackAmount_clip / denom_order` |
| **Promo_Sensitivity** | 주문 대비 **쿠폰 사용 빈도** — 프로모션 의존도·민감도 대용. | `CouponUsed / denom_order` |
| **Stagnant_Loyal** | 가입은 오래됐는데(`actual_tenure ≥ 30`) **활동 빈도가 전체 평균보다 낮은** “정체된 충성” 구간을 표시한다. 비교 기준 `μ`는 아래 4절. | `(actual_tenure ≥ 30) & (MonthlyOrderFreq < μ)` |
| **ManyAddressesFlag** | 배송지가 여러 개면 **이용 반경·헤비 유저** 여부를 단순 플래그로 본다. | `NumberOfAddress ≥ 3` |

범주형 `PreferredLoginDevice`, `PreferedOrderCat`, `MaritalStatus`, `Gender`는 `pd.get_dummies(..., drop_first=True)`로 수치화한다. 기준 범주는 컬럼별 첫 레벨이 제거된다.

---

## 4. 관련 파일

| 파일 | 역할 |
|------|------|
| `src/pipeline/features.py` | `FeatureCreate` 구현 |
| `src/pipeline/outlier_control.py` | 선행 clip·log |
| `src/pipeline/missing_value.py` | 선행 결측 처리 |
| `doc/columns.md` | 원본·중간·파생 컬럼 스키마 상세 |

---