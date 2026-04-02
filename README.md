# 💠 Re:tain — 고객 이탈 예측 & 유지 전략 플랫폼

> **SKN27 2차 프로젝트 | 4팀**  
> 데이터 기반 선제적 고객 유지로 이커머스의 미래를 만듭니다

---

## 👥 팀원 소개

| <img src="https://cdn.discordapp.com/attachments/1485869282872135693/1489109495668936704/image.png?ex=69cf38ca&is=69cde74a&hm=d8639df7bb28212e0b040ede21975cd2aa3cbab0ab64e2cff06e112a135ee827&" width="170"> | <img src="https://i.namu.wiki/i/ZEaPrUIMoMnfKnwSCImoLRrPqABv9V0a--LoFg2kHx-36iNY8Qmfedhl9eWYdrJrzkpX9qwpofPPBxh9VGd-rmYn7iPG_HAqB9wbB9nfQWpE2Uf1pa1NsJtCnbtpWv1-VwiWT42-zn0nAypa8abwYw.webp" width="200"> | <img src="https://i.namu.wiki/i/KusrjcH3key2LNRucTDr2lGy4Bv4q9GgGTjE8IPl_j50pPg5GCtBbz1GqIqu3PANKHmt1jOIaUlpfX8qT17lBBQHxTH7BSA9N5eJJnKGOcEEUz_prtQMp0-rN0XQXCC0Se439_un-siLoZFlrqgZDA.webp" width="200"> | <img src="https://cdn.discordapp.com/attachments/1485869282872135693/1489106146231976057/latest.png?ex=69cf35ab&is=69cde42b&hm=a050ca905dbea3751a61c7e8d33e99c739b8440aef23312064e6a751cfaffe27&" width="200">  |  <img src="https://img.extmovie.com/files/attach/images/135/068/454/012/4c323399f3a48657615568ea7aac5f48.jpg" width="200"> |
|--------|--------|--------|--------|--------|
| 김민경 (팀장) | 박준희 | 박창제 | 한재웅 | 임예은 |
| Feature Engineering · MLP 모델링 · DB 연결 · 최종 점검 | 데이터 전처리 (결측치) · Random Forest 모델링 | 데이터 전처리 (결측치) · XGBoost 모델링 · 이탈 예측 UI 연결 | 데이터 전처리 (이상치) · LightGBM 모델링 | 한국 소비 트렌드 데이터 수집 · Streamlit 개발 |

---
## 📅 WBS (작업 일정)

| 단계 | 기간 | 주요 작업 |
|------|------|----------|
| 분석 및 설계 | 3/26 ~ 3/27 | 환경 세팅 · 데이터 이해 · 기획서 작성 |
| 전처리 & 모델링 | 3/27 ~ 3/31 | 결측치/이상치 처리 · Feature Engineering · 4개 모델 학습 및 비교 |
| 서비스 개발 | 3/30 ~ 4/1 | Streamlit 3페이지 구현 · DB 연결 · UI 통합 |
| 발표 준비 | 4/2 | PPT 작성 · 최종 시연 준비 |

---
## 🛠️ 기술 스택

### ML / Data
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat)
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=flat)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-FF4B4B?style=flat)

### Backend / Infra
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat)

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

---

## 📁 프로젝트 구조

```
SKN27-2nd-4TEAM/
├── frontend/
│   ├── app.py                      # 메인 Streamlit 앱
│   ├── pages/
│   │   ├── 01_Churn_Dashboard.py   # 이탈 예측 대시보드
│   │   ├── 02_Behavior_Analysis.py # 행동 분석
│   │   └── 03_Consumer_Trends.py   # 소비 트렌드
│   └── components/
├── backend/
│   ├── connection.py               # DB 연결
│   ├── queries.py                  # SQL 쿼리
│   └── schema.sql                  # DB 스키마
├── src/
│   ├── modeling/                   # 모델 학습 코드
│   ├── pipeline/                   # 데이터 파이프라인
│   └── service/                    # 서비스 로직
├── models/                         # 학습된 모델 파일
│   ├── best_model_xgboost.pkl
│   ├── lgbm model.pkl
│   └── MLP_model.joblib
├── data/                           # 데이터셋
├── doc/                            # 문서 및 분석 리포트
├── FYR/                            # 전처리 참고 코드
├── docker-compose.yml
└── requirements.txt
```
----

