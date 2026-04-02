# MLP(다층 퍼셉트론) 모델링 평가·분석 보고서 (Churn)

**대상 노트북:** `src/modeling/MLP.ipynb`  
**데이터:** `data/dataset.xlsx` (Target: `Churn`, 이진 분류)  
**목적:** 현재 노트북에 구현된 전처리·학습·검증·평가 절차를 문서화하고, 분할·SMOTE·Early stopping·임계값 설정이 결과에 미치는 영향을 명확히 한다.

> **원칙:** 본 문서의 **수치**는 아래에 적은 **노트북 실행 출력(한 번의 실행 기준)** 과 일치한다. 노트북을 수정·재실행하면 수치는 달라질 수 있다.

---

## 0. Executive Summary (한 장 요약)

- **모델:** `sklearn.neural_network.MLPClassifier` (이진 분류, `partial_fit` 반복 학습)
- **전처리:** 결측(CJ/JH) → 이상치(`OutlierControl`) → 파생(`FeatureCreate`) → `StandardScaler`
- **불균형:** Train을 **내부 train/val로 나눈 뒤**, **내부 train 구간에만** `SMOTE` 적용 (검증·테스트 원본 분포 유지)
- **조기 종료:** **Validation log loss** 기준, **patience=30** (개선 없으면 중단)
- **노트북 출력(확정, 해당 실행 기준)**
  - **Early stopping:** epoch **428** 에서 종료 메시지 출력
  - **Test F1** (threshold **0.6**): **0.7146**
  - **Test ROC-AUC:** **0.9325**

---

## 1. 데이터·분할 설계

### 1.1 원본 로드

| 항목 | 내용 |
|------|------|
| 파일 | `../../data/dataset.xlsx` (노트북 기준 상대 경로) |
| 중복 | `CustomerID` 기준 `drop_duplicates` |

### 1.2 학습 전 컬럼 드롭 (라벨 분리 전 `data`에서 제거)

노트북에서 `X = data.drop("Churn")` 이전에 아래 컬럼을 제거한다 (`errors="ignore"`).

- `CustomerID`, `IssueIndex`, `Silent_Killer`, `Recency_Tenure_Ratio`, `Stagnant_Loyal`, `Dormancy_Shock`

### 1.3 홀드아웃 (Train / Test)

| 항목 | 값 |
|------|-----|
| 방법 | `train_test_split` |
| test 비율 | 20% (`test_size=0.2`) |
| stratify | `stratify=y` |
| seed | `random_state=42` |

### 1.4 내부 Train / Validation (스케일링 이후)

전체 **Train**을 `StandardScaler`로 변환한 행렬 `X_train_scaled`에 대해 다시 분할한다.

| 항목 | 값 |
|------|-----|
| 방법 | `train_test_split` |
| validation 비율 | Train의 20% (`test_size=0.2`) |
| stratify | `stratify=y_train` |
| seed | `random_state=42` |

- **SMOTE:** `X_tr_raw`, `y_tr_raw` (내부 train)에만 `fit_resample` → `X_tr`, `y_tr`
- **Validation:** `X_val_raw`, `y_val` — **SMOTE 미적용** (`X_val = X_val_raw`)

---

## 2. 전처리 파이프라인 (코드 기준)

### 2.1 결측치

- **모듈:** `src/pipeline/missing_value.py`
- **CJ:** `CJ_MissingValue` — 지정 컬럼·그룹·최소 그룹 크기에 따라 그룹 중앙값 등으로 대체, 테스트는 train에서 구한 중앙값으로 보조
- **JH:** `JH_train_stats(X_train)`로 **train 전용 통계** 산출 후 `JH_MissingValue`를 train/test에 동일 적용

### 2.2 이상치·변환

- **모듈:** `src/pipeline/outlier_control.py`
- **대상 컬럼:** `Tenure`, `WarehouseToHome`, `DaySinceLastOrder`, `CashbackAmount`
- Train/Test 각각에 동일 함수 호출 (clip/log 등은 코드 정의에 따름)

