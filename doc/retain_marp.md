---
marp: true
theme: default
paginate: false
html: true
style: |

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

  * {
    font-family: 'Noto Sans KR', sans-serif;
    box-sizing: border-box;
  }

  section {
    background: #ffffff;
    color: #1a1a2e;
    padding: 60px 70px;
    font-size: 18px;
  }

  /* ── Title slide ── */
  section.title {
    background: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px 100px;
  }

  section.title .tag {
    font-size: 13px;
    font-weight: 700;
    color: #1a73e8;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 24px;
  }

  section.title h1 {
    font-size: 52px;
    font-weight: 900;
    color: #0d1b4b;
    line-height: 1.2;
    margin: 0 0 24px 0;
    border: none;
  }

  section.title h1 span {
    color: #1a73e8;
  }

  section.title p {
    font-size: 20px;
    color: #555;
    margin: 0;
    line-height: 1.6;
  }

  section.title .accent-bar {
    width: 60px;
    height: 5px;
    background: #1a73e8;
    border-radius: 3px;
    margin-bottom: 32px;
  }

  /* ── Common headings ── */
  h1, h2 {
    font-weight: 900;
    color: #0d1b4b;
    border: none;
    margin-top: 0;
  }

  h1 { font-size: 38px; margin-bottom: 8px; }
  h2 { font-size: 28px; margin-bottom: 6px; }

  .subtitle {
    color: #666;
    font-size: 15px;
    margin-bottom: 32px;
  }

  /* ── Feature Engineering slide ── */
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 32px;
    margin-top: 8px;
  }

  .feat-group h3 {
    font-size: 17px;
    font-weight: 700;
    color: #1a73e8;
    margin: 0 0 12px 0;
    padding-bottom: 6px;
    border-bottom: 2px solid #1a73e8;
  }

  .feat-group.muted h3 { color: #aaa; border-bottom-color: #aaa; }
  .feat-group.dark h3  { color: #0d1b4b; border-bottom-color: #0d1b4b; }

  .feat-group ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .feat-group ul li {
    font-size: 13.5px;
    color: #333;
    padding: 5px 0 5px 14px;
    border-left: 3px solid transparent;
    line-height: 1.5;
  }

  .feat-group ul li strong {
    color: #0d1b4b;
  }

  .final-process {
    margin-top: 28px;
    background: #f0f5ff;
    border-left: 4px solid #1a73e8;
    padding: 14px 20px;
    border-radius: 0 8px 8px 0;
    font-size: 15px;
    color: #333;
  }

  .final-process strong {
    color: #1a73e8;
    font-weight: 700;
  }

  /* ── Modeling Table slide ── */
  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    font-size: 14px;
    margin-top: 24px;
  }

  thead tr {
    background: #1a73e8;
    color: #fff;
  }

  thead th {
    padding: 14px 16px;
    text-align: center;
    text-align: left;
    font-weight: 700;
    font-size: 15px;
  }

  th:nth-child(1) { width: 15%; } /* 모델명 */
  th:nth-child(2) { width: 20%; } /* 특장점 */
  th:nth-child(3) { width: 20%; } /* 사용 기법 */
  th:nth-child(4) { width: 45%; }

  tbody tr {
    border-bottom: 1px solid #e8eaf0;
  }

  tbody tr:nth-child(even) {
    background: #f7f9ff;
  }

  tbody td {
    padding: 14px 16px;
    vertical-align: middle;
    color: #2c2c2c;
    line-height: 1.5;
    word-break: break-all;
  }

  tbody td:first-child {
    font-weight: 700;
    color: #0d1b4b;
  }

  code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 12.5px;
    background: #f0f2f8;
    padding: 1px 4px;
    border-radius: 3px;
    color: #333;
  }

  /* ── AUC Chart slide ── */
  .auc-container {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 24px;
  }

  .auc-row {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .auc-label {
    width: 200px;
    font-size: 15px;
    font-weight: 600;
    color: #0d1b4b;
    flex-shrink: 0;
  }

  .auc-bar-wrap {
    flex: 1;
    background: #e8eaf0;
    border-radius: 6px;
    height: 36px;
    overflow: hidden;
  }

  .auc-bar {
    height: 100%;
    border-radius: 6px;
    transition: width 0.3s;
  }

  .auc-bar.rf    { width: 90%;   background: #90caf9; }
  .auc-bar.lgbm  { width: 97%;   background: #42a5f5; }
  .auc-bar.mlp   { width: 98%;   background: #1e88e5; }
  .auc-bar.xgb   { width: 99.5%; background: #0d47a1; }

  .auc-score {
    width: 70px;
    text-align: right;
    font-size: 16px;
    font-weight: 700;
    color: #0d1b4b;
  }

  .auc-winner {
    background: #e8f0fe;
    border-left: 4px solid #1a73e8;
    border-radius: 0 8px 8px 0;
    padding: 14px 20px;
    margin-top: 24px;
    font-size: 16px;
    font-weight: 700;
    color: #0d1b4b;
  }

  .auc-winner span { color: #1a73e8; }

  /* ── Confusion Matrix slide ── */

  .grid-wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* 2열 배치 */
    gap: 20px;
    width: 100%;
    margin-top: 20px;
  }

  .model-box {
    background: #fafbff;
    border: 1px solid #e0e4ef;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .model-box img {
    width: 100%;
    max-height: 200px; /* 슬라이드 높이에 맞춰 조절 */
    object-fit: contain;
  }

  .model-box p {
    margin: 10px 0 0 0;
    font-size: 16px;
    font-weight: 700;
    color: #1a73e8;
  }
  .cm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 24px;
  }

  .cm-card {
    border: 1px solid #e0e4ef;
    border-radius: 10px;
    padding: 20px;
    background: #fafbff;
  }

  .cm-card h3 {
    font-size: 15px;
    font-weight: 700;
    color: #0d1b4b;
    margin: 0 0 14px 0;
    text-align: center;
  }

  .cm-matrix {
    display: grid;
    grid-template-columns: auto 1fr 1fr;
    grid-template-rows: auto 1fr 1fr;
    gap: 3px;
    font-size: 12px;
  }

  .cm-matrix .header {
    background: #1a73e8;
    color: #fff;
    font-weight: 700;
    text-align: center;
    padding: 6px;
    border-radius: 4px;
  }

  .cm-matrix .corner { background: transparent; }

  .cm-matrix .tp { background: #1a73e8; color: #fff; font-weight: 700; text-align: center; padding: 12px 8px; border-radius: 4px; }
  .cm-matrix .tn { background: #1a73e8; color: #fff; font-weight: 700; text-align: center; padding: 12px 8px; border-radius: 4px; }
  .cm-matrix .fp { background: #e8eaf0; color: #555; text-align: center; padding: 12px 8px; border-radius: 4px; }
  .cm-matrix .fn { background: #e8eaf0; color: #555; text-align: center; padding: 12px 8px; border-radius: 4px; }
  .cm-matrix .row-label { background: #0d1b4b; color: #fff; font-weight: 700; text-align: center; padding: 6px; border-radius: 4px; writing-mode: vertical-rl; }

  .cm-note {
    font-size: 11px;
    color: #888;
    text-align: center;
    margin-top: 8px;
  }


---

<!-- _class: title -->

<div class="tag">🛒 E-Commerce Churn Solution</div>
<div class="accent-bar"></div>

# 고객 이탈 예측 플랫폼 <span>Re:tain</span>

<p>데이터 기반 고객 유지 전략으로 이커머스의 미래를 만듭니다</p>

---

# 피처 엔지니어링

<div class="subtitle">EDA 기반 이탈 예측력 강화를 목적으로 함</div>

<div class="three-col">
  <div class="feat-group">
    <h3>행동 패턴 (4개)</h3>
    <ul>
      <li><strong>Dormancy Shock</strong>: 평소 대비 주문 공백의 충격 지수</li>
      <li><strong>Recency Tenure Ratio</strong>: 가입기간 대비 최근 공백 비중</li>
      <li><strong>MonthlyOrderFreq</strong>: 월평균 주문 빈도</li>
      <li><strong>Stagnant Loyal</strong>: 정체된 장기 고객 <br>(가입은 오래됐지만 활동은 평균 이하)</li>
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

# 모델링 및 평가

| 모델명 | 특장점 | 사용 기법 | 하이퍼 파라미터 튜닝 |
|---|---|---|---|
| **Random Forest<br>(박준희)** | 비선형 학습, 안정적 | Manual Search CV | `n_estimators=100, max_depth=12,`<br>`class_weight='balanced', random_state=42` |
| **XGBoost(박창제)** | 최고 정확도, 정규화 | Grid Search CV | `colsample_bytree=0.9, learning_rate=0.1,`<br>`max_depth=5, n_estimators=300, subsample=0.9` |
| **LightGBM(한재웅)** | 빠른 학습, 메모리 효율 | Bayesian Search CV | `max_depth=5, min_samples_split=4,`<br>`criterion='entropy', max_leaf_nodes=9,`<br>`n_estimators=460, learning_rate=0.0811` |
| **다층 퍼셉트론<br>(MLP,김민경)** | 배포 용이, 실시간 | Standard Scaler,<br>Grid Search CV | `alpha=0.0001,`<br>`hidden_layer_sizes=(50,50),`<br>`learning_rate_init=0.01` |

---

# 혼동행렬 (Confusion Matrix) 비교

<div class="grid-wrapper">
  <div class="model-box">
    <img src="./images/output4.png"> <p>Random Forest</p>
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

# 팀원 모델링 비교: AUC 성능

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