## 📌 프로젝트 개요

최근 이커머스 시장은 쿠팡, 컬리 등 플랫폼 간 경쟁 심화로 **가격·할인·배송속도** 중심의 경쟁 구조로 변화하고 있습니다.  
소비자는 가격과 혜택에 따라 플랫폼을 유동적으로 이동하며, **고객 이탈(Churn)** 은 기업 매출에 직접적인 영향을 미치는 핵심 요소가 되었습니다.

**Re:tain**은 이커머스 고객 데이터를 기반으로:

- 고객 행동 패턴을 분석하여 **이탈 가능성을 사전에 예측**하고
- 한국 소비 트렌드와 결합하여 **이탈 원인을 해석**하며
- **실행 가능한 유지 전략**까지 제안하는

데이터 기반 의사결정 지원 시스템입니다.

> 💡 핵심 철학: **"고객이 떠난 이후 대응"이 아니라 "떠나기 전에 미리 대응"**

---

## 🚨 문제 정의

| 문제 | 설명 |
|------|------|
| 🔍 사전 식별 불가 | 고객 이탈을 미리 파악하기 어려움 |
| 📦 데이터 활용 부재 | 데이터는 축적되어 있으나 실질적 의사결정으로 연결되지 않음 |
| 📉 충성도 하락 | 가격·혜택 중심 경쟁으로 고객 Lock-in 약화 |
| 💸 사후적 대응 | 이탈 이후 대응 → LTV 감소 & 마케팅 비용 증가 |

---

## 🏗️ 서비스 아키텍처

```
┌────────────────────────────────────────────────────────--─┐
│                     Re:tain Platform                      │
├───────────── ─┬──────────────┬──────────────┬──────────--─┤
│  Predictive   │   Insight    │    Trend     │   Action    │
│    Layer      │    Layer     │    Layer     │   Layer     │
│               │              │              │             │
│이탈 확률 예측 │ RFM 세그먼트 │  소비 트렌드 │  맞춤 전략  │
│ 위험군 분류   │행동 패턴 분석│  경제 맥락   │ 마케팅 제안 │
│               │              │    해석      │             │
└─────────────-─┴──────────────┴──────────────┴────────────-┘
```

---

## 📊 데이터

<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN27-2nd-4TEAM/blob/dev/doc/ERD.png?raw=true" width=1000>

### 1. 고객 이탈 데이터 (E-commerce Customer Churn Dataset)

| 항목 | 수치 |
|------|------|
| 전체 데이터 건수 | **5,630건** |
| 원본 피처 수 | **20개** |
| 이탈 고객 비율 (Churn=1) | **16.9%** |
| Train / Test 분할 | **80 / 20** |

| 카테고리 | 주요 피처 |
|---------|----------|
| 구매 행동 | `OrderCount`, `DaySinceLastOrder` |
| 혜택 | `CouponUsed`, `CashbackAmount` |
| 고객 경험 | `SatisfactionScore`, `Complain` |
| 기타 | `Tenure`, `NumberOfDeviceRegistered`, `WarehouseToHome` |

- Churn = 1 → 이탈 고객 / Churn = 0 → 유지 고객

### 2. 한국 소비 트렌드 데이터 (공공데이터)

- 통계청 소비 지출 데이터
- 온라인 쇼핑 거래액 (통계청)
- 소비자 심리지수 (소비자동향조사)

---

## 🧹 데이터 전처리

