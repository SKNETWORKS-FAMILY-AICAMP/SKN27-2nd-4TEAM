---
marp: true
theme: default
paginate: true
html: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

  :root {
    --navy:   #0D1B4B;
    --blue:   #1A73E8;
    --blue-lt:#4A9EF5;
    --blue-bg:#E8F0FE;
    --white:  #FFFFFF;
    --off:    #F4F7FD;
    --gray:   #64748B;
    --gray-lt:#E2EAF4;
    --green:  #16A34A;
    --amber:  #D97706;
    --mono:   'JetBrains Mono', monospace;
  }

  * { font-family: 'Noto Sans KR', sans-serif; box-sizing: border-box; }

  section {
    background: var(--off);
    color: var(--navy);
    padding: 0;
    font-size: 16px;
    width: 1280px;
    height: 720px;
    overflow: hidden;
  }

  section::after { color: var(--gray); font-size: 12px; }

  /* ════════════════════════════
     SLIDE HEADER STRIP
  ════════════════════════════ */
  .hdr {
    background: var(--navy);
    color: var(--white);
    font-size: 20px;
    font-weight: 700;
    padding: 0 52px;
    height: 62px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .hdr .num {
    color: var(--blue-lt);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
  }

  /* ════════════════════════════
     TITLE SLIDE
  ════════════════════════════ */
  section.title {
    background: var(--navy);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 72px 84px;
    position: relative;
    overflow: hidden;
  }
  section.title::before {
    content: '';
    position: absolute;
    top: -140px; right: -140px;
    width: 560px; height: 560px;
    border-radius: 50%;
    background: rgba(26,115,232,0.13);
    pointer-events: none;
  }
  section.title::after {
    content: '';
    position: absolute;
    bottom: -90px; left: -90px;
    width: 340px; height: 340px;
    border-radius: 50%;
    background: rgba(26,115,232,0.09);
    pointer-events: none;
  }
  .tag {
    font-size: 11px;
    font-weight: 700;
    color: var(--blue-lt);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 18px;
  }
  .accent-bar {
    width: 56px; height: 5px;
    background: var(--blue);
    border-radius: 3px;
    margin-bottom: 28px;
  }
  section.title h1 {
    font-size: 58px;
    font-weight: 900;
    color: var(--white);
    line-height: 1.15;
    margin: 0 0 20px 0;
    border: none;
  }
  section.title h1 span { color: var(--blue-lt); }
  section.title p {
    font-size: 18px;
    color: #AABCDD;
    margin: 0 0 44px 0;
    font-weight: 300;
  }
  .title-bar {
    display: flex;
    align-items: center;
    gap: 0;
    font-size: 13px;
    color: #7BA7D8;
    background: rgba(255,255,255,0.06);
    padding: 14px 24px;
    border-radius: 8px;
    width: fit-content;
  }
  .title-bar span { margin: 0 12px; opacity: .4; }

  /* ════════════════════════════
     COMMON HEADINGS (기존 h1/h2)
  ════════════════════════════ */
  h1, h2 {
    font-weight: 900;
    color: var(--navy);
    border: none;
    margin-top: 0;
  }
  h1 { font-size: 34px; margin: 0 0 4px; padding: 18px 52px 0; }
  h2 { font-size: 24px; margin-bottom: 6px; }

  .subtitle {
    font-size: 13px;
    color: var(--gray);
    padding: 4px 52px 0;
    margin-bottom: 0;
  }

  /* ════════════════════════════
     AGENDA
  ════════════════════════════ */
  .agenda-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 22px 52px 28px;
  }
  .agenda-card {
    background: var(--white);
    border-radius: 10px;
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 18px 22px;
    border-left: 4px solid var(--blue);
    box-shadow: 0 2px 10px rgba(0,0,0,.06);
  }
  .agenda-num {
    font-size: 28px;
    font-weight: 900;
    color: var(--blue);
    font-family: var(--mono);
    line-height: 1;
    min-width: 38px;
  }
  .agenda-text h3 { font-size: 15px; font-weight: 700; color: var(--navy); margin: 0 0 3px; padding: 0; }
  .agenda-text p  { font-size: 12px; color: var(--gray); margin: 0; }

  /* ════════════════════════════
     STAT CARDS
  ════════════════════════════ */
  .stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    padding: 20px 52px 0;
  }
  .stat-card {
    background: var(--blue);
    border-radius: 12px;
    padding: 18px 16px 14px;
    text-align: center;
    color: var(--white);
    box-shadow: 0 4px 16px rgba(26,115,232,.28);
  }
  .stat-val { font-size: 30px; font-weight: 900; line-height: 1; font-family: var(--mono); }
  .stat-lbl { font-size: 11px; opacity: .85; margin-top: 6px; }

  /* ════════════════════════════
     TWO-COL
  ════════════════════════════ */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    padding: 18px 52px 22px;
  }

  /* ════════════════════════════
     CONTENT CARD
  ════════════════════════════ */
  .card {
    background: var(--white);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,.07);
  }
  .card-head {
    background: var(--navy);
    color: var(--white);
    font-size: 13px;
    font-weight: 700;
    padding: 10px 18px;
  }
  .card-head.blue  { background: var(--blue); }
  .card-head.green { background: #166534; }
  .card-body { padding: 14px 18px; }

  /* ════════════════════════════
     TABLE — 전체 통일
  ════════════════════════════ */
  table {
    width: 100%;
    table-layout: auto;
    border-collapse: collapse;
    font-size: 13px;
    margin-top: 12px;
  }
  thead tr { background: var(--navy); color: var(--white); }
  thead th {
    padding: 10px 14px;
    text-align: left;
    font-size: 12.5px;
    font-weight: 700;
  }
  tbody tr { border-bottom: 1px solid var(--gray-lt); }
  tbody tr:nth-child(even) { background: #F8FAFF; }
  tbody td {
    padding: 9px 14px;
    vertical-align: middle;
    color: #2c2c2c;
    font-size: 12.5px;
    line-height: 1.5;
    word-break: break-word;
  }
  tbody td:first-child { font-weight: 600; color: var(--navy); }

  code {
    font-family: var(--mono);
    font-size: 11.5px;
    background: var(--gray-lt);
    padding: 1px 5px;
    border-radius: 3px;
    color: #333;
  }

  /* ════════════════════════════
     FEATURE ENGINEERING (3-col)
     — 기존 three-col 재활용,
       디자인만 통일
  ════════════════════════════ */
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 18px;
    padding: 14px 52px 0;
  }
  .feat-group {
    background: var(--white);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,.06);
  }
  .feat-group h3 {
    font-size: 13px;
    font-weight: 700;
    color: var(--white);
    background: var(--blue);
    margin: 0;
    padding: 10px 16px;
    border-bottom: none;
  }
  .feat-group.muted h3 { background: var(--navy); }
  .feat-group.dark  h3 { background: #2D6A4F; }
  .feat-group ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .feat-group ul li {
    font-size: 12px;
    color: #333;
    padding: 8px 16px;
    border-bottom: 1px solid var(--gray-lt);
    border-left: none;
    line-height: 1.5;
  }
  .feat-group ul li:last-child { border-bottom: none; }
  .feat-group ul li strong { color: var(--navy); }

  .final-process {
    margin: 14px 52px 0;
    background: var(--blue-bg);
    border-left: 4px solid var(--blue);
    padding: 11px 20px;
    border-radius: 0 8px 8px 0;
    font-size: 13px;
    color: var(--navy);
    font-weight: 500;
  }
  .final-process strong { color: var(--blue); font-weight: 700; }

  /* ════════════════════════════
     MODELING TABLE SLIDE
     (h1 + 일반 table)
  ════════════════════════════ */
  section:has(table) table { margin-top: 10px; }

  /* ════════════════════════════
     CONFUSION MATRIX GRID
  ════════════════════════════ */
  .grid-wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    padding: 16px 52px 0;
  }
  .model-box {
    background: var(--white);
    border: 1px solid var(--gray-lt);
    border-radius: 10px;
    padding: 14px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(0,0,0,.05);
  }
  .model-box img {
    width: 100%;
    max-height: 210px;
    object-fit: contain;
  }
  .model-box p {
    margin: 8px 0 0;
    font-size: 14px;
    font-weight: 700;
    color: var(--blue);
  }

  /* ════════════════════════════
     AUC BARS
  ════════════════════════════ */
  .auc-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 14px 52px 0;
  }
  .auc-row { display: flex; align-items: center; gap: 16px; }
  .auc-label {
    width: 200px;
    font-size: 14px;
    font-weight: 600;
    color: var(--navy);
    flex-shrink: 0;
  }
  .auc-bar-wrap {
    flex: 1;
    background: var(--gray-lt);
    border-radius: 6px;
    height: 38px;
    overflow: hidden;
  }
  .auc-bar { height: 100%; border-radius: 6px; }
  .auc-bar.rf   { width: 90%;   background: #90CAF9; }
  .auc-bar.lgbm { width: 97%;   background: #42A5F5; }
  .auc-bar.mlp  { width: 98%;   background: #1E88E5; }
  .auc-bar.xgb  { width: 99.5%; background: var(--navy); }
  .auc-score {
    width: 68px;
    text-align: right;
    font-size: 17px;
    font-weight: 900;
    color: var(--navy);
    font-family: var(--mono);
  }
  .auc-winner {
    background: var(--blue-bg);
    border-left: 4px solid var(--blue);
    border-radius: 0 8px 8px 0;
    padding: 12px 20px;
    margin: 16px 52px 0;
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
  }
  .auc-winner span { color: var(--blue); }

  /* ════════════════════════════
     CONTENT PAD / BANNER
  ════════════════════════════ */
  .content-pad { padding: 16px 52px; }
  .banner {
    background: var(--blue-bg);
    border-left: 4px solid var(--blue);
    border-radius: 0 8px 8px 0;
    padding: 10px 20px;
    margin: 12px 52px 0;
    font-size: 12.5px;
    color: var(--navy);
    font-weight: 500;
  }

  /* ════════════════════════════
     CONCLUSION
  ════════════════════════════ */
  section.conclusion {
    background: var(--navy);
    color: var(--white);
    padding: 0;
    position: relative;
    overflow: hidden;
  }
  section.conclusion::before {
    content: '';
    position: absolute;
    top: -100px; right: -100px;
    width: 400px; height: 400px;
    border-radius: 50%;
    background: rgba(26,115,232,.15);
    pointer-events: none;
  }
  .concl-body { padding: 44px 72px; }
  .concl-label { font-size: 11px; font-weight: 700; color: var(--blue-lt); letter-spacing: 3px; margin-bottom: 12px; }
  .concl-item {
    display: flex; align-items: flex-start; gap: 20px;
    padding: 13px 0; border-bottom: 1px solid rgba(255,255,255,.08);
  }
  .concl-num { font-size: 26px; font-weight: 900; color: var(--blue-lt); font-family: var(--mono); min-width: 40px; line-height: 1; }
  .concl-text { font-size: 15px; color: rgba(255,255,255,.9); line-height: 1.5; padding-top: 3px; }
  .qa-bar {
    background: var(--blue);
    padding: 18px 72px;
    font-size: 22px;
    font-weight: 700;
    color: var(--white);
    text-align: center;
    margin-top: 10px;
  }

  /* ════════════════════════════
     TAG BADGES (WBS)
  ════════════════════════════ */
  .tag-badge {
    display: inline-block;
    font-size: 11px; font-weight: 700;
    padding: 2px 9px; border-radius: 20px;
  }
  .tag-badge.green { background: #DCFCE7; color: #166534; }
  .tag-badge.amber { background: #FEF3C7; color: #92400E; }
  .tag-badge.gray  { background: var(--gray-lt); color: var(--gray); }

---
<!-- _class: title -->
<!-- _paginate: false -->

<div class="tag">🛒 E-Commerce Churn Solution</div>
<div class="accent-bar"></div>

# 고객 이탈 예측 플랫폼 <span>Re:tain</span>

<p>데이터 기반 고객 유지 전략으로 이커머스의 미래를 만듭니다</p>

<div class="title-bar">
  👥 SKN27기 4팀
  <span>|</span>
  김민경 · 박준희 · 박창제 · 임예은 · 한재웅
  <span>|</span>
  2026. 04. 02
</div>

---

<div class="hdr"><span class="num">AGENDA</span> 목차</div>

<div class="agenda-grid">

<div class="agenda-card">
  <div class="agenda-num">01</div>
  <div class="agenda-text"><h3>프로젝트 개요</h3><p>배경 · 목적 · 팀 구성</p></div>
</div>

<div class="agenda-card">
  <div class="agenda-num">02</div>
  <div class="agenda-text"><h3>데이터 & 전처리</h3><p>결측치 처리 · 이상치 제어 · EDA</p></div>
</div>

<div class="agenda-card">
  <div class="agenda-num">03</div>
  <div class="agenda-text"><h3>피처 엔지니어링</h3><p>10개 파생 변수 설계 · 최종 24개 피처</p></div>
</div>

<div class="agenda-card">
  <div class="agenda-num">04</div>
  <div class="agenda-text"><h3>모델링 & 성능 비교</h3><p>RF · XGBoost · LightGBM · MLP</p></div>
</div>

<div class="agenda-card">
  <div class="agenda-num">05</div>
  <div class="agenda-text"><h3>최종 모델 선정</h3><p>XGBoost · AUC 0.995 · SHAP 분석</p></div>
</div>

<div class="agenda-card">
  <div class="agenda-num">06</div>
  <div class="agenda-text"><h3>서비스 아키텍처</h3><p>Re:tain 플랫폼 · Streamlit · DB</p></div>
</div>

</div>

---

<div class="hdr"><span class="num">01</span> 프로젝트 개요</div>

<div class="two-col" style="padding-top:22px;">

<div class="card">
  <div class="card-head">🔍 문제 정의</div>
  <div class="card-body">
    <p style="font-size:13px;margin:0 0 12px;">이커머스에서 <strong>고객 이탈(Churn)</strong>은 비즈니스의 직접적 손실로 이어집니다.</p>

| 구분 | 내용 |
|------|------|
| 비용 문제 | 신규 고객 유치 비용 ≒ 유지 비용의 5~7배 |
| 탐지 어려움 | 체리피커(혜택만 수령 후 이탈) 식별 불가 |
| 대응 한계 | 이탈 사후 대응은 ROI 낮음 |

  </div>
</div>

<div class="card">
  <div class="card-head blue">🎯 프로젝트 목적</div>
  <div class="card-body">
    <p style="font-size:13px;margin:0 0 12px;"><strong>머신러닝 기반 이탈 예측 모델</strong>로 선제적 고객 관리 체계 구축</p>

| 목표 | 세부 내용 |
|------|----------|
| 모델 비교 | RF / XGBoost / LightGBM / MLP |
| 피처 설계 | 파생 변수 10개로 이탈 패턴 포착 |
| 플랫폼 구현 | Re:tain 대시보드로 실시간 이탈 예측 |

  </div>
</div>

</div>

---

<div class="hdr"><span class="num">02</span> 데이터 개요</div>

<div class="stat-row">
  <div class="stat-card"><div class="stat-val">5,630</div><div class="stat-lbl">전체 데이터 건수</div></div>
  <div class="stat-card"><div class="stat-val">20개</div><div class="stat-lbl">원본 피처 수</div></div>
  <div class="stat-card"><div class="stat-val">16.9%</div><div class="stat-lbl">이탈 고객 비율 (Churn=1)</div></div>
  <div class="stat-card"><div class="stat-val">80/20</div><div class="stat-lbl">Train / Test 분할 비율</div></div>
</div>

<div class="content-pad" style="padding-top:18px;">

| 주요 변수 | 타입 | 설명 |
|-----------|------|------|
| `Churn` | int | 타겟 변수 — 이탈(1) / 유지(0) |
| `Tenure` | float | 가입 기간 (월) |
| `OrderCount` | float | 주문 횟수 |
| `SatisfactionScore` | int | 만족도 점수 (1–5) |
| `CashbackAmount` | float | 캐시백 금액 |
| `DaySinceLastOrder` | float | 마지막 주문 후 경과일 |
| `Complain` | int | 불만 제기 여부 (0/1) |

</div>

---

<div class="hdr"><span class="num">02</span> 데이터 전처리</div>

<div class="two-col" style="padding-top:20px;">

<div class="card">
  <div class="card-head">💊 결측치 처리 — 그룹별 중앙값 대체</div>
  <div class="card-body">

| 피처 | 결측률 | 처리 방법 |
|------|--------|-----------|
| `Tenure` | 4.7% | NumberOfAddress 그룹 중앙값 |
| `DaySinceLastOrder` | 5.5% | 카테고리×로그인기기 중앙값 |
| `OrderCount` | 4.7% | 카테고리×결제수단 중앙값 |
| `OrderAmountHike` | 4.6% | 카테고리 그룹 중앙값 |
| `HourSpendOnApp` | 4.4% | 전체 중앙값 |
| `CouponUsed` | 4.6% | 전체 중앙값 |

  </div>
</div>

<div class="card">
  <div class="card-head blue">📐 이상치 처리 — 분포 기반 차별 적용</div>
  <div class="card-body">

| 피처 | 처리 방식 | 변환 피처명 |
|------|-----------|-------------|
| `Tenure` | 로그 변환 (`log1p`) | `Tenure_log` |
| `WarehouseToHome` | 로그 변환 (`log1p`) | `WH_log` |
| `DaySinceLastOrder` | IQR 클리핑 | `Days_clip` |
| `CashbackAmount` | IQR 클리핑 | `Cashback_clip` |

<div class="banner" style="margin:12px 0 0;">💡 우편향 분포 → 로그 정규화 / 극단값 → IQR 억제</div>

  </div>
</div>

</div>

---

<div class="hdr"><span class="num">03</span> 피처 엔지니어링</div>

<div class="subtitle">EDA 기반 이탈 예측력 강화를 목적으로 함</div>

<div class="three-col">
  <div class="feat-group">
    <h3>행동 패턴 (4개)</h3>
    <ul>
      <li><strong>Dormancy Shock</strong>: 평소 대비 주문 공백의 충격 지수</li>
      <li><strong>Recency Tenure Ratio</strong>: 가입기간 대비 최근 공백 비중</li>
      <li><strong>MonthlyOrderFreq</strong>: 월평균 주문 빈도</li>
      <li><strong>Stagnant Loyal</strong>: 정체된 장기 고객 (가입은 오래됐지만 활동은 평균 이하)</li>
    </ul>
  </div>
  <div class="feat-group muted">
    <h3>만족도 &amp; 경험 (3개)</h3>
    <ul>
      <li><strong>Satisfaction_Per_Order</strong>: 주문당 만족도 효율</li>
      <li><strong>Silent Killer</strong>: 조용한 이탈자 (불만은 낮지만 만족도 낮음)</li>
      <li><strong>IssueIndex</strong>: 불만 제기 여부 (명시적인 부정적 경험)</li>
    </ul>
  </div>
  <div class="feat-group dark">
    <h3>가치 &amp; 반응성 (3개)</h3>
    <ul>
      <li><strong>CashbackPerOrder</strong>: 주문당 캐시백 체감도</li>
      <li><strong>Promo_Sensitivity</strong>: 프로모션 민감도</li>
      <li><strong>ManyAddressesFlag</strong>: 배송지가 많음 (헤비 유저 여부)</li>
    </ul>
  </div>
</div>

<div class="final-process">
  <strong>최종 처리</strong> &nbsp;|&nbsp; 카테고리 피처에 원-핫 인코딩 적용 → 불필요 컬럼 제거 → 최종 <strong>24개 피처</strong>로 모델 학습
</div>

---

<div class="hdr"><span class="num">04</span> 모델링 및 평가</div>

<div class="content-pad">

| 모델명 | 특장점 | 사용 기법 | 하이퍼 파라미터 튜닝 |
|---|---|---|---|
| **Random Forest<br>(박준희)** | 비선형 학습, 안정적 | Manual Search CV | `n_estimators=100, max_depth=12,`<br>`class_weight='balanced', random_state=42` |
| **XGBoost(박창제)** | 최고 정확도, 정규화 | Grid Search CV | `colsample_bytree=0.9, learning_rate=0.1,`<br>`max_depth=5, n_estimators=300, subsample=0.9` |
| **LightGBM(한재웅)** | 빠른 학습, 메모리 효율 | Bayesian Search CV | `max_depth=5, min_samples_split=4,`<br>`criterion='entropy', max_leaf_nodes=9,`<br>`n_estimators=460, learning_rate=0.0811` |
| **다층 퍼셉트론<br>(MLP, 김민경)** | 배포 용이, 실시간 | Standard Scaler,<br>Grid Search CV | `alpha=0.0001,`<br>`hidden_layer_sizes=(50,50),`<br>`learning_rate_init=0.01` |

</div>

---

<div class="hdr"><span class="num">04</span> 혼동행렬 (Confusion Matrix) 비교</div>

<div class="grid-wrapper">
  <div class="model-box">
    <img src="./images/output4.png">
    <p>Random Forest</p>
  </div>
  <div class="model-box">
    <img src="./images/MLP_output.png">
    <p>MLP</p>
  </div>
  <div class="model-box">
    <img src="./images/output.png">
    <p>LightGBM</p>
  </div>
  <div class="model-box">
    <img src="./images/output3.png">
    <p>XGBoost (Best)</p>
  </div>
</div>

---

<div class="hdr"><span class="num">04</span> 팀원 모델링 비교: AUC 성능</div>

<div class="auc-container">
  <div class="auc-row">
    <div class="auc-label">⚡ XGBoost</div>
    <div class="auc-bar-wrap"><div class="auc-bar xgb"></div></div>
    <div class="auc-score">0.995</div>
  </div>
  <div class="auc-row">
    <div class="auc-label">🧠 MLP</div>
    <div class="auc-bar-wrap"><div class="auc-bar mlp"></div></div>
    <div class="auc-score">0.980</div>
  </div>
  <div class="auc-row">
    <div class="auc-label">🚀 LightGBM</div>
    <div class="auc-bar-wrap"><div class="auc-bar lgbm"></div></div>
    <div class="auc-score">0.970</div>
  </div>
  <div class="auc-row">
    <div class="auc-label">🌲 Random Forest</div>
    <div class="auc-bar-wrap"><div class="auc-bar rf"></div></div>
    <div class="auc-score">0.900</div>
  </div>
</div>

<div class="auc-winner">
  ✓ <span>XGBoost</span> &nbsp;|&nbsp; AUC <span>0.995</span> &nbsp;|&nbsp; 최종 선택 모델 ⭐
</div>
