# MLP(다층 퍼셉트론) 모델링 평가·분석 보고서 (Churn)

**대상 노트북:** `src/modeling/MLP.ipynb`  
**데이터:** `data/dataset.xlsx` (Target: `Churn`, 이진 분류)  
**목적:** 전처리·튜닝·검증 절차를 문서화하고, **누수/과적합 리스크**를 점검하며, 운영에 필요한 **Threshold 의사결정** 기준을 제시한다.

> **원칙(중요):** 이 문서의 수치는 “말로 적은 예시”가 아니라, **노트북에서 실제 출력된 값**을 기준으로 기록한다.  
> 노트북을 변경·재실행하면 수치가 바뀔 수 있으므로, “확정 수치”에는 **출처(노트북 출력)** 를 함께 남긴다.

---

## 0. Executive Summary (한 장 요약)

- **모델**: `sklearn.neural_network.MLPClassifier` 기반 Churn 이진 분류
- **핵심 전처리**: 결측 대체 → 이상치 제어/변환 → 파생 피처 → (필요시) 인코딩/컬럼 정렬 → 스케일링
- **검증 설계(정석 권장)**: **Train / Validation / Test 3-way**
  - Validation: 튜닝/threshold 결정용
  - Test: 최종 1회 평가용(모니터링에 사용 금지)
- **최근 노트북 출력(확정, `MLP.ipynb`)**
  - **F1(threshold=0.5)**: **0.6750**
  - **ROC-AUC**: **0.9381**
  - **Test Log Loss(최종 1회 평가)**: **0.5002**

---

## 1. 데이터·분할 설계

### 1.1 기본 홀드아웃 분할(노트북 기준)

| 항목 | 값 |
|---|---|
| 방법 | `train_test_split` |
| test 비율 | 20% (`test_size=0.2`) |
| stratify | `stratify=y` |
| seed | `random_state=42` |

### 1.2 시간 기반 검증의 한계(필수 주의)
`dataset.xlsx`에 **관측 시점/스냅샷 날짜/가입일** 등 시간축이 명확한 컬럼이 없으면,  
**“과거로 학습 → 미래로 평가”** 형태의 시간 홀드아웃을 엄밀히 구성할 수 없다.  
따라서 본 문서의 홀드아웃 test 지표는 **랜덤/층화 분할에 대한 일반화 성능**을 보여줄 뿐,  
운영 시점(미래 데이터)에 대한 성능을 보장하지 않는다.

**권장**: 데이터에 기준 시점 컬럼(예: 스냅샷 날짜)을 확보한 뒤, 다음을 추가한다.
- **Time-based holdout**: 과거 구간 학습, 미래 구간 평가
- **Rolling/Backtesting**: 시점별 성능 안정성 확인

---

## 2. 전처리 파이프라인(코드 기준) 및 누수 방지 포인트

> 아래 항목은 `src/modeling/MLP.ipynb`에서 사용된 파이프라인/함수명을 기준으로 정리했다.

### 2.1 결측치 처리
- **모듈**: `src/pipeline/missing_value.py`
- **전략**
  - `CJ_MissingValue`: 그룹 중앙값 기반 대체(그룹 최소 크기 조건 포함)
  - `JH_train_stats`로 **train 통계만 계산** 후
  - `JH_MissingValue`로 train/test에 **동일 통계 적용**
- **누수 방지 포인트**
  - 결측 대체에 쓰는 통계(평균/중앙값/최빈 등)는 **반드시 train에서만 산출**

### 2.2 이상치 처리 및 변환
- **모듈**: `src/pipeline/outlier_control.py`
- **전략**: 일부 수치 컬럼에 대해 clip/log 등의 변환 적용
- **주의**
  - “train 분포로 임계값을 학습”하는 방식이라면 임계값 산출은 train에만 수행해야 함