### 결측치 처리 — 그룹별 중앙값 대체

| 피처 | 결측률 | 처리 방법 |
|------|--------|-----------|
| `Tenure` | 4.7% | NumberOfAddress 그룹 중앙값 |
| `DaySinceLastOrder` | 5.5% | 카테고리×로그인기기 중앙값 |
| `OrderCount` | 4.7% | 카테고리×결제수단 중앙값 |
| `OrderAmountHike` | 4.6% | 카테고리 그룹 중앙값 |
| `HourSpendOnApp` | 4.4% | 전체 중앙값 |
| `CouponUsed` | 4.6% | 전체 중앙값 |

### 이상치 처리 — 분포 기반 차별 적용

| 피처 | 처리 방식 | 변환 피처명 |
|------|-----------|-------------|
| `Tenure` | 로그 변환 (`log1p`) | `Tenure_log` |
| `WarehouseToHome` | 로그 변환 (`log1p`) | `WH_log` |
| `DaySinceLastOrder` | IQR 클리핑 | `Days_clip` |
| `CashbackAmount` | IQR 클리핑 | `Cashback_clip` |

> 💡 우편향 분포 → 로그 정규화 / 극단값 → IQR 억제

---

## ⚙️ 피처 엔지니어링

EDA 기반 이탈 예측력 강화를 목적으로 총 **10개의 파생 변수**를 설계했습니다.

### 행동 패턴 (4개)

| 피처명 | 설명 |
|--------|------|
| `Dormancy Shock` | 평소 대비 주문 공백의 충격 지수 |
| `Recency Tenure Ratio` | 가입기간 대비 최근 공백 비중 |
| `MonthlyOrderFreq` | 월평균 주문 빈도 |
| `Stagnant Loyal` | 정체된 장기 고객 (가입은 오래됐지만 활동은 평균 이하) |

### 만족도 & 경험 (3개)

| 피처명 | 설명 |
|--------|------|
| `Satisfaction_Per_Order` | 주문당 만족도 효율 |
| `Silent Killer` | 조용한 이탈자 (불만은 낮지만 만족도 낮음) |
| `IssueIndex` | 불만 제기 여부 (명시적인 부정적 경험) |

### 가치 & 반응성 (3개)

| 피처명 | 설명 |
|--------|------|
| `CashbackPerOrder` | 주문당 캐시백 체감도 |
| `Promo_Sensitivity` | 프로모션 민감도 |
| `ManyAddressesFlag` | 배송지가 많음 (헤비 유저 여부) |

> 카테고리 피처에 원-핫 인코딩 적용 → 불필요 컬럼 제거 → 최종 **24개 피처**로 모델 학습

---

## 🤖 모델링 및 성능 비교

| 모델 | 특장점 |  하이퍼파라미터 튜닝 | AUC |
|------|------|-----------|-----|
| 🌲 Random Forest | 비선형 학습, 안정적 | Manual Search CV | 0.900 |
| 🧠 다층 퍼셉트론(MLP) | 최고 정확도, 정규화 | Standard Scaler + Grid Search CV | 0.969 |
| 🚀 LightGBM | 빠른 학습, 메모리 효율 | Bayesian Search CV (Optuna) | 0.976 |
| ⭐ XGBoost | 배포 용이, 실시간 | Grid Search CV | 0.995 |

---

### 하이퍼파라미터


<details>

| 모델명 | 주요 하이퍼파라미터 (Hyperparameters) |
| :--- | :--- |
| **Random Forest** | `n_estimators=100`, `max_depth=12`, `class_weight='balanced'`, `random_state=42` |
| **XGBoost** | `colsample_bytree=0.9`, `learning_rate=0.1`, `max_depth=5`, `n_estimators=300`, `subsample=0.9` |
| **LightGBM** | `max_depth=5`, `min_samples_split=4`, `criterion='entropy'`, `max_leaf_nodes=9`, `n_estimators=460`, `learning_rate=0.0811` |
| **MLP** | `alpha=0.0001`, `hidden_layer_sizes=(50, 50)`, `learning_rate_init=0.01` |