### 2.3 파생 피처

- **모듈:** `src/pipeline/features.py` — `FeatureCreate`
- **Test 쪽:** `train_monthly_freq_mean=X_train['MonthlyOrderFreq'].mean()` 전달 (train 평균 고정)
- **컬럼 정렬:** `X_test.reindex(columns=X_train.columns, fill_value=0)`

### 2.4 스케일링

- **도구:** `StandardScaler`
- **fit:** 전체 `X_train` (피처 생성·정렬 완료 후)
- **transform:** `X_test`
- 이후 내부 train/val 분할은 **이미 스케일된** `X_train_scaled` 기준

---

## 3. 모델·학습·Early stopping

### 3.1 MLP 설정 (노트북 기준)

| 하이퍼파라미터 | 값 |
|----------------|-----|
| `hidden_layer_sizes` | `(32, 16)` |
| `activation` | `relu` |
| `solver` | `adam` |
| `alpha` | `0.2` |
| `learning_rate_init` | `0.0001` |
| `max_iter` | `1` (매 epoch `partial_fit` 1회) |
| `warm_start` | `True` |
| `random_state` | `42` |

### 3.2 학습 루프

- 최대 **1000** epoch 동안 `mlp.partial_fit(X_tr, y_tr, classes=np.unique(y_tr))` 반복
- 매 epoch마다:
  - **Train loss:** `log_loss(y_tr, mlp.predict_proba(X_tr))` — SMOTE로 증강된 train 분포 기준
  - **Validation loss:** `log_loss(y_val, mlp.predict_proba(X_val))` — 원본 분포 validation

### 3.3 Early stopping

- `best_val_loss` 갱신 시 patience 카운터 리셋
- validation loss가 **30 epoch 연속** 개선되지 않으면 중단 (`patience=30`)
- 기록된 실행에서는 약 **epoch 428** 에서 조기 종료


---

## 4. 평가·임계값

### 4.1 Test 확률

- `y_prob = mlp.predict_proba(X_test_scaled)[:, 1]`

### 4.2 임계값

- 노트북에서는 **`best_t = 0.6`** 으로 고정 후 `y_pred = (y_prob >= best_t).astype(int)`
- **권장:** 운영 임계값은 validation에서 목표(Recall/F1/비용)에 맞게 스윕해 선택하고, test는 최종 1회만 사용한다. 현재 코드는 임계값을 validation에서 자동 튜닝하지 않는다.

### 4.3 보고 지표 (해당 실행 출력)

| 지표 | 값 |
|------|-----|
| F1 (`best_t=0.6`) | **0.7146** |
| ROC-AUC | **0.9325** |

### 4.4 혼동 행렬

- `confusion_matrix(y_test, y_pred, normalize="true")` 후 히트맵 시각화 (축 라벨: stay / churn)

---

## 5. 누수·신뢰성 체크리스트

- JH 통계는 **train만**으로 계산되는가
- 스케일러는 **test에 fit하지 않았는가**
- SMOTE는 **validation/test에 적용하지 않았는가**
- `FeatureCreate`의 `MonthlyOrderFreq` 평균은 **train에서만** 계산되어 test에 전달되는가
- ID·의미 없는 컬럼이 학습 행렬에 남지 않았는가

---

## 6. 재현 방법

1. 프로젝트 루트에서 `src/modeling/MLP.ipynb` 열기  
2. 셀을 위에서 아래로 실행 (현재 구조는 단일 코드 셀 중심)  
3. 출력되는 Early stopping epoch, F1, ROC-AUC, 그래프를 보고서 수치와 대조

---

## 7. 문서·코드 동기화

- 피처 정의·컬럼 대응은 `doc/columns.md`, `src/pipeline/features.py`와 함께 관리한다.  
- 노트북의 **사전 드롭 컬럼 목록**이나 **SMOTE/Early stopping** 정책이 바뀌면 본 보고서의 해당 절을 같이 수정한다.
