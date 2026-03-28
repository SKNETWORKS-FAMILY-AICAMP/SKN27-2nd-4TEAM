| 분류 | 변수명 | 상세 정의 및 비즈니스 의미 (Insight) |
| :--- | :--- | :--- |
| **ID & Target** | **`CustomerID`** | 고객 고유 식별 번호. (분석 시 학습 제외 대상) |
| | **`Churn`** | **목적 변수(Target).** 고객의 이탈 여부 (1: 이탈, 0: 유지) |
| **핵심 파생 변수** | **`Dormancy_Shock`** | 개인별 주문 주기 대비 현재 휴면 기간의 비율. 갑작스러운 활동 중단 탐지. |
| (Feature Eng.) | **`Recency_Tenure_Ratio`** | 가입 기간 중 마지막 주문 이후 경과 시간의 비중. 이탈의 강력한 선행 지표. |
| | **`MonthlyOrderFreq`** | 월평균 주문 빈도. 가입 기간이 다른 고객 간 활동 밀도를 공정하게 비교. |
| | **`Promo_Sensitivity`** | 주문 대비 쿠폰 사용량. 가격 민감도가 높은 '체리피커' 성향 측정. |
| | **`Stagnant_Loyal`** | 장기 가입자 중 활동성이 급감한 '정체된 우량 고객' 식별 플래그. |
| | **`Satisfaction_Per_Order`**| 주문 건수 대비 만족도 점수. 개별 구매 경험의 질적 수준을 수치화. |
| **고객 활동 지표** | **`Tenure_log`** | 가입 기간(Tenure)에 로그 변환을 적용하여 데이터의 왜도(Skewness)를 완화함. |
| | **`CityTier`** | 고객 거주 도시의 등급 (1~3등급). 지역별 구매력 및 인프라 차이 반영. |
| | **`NumberOfDeviceRegistered`** | 서비스 이용을 위해 등록된 기기 수. 서비스 의존도 및 보안 관심도 반영. |
| | **`NumberOfAddress`** | 등록된 배송지 개수. 거주지 이동 빈도나 선물하기 이용 패턴 유추 가능. |
| | **`OrderAmountHikeFromlastYear`** | 전년 대비 주문 금액 증가율. 고객의 소비 규모 변화 추이 파악. |
| **행동 플래그** | **`ManyAddressesFlag`** | 배송지가 일정 수 이상인 고객을 분류. (주소지가 잦은 변경 등 특이 패턴) |
| | **`High_OrderCount`** | 상위권 주문 횟수를 기록한 우량 고객 여부 플래그. |
| | **`High_CouponUsed`** | 쿠폰 활용도가 매우 높은 프로모션 주도형 고객 여부 플래그. |
| **로그인 & 결제** | **`PreferredLoginDevice_*`** | 선호하는 로그인 기기 (Mobile Phone, Phone). 접근 경로의 편의성 파악. |
| (One-Hot Enc.) | **`PreferredPaymentMode_*`** | 선호 결제 수단 (COD, Credit/Debit Card, E-wallet, UPI). 결제 편의성 선호도. |
| **카테고리 & 인적** | **`PreferedOrderCat_*`** | 선호 쇼핑 카테고리 (Grocery, Laptop, Mobile 등). 고객의 주요 관심사 분류. |
| (One-Hot Enc.) | **`MaritalStatus_Married`** | 기혼 여부. 가구 구성원에 따른 구매 패턴 차이 반영. |
| | **`Gender_Male`** | 성별 (남성 여부). 성별에 따른 선호 품목 및 쇼핑 성향 차이 반영. |