</details>

---

### 혼동 행렬(Confusion matrix) 비교
<table>
  <tr>
    <td align="center" style="padding: 15px;">
      <img src="doc/images/output4.png" width="300" height="300"><br>
      <b>Random Forest</b>
    </td>
    <td align="center" style="padding: 15px;">
      <img src="doc/images/MLP_output2.png" width="300" height="300"><br>
      <b>MLP</b>
    </td>
  </tr>
  <tr>
    <td align="center" style="padding: 15px;">
      <img src="doc/images/output.png" width="300" height="300"><br>
      <b>Light GBM</b>
    </td>
    <td align="center" style="padding: 15px;">
      <img src="doc/images/output3.png" width="300" height="300"><br>
      <b>XGBoost</b>
    </td>
  </tr>
</table>

### AUC 성능 시각화

```
XGBoost     ████████████████████████████████████████ 0.995 ⭐ 최종 선택
LightGBM    █████████████████████████████████████░░░ 0.976
MLP         ████████████████████████████████████░░░░ 0.969
Ran. Forest ██████████████████████████████████░░░░░░ 0.900
```

> ✅ **최종 선택 모델: XGBoost** — AUC 0.995, Grid Search CV 최적화<br>

- 행동 패턴 기반 파생 변수(`Dormancy Shock`, `Recency Tenure Ratio`)가 예측력에 크게 기여
- 만족도 및 불만 관련 피처(`Complain`, `SatisfactionScore`)가 주요 이탈 신호로 작용

---

## 🖥️ Streamlit 서비스 구성

| 페이지 | 기능 |
|--------|------|
| 📊 Churn Dashboard | 고객별 이탈 확률 예측 · 위험군 분류(High/Medium/Low) |
| 🔍 Behavior Analysis | RFM 세그먼트 · 구매 패턴 · 쿠폰/만족도 영향 분석 |
| 📈 Consumer Trends | 한국 소비 트렌드 시각화 · 경제적 맥락 기반 이탈 해석 |

---
📊 Churn Dashboard
<img src="https://cdn.discordapp.com/attachments/1486264541925867580/1489167469888278528/screencapture-localhost-8501-Churn-Dashboard-2026-04-02-14_31_54_1_page-0001.jpg?ex=69cf6ec8&is=69ce1d48&hm=1d3769f96bd758aaf6f8249fcdcc7eb87f3d4b0b34f8d47476f3a0ff525a54a6&" width=1000>
🔍 Behavior Analysis
<img src="https://cdn.discordapp.com/attachments/1486264541925867580/1489166963501432942/screencapture-localhost-8501-Behavior-Analysis-2026-04-02-14_32_59_page-0001.jpg?ex=69cf6e4f&is=69ce1ccf&hm=5fca3e9f9cf7ed1ad229abddca2513ec9365a582b4873ee41982be724193b46c&" width=1000>
📈 Consumer Trends 
<img src="https://cdn.discordapp.com/attachments/1486264541925867580/1489169337934680174/screencapture-localhost-8501-Consumer-Trends-2026-04-02-14_33_44_page-0001.jpg?ex=69cf7085&is=69ce1f05&hm=f7d1a2321a3b7037aed55eefa9051a24fdc822790d709cbe691d8a83f6308d35&" width=1000>
---

## 🚀 실행 방법

### 1. 환경 설치

```bash
git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN27-2nd-4TEAM.git
cd SKN27-2nd-4TEAM
pip install -r requirements.txt
```

### 2. Docker로 DB 실행 (PostgreSQL)

```bash
docker-compose up -d
```

### 3. Streamlit 앱 실행

```bash
streamlit run frontend/app.py
```

---

