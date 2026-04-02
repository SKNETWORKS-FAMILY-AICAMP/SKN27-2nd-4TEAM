# XGBoost 고객 이탈 예측 모델 평가 보고서

> **모델:** XGBClassifier (XGBoost)  
> **데이터:** E-Commerce Customer Churn Dataset  
> **작성 기반:** model_pcj.ipynb

---

## 1. 프로젝트 개요

### 1.1 목적

E-Commerce 플랫폼의 고객 이탈(Churn) 여부를 예측하기 위해 XGBoost 분류 모델을 학습하고 평가한 결과를 정리한 문서입니다.  
고객 이탈을 사전에 예측함으로써 마케팅 비용 최적화 및 고객 유지 전략 수립에 활용하는 것을 목표로 합니다.

### 1.2 데이터셋

| 항목 | 내용 |
|------|------|
| 데이터 출처 | E-Commerce Customer Churn Dataset (dataset.xlsx) |
| 타겟 변수 | Churn (0: 유지, 1: 이탈) |
| Train/Test 분리 | 80% / 20% (StratifiedKFold, random_state=42) |
| 클래스 불균형 | 이탈 고객 비율 약 16~17% (불균형 데이터) |
| 주요 피처 | Tenure, OrderCount, SatisfactionScore, CashbackAmount 등 |

### 1.3 전처리 파이프라인

- **결측치 처리:** CJ 방식(그룹별 중앙값), JH 방식(통계 기반) 적용
- **이상치 제거:** Tenure, WarehouseToHome, DaySinceLastOrder, CashbackAmount 대상
- **피처 엔지니어링:** Dormancy_Shock, Recency_Tenure_Ratio, MonthlyOrderFreq 등 9개 파생 피처 생성
- **범주형 인코딩:** PreferredLoginDevice, PreferedOrderCat, MaritalStatus, Gender → One-Hot Encoding
- **데이터 누수 검증:** Train/Test index 겹침 0개 확인 완료

---

## 2. 모델 학습 단계별 결과

총 5단계에 걸쳐 모델을 점진적으로 개선하였습니다.

### 2.1 단계별 모델 비교

| 단계 | 설명 | 주요 변경사항 | Test AUC |
|------|------|--------------|----------|
| 1단계 | 기본 모델 | n_estimators=100, max_depth=5 | - |
| 2단계 | Imbalanced 보정 | scale_pos_weight 적용 (neg/pos 비율) | - |
| 3단계 | Overfitting 방지 | learning_rate=0.05, subsample=0.8, reg_alpha=0.1 | - |
| 4단계 | Cross Validation | StratifiedKFold(n_splits=5) CV AUC 측정 | 0.9643 (CV) |
| 5단계 | 하이퍼파라미터 튜닝 | GridSearchCV로 최적 파라미터 탐색 | 0.9952 |

### 2.2 클래스 불균형 처리

이탈 고객 비율이 약 16~17%로 불균형 데이터이므로, `scale_pos_weight`를 음성/양성 샘플 비율로 설정하여 이탈 고객에 더 높은 가중치를 부여하였습니다.

| 파라미터 | 계산 방식 | 적용 효과 |
|----------|----------|----------|
| scale_pos_weight | 음성(0) 샘플 수 / 양성(1) 샘플 수 | 소수 클래스(이탈) 예측 정확도 향상 |

### 2.3 하이퍼파라미터 튜닝 (GridSearchCV)

5-Fold Stratified Cross Validation을 사용하여 최적 파라미터를 탐색하였습니다.

| 파라미터 | 탐색 범위 | 선택 기준 |
|----------|----------|----------|
| n_estimators | [100, 200, 300, 400, 500] | Loss Plot 분석 기반 |
| max_depth | [3, 4, 5] | 트리 복잡도 제어 |
| learning_rate | [0.01, 0.05, 0.1] | 수렴 속도 조정 |
| subsample | [0.7, 0.8, 0.9] | 과적합 방지 |
| colsample_bytree | [0.7, 0.8, 0.9] | 피처 샘플링 |

---

## 3. 최종 모델 성능 평가

### 3.1 주요 성능 지표

| 지표 | Train | Test | 판정 |
|------|-------|------|------|
| AUC (ROC) | ~1.0000 | 0.9952 | 양호 |
| CV AUC (5-Fold) | - | 0.9643 | 양호 |
| AUC 차이 (Train-Test) | - | ~0.005 | 과적합 없음 |
| CV vs Test 차이 | - | 0.0309 | 경계 수준 |

### 3.2 분류 성능 (Classification Report)

이탈 예측에서 핵심 지표인 Recall(재현율)과 F1 Score를 중점적으로 평가하였습니다.

| 클래스 | Precision | Recall | F1 Score | 설명 |
|--------|-----------|--------|----------|------|
| 0 (유지) | - | - | - | 정상 고객 예측 |
| 1 (이탈) | - | - | - | 이탈 고객 예측 (핵심) |

> ※ 이탈 예측 비즈니스 특성상 **Recall(실제 이탈 고객 중 맞춘 비율)** 이 가장 중요한 지표입니다.

### 3.3 과적합 검증 결과

다음 3가지 방법으로 과적합 및 데이터 누수 여부를 검증하였습니다.

| 검증 항목 | 결과 | 판정 |
|----------|------|------|
| Train/Test index 겹침 | 0개 | 누수 없음 |
| Tenure 중앙값 (train 기준) | 2.1972 (log 변환값) | 정상 |
| train_monthly_freq_mean 전달 | 2.3515 (train 기준) | 정상 |
| CV AUC vs Test AUC 차이 | 0.0309 (경계 수준) | 모니터링 필요 |