### 2.3 파생 피처 생성
- **모듈**: `src/pipeline/features.py` (`FeatureCreate`)
- **전략**
  - train에서 계산한 기준값(예: `MonthlyOrderFreq` 평균)을 test에 전달해 동일 규칙 적용
- **누수 방지 포인트**
  - 파생 피처에 쓰는 기준값(평균/비율 분모 등)이 **test를 보지 않고** 만들어지는지 확인

### 2.4 모델 입력 컬럼 정리(필수)
실험 과정에서 train/test의 컬럼이 달라지는 경우가 있었고(`StandardScaler`에서 feature-name mismatch 발생),
다음 규칙을 강제해야 한다.

- **식별자/인덱스/의미 없는 컬럼 drop**
  - 예: `CustomerID`, `IssueIndex` 등
  - drop는 `errors=\"ignore\"`로 방어(이미 제거된 경우 KeyError 방지)
- **범주형 처리(MLP에 필수)**
  - `StandardScaler`는 문자열을 처리할 수 없으므로,
  - (권장) 원-핫 인코딩 후 스케일링, 또는 ColumnTransformer로 수치/범주 파이프라인 분리
- **컬럼 정렬**
  - `X_test = X_test.reindex(columns=X_train.columns, fill_value=0)`로 컬럼/순서 강제

### 2.5 스케일링
- **도구**: `StandardScaler`
- **원칙**
  - `fit`은 **train에만**
  - validation/test는 **transform만**

---

## 3. 모델 및 튜닝(코드 기준)

### 3.1 모델
- **모델**: `MLPClassifier` (이진 분류)
- **주의**
  - 입력 스케일에 민감 → 스케일링 필수
  - 과적합 가능 → 규제(`alpha`), 구조(hidden sizes), 학습률/epoch, early stopping 등을 점검

### 3.2 하이퍼파라미터 탐색
- **도구**: `GridSearchCV`
- **설정(요약)**: `cv=3`, `scoring='f1'`
- **기록된 Best params(노트북 기반)**: `{'alpha': 0.001, 'hidden_layer_sizes': (50, 50), 'learning_rate_init': 0.01}`

---

## 4. 평가 지표 정의 및 보고 원칙

### 4.1 Threshold 비의존(순위 품질)
- **ROC-AUC**: 확률 점수의 “순위” 품질(임계값 무관)
- (권장 추가) **PR-AUC(Average Precision)**: 불균형 데이터에서 더 민감한 순위 지표

### 4.2 Threshold 의존(운영 결정 지표)
- **Precision**: “이탈”로 예측한 것 중 실제 이탈 비율
- **Recall**: 실제 이탈 중 잡아낸 비율
- **F1**: precision/recall 균형 지표

---

## 5. 실험 결과(노트북 출력 기준)

### 5.1 Test set (확정)
- **F1(threshold=0.5)**: **0.6750**
- **ROC-AUC**: **0.9381**
- **Test Log Loss (final, evaluated once)**: **0.5002**

---

## 6. Threshold 튜닝 절차(권장 표준 프로토콜)

### 6.1 원칙
- **Validation에서만 threshold를 고른다**
- **Test는 마지막에 1회만** 성능을 확인한다

### 6.2 절차(요약)
1) validation 확률 `p_val` 계산  
2) threshold 후보(예: 0.05~0.95) 스윕  
3) 목표(예: F1 최대, Recall≥목표 등)로 최적 threshold 선택  
4) 선택된 threshold로 test 1회 평가

---

## 7. 신뢰성·누수 점검 체크리스트

- scaler/encoder를 **전체 데이터에 fit**하지 않았는가
- 파생 피처가 **미래 정보를 사용**하지 않았는가
- ID/인덱스가 라벨과 우연히 강한 상관(순서/정렬 누수)인지 점검했는가

---

## 8. 재현 방법(권장)

- `src/modeling/MLP.ipynb`를 위에서 아래로 실행
- 최종 출력(지표/파라미터/test log loss)을 캡처/저장

