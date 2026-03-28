| 분류 | 변수명 | 상세 정의 및 비즈니스 의미 (Insight) |
| :--- | :--- | :--- |
| **기본 정보** | **`CustomerID`** | 고객 고유 식별 번호. (학습 시 제외) |
| **타겟** | **`Churn`** | **목적 변수.** 이탈 여부 (1: 이탈, 0: 유지) |
| **고도화 파생** | **`Dormancy_Shock`** | `Recency / Avg_Interval`. 개인별 주기 대비 휴면기의 심각도 측정. |
| (Feature Eng.) | **`Recency_Tenure_Ratio`** | 가입 기간 대비 휴면 비중. 이탈의 가장 강력한 선행 지표. |
|  | **`MonthlyOrderFreq`** | 월평균 주문 빈도. 고객 간 활동 밀도를 동일 선상에서 비교. |
|  | **`Promo_Sensitivity`** | 쿠폰 사용 비중. 혜택 종료 시 이탈 가능성이 높은 체리피커 식별. |
|  | **`Satisfaction_Per_Order`** | 주문당 만족도. 구매 경험의 질적 수준을 수치화. |
|  | **`Stagnant_Loyal`** | 장기 고객 중 활동 급감자 식별 (1: 정체 우량고객, 0: 일반). |
| **수치형 변수** | **`Tenure_log`** | 가입 기간에 로그를 취해 데이터 왜도를 완화한 변수. |
| (Behavioral) | **`CityTier`** | 거주 도시 등급 (1~3). 지역별 구매력 차이 반영. |
|  | **`NumberOfDeviceRegistered`** | 등록 기기 수. 서비스 의존도 및 멀티 디바이스 이용 행태. |
|  | **`NumberOfAddress`** | 등록된 배송지 수. 거주지 이동 또는 선물하기 빈도 유추. |
|  | **`OrderAmountHikeFromlastYear`** | 전년 대비 주문 금액 증가율. 소비 규모의 확장/축소 추세. |
| **상태 플래그** | **`ManyAddressesFlag`** | 배송지 수가 임계치를 넘는 특이 고객 (1: 다수 주소지 보유). |
| (Flags) | **`High_OrderCount`** | 누적 주문량이 상위권인 헤비 유저 여부. |
|  | **`High_CouponUsed`** | 쿠폰 활용이 매우 높은 프로모션 지향 고객 여부. |
| **로그인 기기** | **`PreferredLoginDevice_Mobile Phone`** | 스마트폰 앱을 통한 주력 접속 고객 여부. |
| (One-Hot) | **`PreferredLoginDevice_Phone`** | 웹/일반 폰을 통한 접속 고객 여부. |
| **결제 수단** | **`PreferredPaymentMode_COD`** | 착불 결제(Cash on Delivery) 선호 고객. |
| (One-Hot) | **`PreferredPaymentMode_Cash on Delivery`** | (상동) 데이터 기록 방식에 따른 중복 범주. |
|  | **`PreferredPaymentMode_Credit Card`** | 신용카드 결제 선호 고객. |
|  | **`PreferredPaymentMode_Debit Card`** | 체크카드 결제 선호 고객. |
|  | **`PreferredPaymentMode_E wallet`** | 전자지갑(페이류) 결제 선호 고객. |
|  | **`PreferredPaymentMode_UPI`** | 인도 계좌간 즉시 송금 시스템 이용 고객. |
| **주문 카테고리** | **`PreferedOrderCat_Grocery`** | 생필품/식료품 주력 구매 고객. (반복 구매 성향) |
| (One-Hot) | **`PreferedOrderCat_Laptop & Accessory`** | 가전/노트북 주력 구매 고객. (고관여, 교체 주기 김) |
|  | **`PreferedOrderCat_Mobile`** | 모바일 기기 주력 구매 고객. |
|  | **`PreferedOrderCat_Mobile Phone`** | (상동) 카테고리 기록 방식 차이 반영. |
|  | **`PreferedOrderCat_Others`** | 기타 잡화 주력 구매 고객. |
| **개인 특성** | **`MaritalStatus_Married`** | 기혼 여부. 가구 단위 소비 패턴 반영. |
|  | **`Gender_Male`** | 성별 (남성 여부). 쇼핑 성향 및 품목 선호도 차이 반영. |