---

## 4. Loss Plot 분석 (과적합 시각화)

n_estimators(트리 개수)를 1~800까지 변화시키며 Train Loss와 Test Loss 추이를 분석하였습니다.

### 4.1 구간별 분석

| 구간 | Train Loss | Test Loss | 해석 |
|------|-----------|-----------|------|
| 0 ~ 100 | 급격히 감소 | 급격히 감소 | 정상 학습 구간 |
| 100 ~ 300 | 계속 감소 | 완만하게 감소 | 격차 벌어지기 시작 (과적합 신호) |
| 300 ~ 800 | 0에 수렴 | 거의 평탄 (0.05~0.06) | 실질적 개선 없음 |

### 4.2 결론 및 권장사항

- test_loss가 다시 올라가지 않아 **극단적 과적합은 아님**
- 300 이후 test_loss가 개선되지 않으므로 **n_estimators는 200~300이 최적**
- 400~500 이상은 학습 시간만 증가하고 성능 향상은 미미

---

## 5. 고객 세그먼트 분석

### 5.1 이탈 위험 고객 분포

최종 모델의 이탈 확률(Churn_Prob)을 기반으로 고객을 5개 위험 등급으로 분류하였습니다.

| 위험 등급 | 이탈 확률 범위 | 설명 | 권장 대응 |
|----------|--------------|------|----------|
| 안전 | 0 ~ 20% | 이탈 가능성 낮음 | 정기 유지 마케팅 |
| 관심 | 20 ~ 50% | 잠재 위험군 | 혜택 제공 검토 |
| 주의 | 50 ~ 80% | 이탈 예측됨 | 쿠폰/캐시백 즉시 제공 |
| 경고 | 80 ~ 95% | 고위험군 | 전담 CS 연결 |
| 위험 | 95 ~ 100% | 이탈 거의 확실 | 긴급 리텐션 캠페인 |

### 5.2 고객 등급 분류 (CustomerGrade)

이탈 확률과 월평균 주문 빈도(MonthlyOrderFreq)를 조합하여 3개 등급으로 분류하였습니다.

| 등급 | 기준 | 설명 |
|------|------|------|
| VIP | 이탈 확률 < 10% AND 주문 빈도 >= 평균 | 핵심 우량 고객 |
| Platinum | 이탈 확률 < 20% | 안정적 저위험 고객 |
| Gold | 이탈 확률 20~50% | 관심 필요 고객 |
| Silver | 이탈 확률 50~80% | 이탈 위험 고객 |
| Risk | 이탈 확률 >= 80% | 고위험 이탈 고객 |

---

## 6. 피처 중요도 및 SHAP 분석

### 6.1 파생 피처 설명 (features.py 기반)

| 피처명 | 계산 방식 | 이탈 관련성 | 
|--------|----------|-----------| 
| Dormancy_Shock | DaySinceLastOrder / (평균 주문 주기 + 1) | 값이 클수록 이탈 위험 높음 | 
| Recency_Tenure_Ratio | DaySinceLastOrder / 가입 기간 | 신규 고객 이탈 포착 | 
| MonthlyOrderFreq | OrderCount / 가입 기간(월) | 활동성 측정 (낮을수록 위험) | 
| Silent_Killer | 불만 없음 AND 만족도 <= 2 | 조용한 이탈자 식별 | 
| Stagnant_Loyal | 가입 30개월+ AND 주문 빈도 < 평균 | 정체된 장기 고객 | 
| Satisfaction_Per_Order | SatisfactionScore / (OrderCount + 1) | 주문 효율 대비 만족도 | 

### 6.2 SHAP 분석

TreeExplainer를 활용한 SHAP 분석으로 개별 고객의 이탈 이유를 설명하였습니다.  
각 고객별 이탈 기여 피처 Top 2를 추출하여 맞춤형 리텐션 전략 수립에 활용하였습니다.

| 분석 항목 | 내용 |
|----------|------|
| 사용 모델 | shap.TreeExplainer(best_model) |
| 분석 대상 | Test 데이터 전체 |
| 주요 출력 | 이탈 예측 고객별 이탈이유 1순위, 2순위 (SHAP 값 기준) |

---

## 7. 결론 및 개선 방향

### 7.1 결론

XGBoost 기반 고객 이탈 예측 모델은 **Test AUC 0.9952, CV AUC 0.9643**으로 높은 예측 성능을 달성하였습니다.  
데이터 누수 검증 결과 index 겹침 0개, 전처리 통계값 train 기준 적용 등 모든 항목에서 정상으로 확인되었습니다.

### 7.2 한계점

- CV AUC(0.9643)와 Test AUC(0.9952) 차이가 **0.0309로 경계 수준** — 지속적인 모니터링 필요
- Loss Plot에서 Train/Test Loss 간 격차 존재 — 경미한 과적합 가능성
- 특정 random_state(42)에 의존한 결과일 수 있어 다양한 seed 검증 권장

### 7.3 개선 방향

- Early Stopping 적용으로 최적 n_estimators 자동 탐색
- SMOTE 등 오버샘플링 기법 추가 적용으로 클래스 불균형 보완 검토



### 7.4 최종 모델 파라미터

| 파라미터 | 값 |
|----------|---|
| 모델 | XGBClassifier |
| eval_metric | logloss |
| scale_pos_weight | neg/pos 비율 (자동 계산) |
| 최적 파라미터 | GridSearchCV best_params_ 참조 |
| 저장 경로 | best_model_xgboossssttttt-01.pkl |

---

