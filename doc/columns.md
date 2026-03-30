# 컬럼 정의서

`data/dataset.xlsx` → 결측·이상치 처리 → `FeatureCreate` 이후의 컬럼 정의와, 코드(`src/pipeline/features.py`, `src/pipeline/outlier_control.py`)와의 대응을 정리한다.

---

## 1. 원본 데이터 (`dataset.xlsx`)

타깃: **`Churn`** (0/1)

| 컬럼명 | 설명 |
|--------|------|
| `CustomerID` | 고객 식별자 — **모델 학습 전에 제거** (`MLP.ipynb` 등) |
| `Tenure` | 가입·이용 기간 (원본 수치) |
| `PreferredLoginDevice` | 선호 로그인 기기 |
| `CityTier` | 도시 등급 |
| `WarehouseToHome` | 물류센터–거주지 거리 |
| `PreferredPaymentMode` | 선호 결제 수단 — `FeatureCreate`에서 **드롭** |
| `Gender` | 성별 |
| `HourSpendOnApp` | 앱 사용 시간 — `FeatureCreate`에서 **드롭** |
| `NumberOfDeviceRegistered` | 등록 기기 수 |
| `PreferedOrderCat` | 선호 주문 카테고리 (데이터 스펠링 그대로) |
| `SatisfactionScore` | 만족도 점수 |
| `MaritalStatus` | 결혼 여부 |
| `NumberOfAddress` | 배송지 주소 개수 |
| `Complain` | 불만 제기 여부 — 파생 후 **드롭** |
| `OrderAmountHikeFromlastYear` | 전년 대비 주문액 증가율 |
| `CouponUsed` | 쿠폰 사용 횟수 — 파생 후 **드롭** |
| `OrderCount` | 주문 횟수 — 파생 후 **드롭** |
| `DaySinceLastOrder` | 마지막 주문 이후 경과 — `OutlierControl`에서 clip 후 `DaySinceLastOrder_clip` |
| `CashbackAmount` | 캐시백 금액 — `OutlierControl`에서 clip 후 `CashbackAmount_clip` |

선행 단계에서 `Tenure`, `WarehouseToHome`는 `log1p` 변환(`Tenure_log`, `WarehouseToHome_log` 등)되고, 원본 수치 컬럼은 `OutlierControl`에서 제거된다. `WarehouseToHome_log`는 `FeatureCreate`의 `drop_cols`에서 제거된다.

---

## 2. 중간 변수 (코드상 이름)

`FeatureCreate` 내부에서 쓰이는 값 (모두 별도 컬럼으로 남지는 않음):

| 이름 | 정의 (코드 기준) |
|------|------------------|
| `actual_tenure` | `expm1(Tenure_log)` 후 하한 `0.1`으로 clip |
| `denom_order` | `OrderCount + 1` (0 나눗셈 방지) |
| `avg_interval` | `actual_tenure / denom_order` 후 하한 `0.1`으로 clip |
| `DaySinceLastOrder_clip` | `OutlierControl`에서 상한 등 적용된 최근 미주문 기간 |

---

## 3. 파생 피처 (`FeatureCreate`에서 생성)

아래 수식은 **`features.py`와 동일**하다.  
`Recency`라는 컬럼명은 없으며, 문서·구두에서 쓰던 별칭은 **`DaySinceLastOrder_clip`** 으로 통일한다.

| 분류 | 컬럼명 | 산출 로직 (코드 일치) | 비고 |
| :--- | :--- | :--- | :--- |
| **핵심 행동** | `Dormancy_Shock` | `DaySinceLastOrder_clip / (avg_interval + 1)` | `avg_interval`은 2절 참고 |
| | `Recency_Tenure_Ratio` | `DaySinceLastOrder_clip / actual_tenure` | |
| | `MonthlyOrderFreq` | `OrderCount / actual_tenure` | “월”이 아니라 **가입 기간 단위당 주문 빈도**; 기간 단위는 `Tenure` 정의에 따름 |
| **심리/경험** | `IssueIndex` | `Complain`을 정수(0/1)로 |
| | `Satisfaction_Per_Order` | `SatisfactionScore / denom_order` (= `/(OrderCount+1)`) | |
| | `Silent_Killer` | `(IssueIndex == 0) & (SatisfactionScore <= 2)` → 0/1 | |
| **경제/효율** | `CashbackPerOrder` | `CashbackAmount_clip / denom_order` | 원본 `CashbackAmount`가 아니라 **clip 이후** |
| | `Promo_Sensitivity` | `CouponUsed / denom_order` | |
| **세그먼트** | `Stagnant_Loyal` | `(actual_tenure >= 30) & (MonthlyOrderFreq < μ)` | **μ**는 `train_monthly_freq_mean`: train에서만 구한 `MonthlyOrderFreq` 평균을 test에도 동일 적용 |
| | `ManyAddressesFlag` | `(NumberOfAddress >= 3)` → 0/1 | |