## 📈 기대 효과

| 지표 | 기대 효과 |
|------|----------|
| 🎯 고객 이탈률 | 사전 예측으로 이탈률 감소 |
| 💰 고객 생애 가치 (LTV) | 유지 전략으로 LTV 증가 |
| 📣 마케팅 효율 | 타겟 마케팅으로 비용 최적화 |
| 🏆 플랫폼 경쟁력 | 데이터 기반 의사결정으로 경쟁력 강화 |

---
## 💡 결론

1. **이탈 예측 정확도 극대화** — XGBoost AUC 0.995로 실용적 수준의 예측 달성
2. **파생 변수의 중요성** — 행동 패턴·만족도·가치 기반 10개 피처가 성능 향상에 핵심 기여
3. **Re:tain 플랫폼** — Streamlit 기반 실시간 이탈 예측 대시보드로 현업 활용 가능

---
## ⭐ 한줄회고
- 김민경 : 서로의 작업 흐름을 맞춰가는 과정에서 예상치 못한 상황으로 일정이 지연되며 어려움을 겪었습니다. 이를 정리하고 다시 맞춰가는 과정에서 전체 흐름을 고려해 일정에 여유를 두는 것이 필요하다는 점을 깨달았고, 동시에 팀원들과 진행 상황을 투명하게 공유하며 우선순위를 재조정하는 과정의 중요성도 배울 수 있었습니다
- 박준희 : 프로젝트를 수행하면서 설계 및 구현의 과정과 더불어 기획의 의도와 목적을 정의하고 결과를 분석하는 것의 중요성을 느낄 수 있었습니다. 특히 데이터 분석의 과정과 어떻게 해야 이 결과를 더 잘 활용할 수 있을지에 대한 고민이 필요하다는 것을 느꼈습니다. 팀원들의 도움으로 하나의 모델을 돌려보면서 공부할 수 있었습니다.
- 박창제 : 이번 프로젝트를 수행하며 수업 시간에는 이해가 안 됐던 코드들을 이해할 수 있었다. 수업 후 꾸준히 복습을 했더라면 이번 2차 프로젝트를 좀 더 수월하게 진행 할 수 있었다고 생각한다.  머신 러닝에 대해 모든 내용을 공부하긴 어렵다고 느끼고 영어 사전을 보듯 필요한 부분을 빠르게 공부하며 xgboost 모델을 학습시켜 좋은 성과를 낼 수 있었다. 수업 시간에 했던 kaggle 경진 대회가 많은 도움이 되었고 팀원들 간에 협업이 익숙하지 않았지만 이번 프로젝트를 통해서 서로 의지하고 원활한 의사소통을 하여 좋은 결과를 낼 수 있었다고 생각한다.
- 한재웅 : 2차 프로젝트에서는 이전과는 달리 비교적 유의미한 역할을 맡을수 있었고 머신 러닝 모델링의 과정의 즐거움을 느낄수 있었습니다.
그러나 더 나은 역할을 하기 위해서는 이번 경험을 바탕으로 개발에 대한 공부를 본격적으로 할수 있도록 하여 다음 프로젝트때는 실질적인 개발을 담당할수 있도록 하고 싶습니다.
또한 개발 뿐만 아니라 기획에서도 유의미한 기여를 할수 있도록 다양한 도메인 지식을 쌓는데 노력할것입니다.
- 임예은 : 우리 데이터셋이 고객별 수치라, 시계열 관련한 데이터가 없었다. 그래서 추이를 구할 수 없어서 아쉬웠다. 다음에 데이터셋을 구할 때는 다른 데이터셋을 쓰고 싶다. 그리고 관련 도메인 지식을 더 쌓아서 유용한 서비스를 만들고 싶다.

---

<div align="center">

**SKN27 2차 프로젝트 | 4팀 Re:tain**  
*"데이터로 고객의 마음을 붙잡다"*

</div>


