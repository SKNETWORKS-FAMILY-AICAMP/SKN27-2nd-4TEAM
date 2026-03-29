### 📋 Feature Engineering 최종 생성 컬럼 정의서

| 분류 | 컬럼명 | 산출 로직 (Formula) | 비즈니스적 의미 및 이탈 징후 |
| :--- | :--- | :--- | :--- |
| **핵심 행동** | `Dormancy_Shock` | `Recency / (Avg_Interval + 1)` | 평소 주기 대비 공백기가 얼마나 비정상적으로 긴지 (이탈의 핵심 지표) |
| | `Recency_Tenure_Ratio` | `Recency / Actual_Tenure` | 가입 기간 대비 공백기 비중 (신규 고객의 이탈 민감도 측정) |
| | `MonthlyOrderFreq` | `OrderCount / Actual_Tenure` | 월평균 주문 빈도 (고객의 서비스 로열티 및 활동성) |
| **심리/경험** | `IssueIndex` | `Complain` (0 or 1) | 직접적인 불만 제기 여부 (명시적 이탈 신호) |
| | `Satisfaction_Per_Order` | `SatisfactionScore / (OrderCount + 1)` | 주문 횟수 대비 만족도 효율 (기대치 충족 여부) |
| | `Silent_Killer` | `(Issue==0) & (Satisfaction <= 2)` | **침묵의 이탈자.** 불만은 없으나 만족도가 낮아 소리 없이 떠날 그룹 |
| **경제/효율** | `CashbackPerOrder` | `CashbackAmount / (OrderCount + 1)` | 건당 평균 혜택 체감도 (혜택 민감 고객 식별) |
| | `Promo_Sensitivity` | `CouponUsed / (OrderCount + 1)` | 쿠폰 의존도 (프로모션 중단 시 이탈 가능성 확인) |
| **세그먼트** | `Stagnant_Loyal` | `(Tenure >= 30) & (Freq < Mean)` | **정체된 충성 고객.** 활동이 뜸해진 장기 이용자 포착 |
| | `ManyAddressesFlag` | `NumberOfAddress >= 3` | 다중 배송지 이용 여부 (서비스 활용도가 높은 헤비 유저) |
| **인프라/환경** | `CityTier` | 원본 유지 | 거주 지역의 도시 등급 (배송 인프라 영향력) |
| | `Number...` | 원본 유지 (Device, Address 등) | 고객의 서비스 접점 및 생활 밀착도 |
| **범주형** | `Preferred..._...` | One-Hot Encoding 결과 | 선호 기기, 상품 카테고리, 결혼 여부, 성별 등 고객 특성 |