---

## 4. 범주형 원-핫 (`pd.get_dummies`, `drop_first=True`)

대상 컬럼: `PreferredLoginDevice`, `PreferedOrderCat`, `MaritalStatus`, `Gender`  
(존재하는 컬럼만 처리)

- 기준 범주는 각 컬럼의 **첫 번째 레벨**이 드롭되어, 생성되는 더미 이름은 데이터 값에 따라 달라진다.
- 예: `Gender_Male`, `PreferredLoginDevice_Phone`, `PreferedOrderCat_Grocery` 등.

---

## 5. `FeatureCreate`에서 제거하는 컬럼 (`drop_cols`)

파생에 사용한 뒤 아래는 **학습 행렬에서 삭제**된다 (존재할 때만).

`DaySinceLastOrder_clip`, `Complain`, `SatisfactionScore`, `CashbackAmount_clip`, `OrderCount`, `CouponUsed`, `WarehouseToHome_log`, `RecentActive`, `HourSpendOnApp`, `is_newbie_risk`, `RoughLTV`, `PreferredPaymentMode`

> 현재 `dataset.xlsx`에는 `RecentActive`, `is_newbie_risk`, `RoughLTV`가 없을 수 있으며, 있을 때만 드롭된다.

---

## 6. 모델 입력에 남는 컬럼 예시 (현재 데이터·시드 기준)

`FeatureCreate` 직후, `CustomerID` 제거 전 **26개** 예시:

`CashbackPerOrder`, `CityTier`, `CustomerID`, `Dormancy_Shock`, `Gender_Male`, `IssueIndex`, `ManyAddressesFlag`, `MaritalStatus_Married`, `MaritalStatus_Single`, `MonthlyOrderFreq`, `NumberOfAddress`, `NumberOfDeviceRegistered`, `OrderAmountHikeFromlastYear`, `PreferedOrderCat_*`, `PreferredLoginDevice_*`, `Promo_Sensitivity`, `Recency_Tenure_Ratio`, `Satisfaction_Per_Order`, `Silent_Killer`, `Stagnant_Loyal`, `Tenure_log`

- 범주형 더미 이름은 **데이터 카테고리 값**에 따라 달라진다.
- 학습 직전에는 **`CustomerID`를 제거**한다.

---

## 7. 기존 문서 대비 수정 요약

| 항목 | 수정 내용 |
|------|-----------|
| `Dormancy_Shock` | `Recency` 표기 → **`DaySinceLastOrder_clip`**, 분모는 **`avg_interval + 1`** (단순 `Avg_Interval` 텍스트와 구분) |
| `CashbackPerOrder` | 원본 금액이 아니라 **`CashbackAmount_clip` / (OrderCount+1)** |
| `Stagnant_Loyal` | `Tenure`가 아니라 **`actual_tenure`(Tenure_log 기반)** , 평균은 **train `MonthlyOrderFreq` 평균** |
| `MonthlyOrderFreq` | “월평균” 표현은 기간 단위와 충돌할 수 있어 **코드 수식**으로 명시 |
| 인프라·원본 | `Number...` 같은 모호한 표기 → **원본 목록·최종 잔존 컬럼**을 절·표로 분리 |
| 누락 | **`Tenure_log`**, **`CustomerID` 처리**, **`drop_cols`**, **원본 엑셀 컬럼 전체 목록** 보강 |

---

*데이터 파일이나 `FeatureCreate` 로직이 바뀌면 본 문서와 `src/pipeline/features.py`를 함께 갱신한다.*
