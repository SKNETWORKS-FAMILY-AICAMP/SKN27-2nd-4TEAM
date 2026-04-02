---
marp: true
theme: default
paginate: true
lang: ko
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Space+Mono:wght@400;700&display=swap');

  section {
    font-family: 'Noto Sans KR', sans-serif;
    background: #f5f9ff;
    color: #1a2332;
    padding: 52px 70px;
    line-height: 1.6;
    font-size: 16px;
    position: relative;
  }

  section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #0d1f3c, #1e8fc5, #00d4ff);
  }

  section.cover {
    background: linear-gradient(135deg, #0d1f3c 0%, #1a4a8a 60%, #1e5fa0 100%);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover::before {
    background: linear-gradient(90deg, #00d4ff, #1e8fc5, #ffffff);
  }

  section.cover h1 {
    font-size: 62px;
    font-weight: 900;
    line-height: 1.1;
    letter-spacing: -2px;
    color: white;
    margin: 0 0 16px 0;
    border: none;
    padding: 0;
  }

  section.cover .accent { color: #00d4ff; }

  section.cover p.sub {
    font-size: 19px;
    color: rgba(255,255,255,0.72);
    font-weight: 300;
    margin: 0;
  }

  section.cover .tags {
    display: flex;
    gap: 10px;
    margin-bottom: 28px;
  }

  section.cover .tag {
    border: 1px solid rgba(255,255,255,0.4);
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 14px;
    color: rgba(255,255,255,0.8);
    display: inline-block;
  }

  h1 {
    font-size: 44px;
    font-weight: 900;
    color: #0d1f3c;
    letter-spacing: -1px;
    border: none;
    margin: 0 0 6px 0;
    padding: 0;
  }

  h2 { font-size: 22px; font-weight: 700; color: #0d1f3c; margin: 0 0 12px 0; }
  h3 { font-size: 18px; font-weight: 700; color: #0d1f3c; margin: 0 0 8px 0; }

  .label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #1e8fc5;
    margin-bottom: 8px;
    display: block;
  }

  .subtitle {
    font-size: 16px;
    color: #8898aa;
    margin-bottom: 30px;
    display: block;
  }

  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  th { background: #0d1f3c; color: white; padding: 12px 15px; font-weight: 500; font-size: 13px; text-align: left; }
  td { padding: 11px 15px; border-bottom: 1px solid #e8f0f8; color: #334; font-size: 13px; }
  tr:nth-child(even) td { background: #f7faff; }
  tr:last-child td { border-bottom: none; }

  .card-row { display: flex; gap: 16px; margin-bottom: 18px; }
  .card { flex: 1; background: #f0f7ff; border: 1px solid #d4e8f7; border-radius: 14px; padding: 20px; }
  .card-dark { flex: 1; background: #0d1f3c; border-radius: 14px; padding: 20px; color: white; }
  .card h3 { color: #0d1f3c; font-size: 16px; margin-bottom: 10px; }
  .card-dark h3 { color: #00d4ff; font-size: 16px; margin-bottom: 10px; }
  .card ul, .card-dark ul { margin: 0; padding-left: 16px; font-size: 13px; }
  .card li { color: #445; margin-bottom: 4px; }
  .card-dark li { color: rgba(255,255,255,0.8); margin-bottom: 4px; }

  .info-box {
    background: linear-gradient(135deg, #e0f0ff, #d0e8ff);
    border-left: 4px solid #1e8fc5;
    border-radius: 10px;
    padding: 14px 20px;
    margin-top: 20px;
    font-size: 15px;
    color: #0d1f3c;
  }
  .info-box strong { color: #1e8fc5; }

  .stat-row { display: flex; gap: 16px; margin-bottom: 28px; }
  .stat-box { flex: 1; background: white; border: 1px solid #d4e8f7; border-radius: 14px; padding: 20px; text-align: center; }
  .stat-num { font-family: 'Space Mono', monospace; font-size: 42px; font-weight: 700; color: #0d1f3c; display: block; line-height: 1; margin-bottom: 6px; }
  .stat-num.accent { color: #1e8fc5; }
  .stat-lbl { font-size: 12px; color: #8898aa; }

  .tl-item { display: flex; gap: 18px; margin-bottom: 22px; align-items: flex-start; }
  .tl-dot { width: 26px; height: 26px; min-width: 26px; background: #1e8fc5; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Space Mono', monospace; font-size: 11px; font-weight: 700; color: white; }
  .tl-date { font-family: 'Space Mono', monospace; font-size: 12px; color: #1e8fc5; margin-bottom: 3px; }
  .tl-label { font-size: 18px; font-weight: 700; color: #0d1f3c; margin-bottom: 6px; }
  .tl-chips { display: flex; flex-wrap: wrap; gap: 6px; }
  .chip { background: #f0f7ff; border: 1px solid #c8e0f4; border-radius: 20px; padding: 4px 12px; font-size: 13px; color: #1a4a8a; }

  .col2 { display: flex; gap: 24px; }
  .col2 > div { flex: 1; }
  .feat-header { font-size: 16px; font-weight: 700; color: #0d1f3c; margin-bottom: 10px; }

  .platform-row { display: flex; gap: 16px; margin-bottom: 20px; }
  .platform-card { flex: 1; background: #f0f7ff; border: 1px solid #d4e8f7; border-radius: 14px; padding: 22px; text-align: center; }
  .platform-card .picon { font-size: 30px; margin-bottom: 10px; display: block; }
  .platform-card h3 { font-family: 'Space Mono', monospace; font-size: 14px; color: #0d1f3c; margin-bottom: 12px; }
  .platform-card ul { list-style: none; padding: 0; text-align: left; font-size: 13px; }
  .platform-card li { color: #445; margin-bottom: 5px; padding-left: 14px; position: relative; }
  .platform-card li::before { content: '▸'; position: absolute; left: 0; color: #1e8fc5; font-size: 10px; }

  .conclude-row { display: flex; gap: 16px; margin-bottom: 18px; }
  .conclude-card { flex: 1; background: white; border: 1px solid #d4e8f7; border-radius: 14px; padding: 24px; position: relative; overflow: hidden; }
  .conclude-card::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #1e8fc5, #00d4ff); }
  .conclude-card .icon { font-size: 28px; margin-bottom: 10px; display: block; }
  .conclude-card h3 { font-size: 16px; margin-bottom: 8px; }
  .conclude-card p { font-size: 13px; color: #8898aa; line-height: 1.5; margin: 0; }

  .tech-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
  .tech-badge { background: #0d1f3c; color: #00d4ff; border-radius: 8px; padding: 7px 16px; font-family: 'Space Mono', monospace; font-size: 13px; font-weight: 700; }

  .cm-row { display: flex; gap: 16px; margin-top: 8px; }
  .cm-box { flex: 1; background: white; border: 1px solid #d4e8f7; border-radius: 14px; overflow: hidden; }
  .cm-box img { width: 100%; display: block; }
  .cm-box p { text-align: center; font-size: 14px; font-weight: 700; color: #0d1f3c; padding: 10px 6px; background: #f0f7ff; border-top: 1px solid #d4e8f7; margin: 0; }

  .card-name { font-size: 20px; font-weight: 700; color: #0d1f3c; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 2px solid #1e8fc5; display: flex; align-items: center; gap: 8px; }
  .role-badge { font-size: 11px; background: #1e8fc5; color: white; padding: 2px 10px; border-radius: 10px; font-weight: 500; }

  code { font-family: 'Space Mono', monospace; font-size: 11px; color: #1a4a8a; background: #eaf3ff; border-radius: 4px; padding: 1px 4px; }

  header, footer { display: none; }
---

<!-- _class: cover -->

<div class="tags">
  <span class="tag">팀 프로젝트</span>
  <span class="tag">데이터 분석</span>
  <span class="tag">머신러닝</span>
</div>

# <span class="accent">Re:tain</span><br>고객 이탈<br>예측 플랫폼

<p class="sub">머신러닝 기반의 고객 이탈 예측 시스템으로 비즈니스 가치를 창출합니다</p>

---

<span class="label">Table of Contents</span>

# 목차

<div class="card-row">
  <div class="card"><h3>📋 프로젝트 개요</h3><ul><li>배경 · 문제 정의</li><li>팀 구성</li><li>프로젝트 목적</li></ul></div>
  <div class="card"><h3>📅 WBS & 일정</h3><ul><li>작업 단계</li><li>역할 분담</li></ul></div>
  <div class="card"><h3>💾 데이터 & 전처리</h3><ul><li>결측치 처리</li><li>이상치 제어</li><li>EDA</li></ul></div>
</div>
<div class="card-row">
  <div class="card"><h3>⚙️ 피처 엔지니어링</h3><ul><li>10개 파생 변수 설계</li><li>최종 24개 피처</li></ul></div>
  <div class="card"><h3>🤖 모델링 & 성능 비교</h3><ul><li>RF · XGBoost</li><li>LightGBM · MLP</li></ul></div>
  <div class="card"><h3>🚀 서비스 & 기대 효과</h3><ul><li>Re:tain 플랫폼</li><li>Streamlit 대시보드</li><li>결론</li></ul></div>
</div>

---

<span class="label">Project Overview</span>

# 프로젝트 개요 — 문제 정의

<span class="subtitle">머신러닝 기반 이탈 예측 모델로 선제적 고객 관리 체계를 구축합니다</span>

<div class="card-row">
  <div class="card-dark"><h3>🎯 모델 비교</h3><ul><li>RF / XGBoost / LightGBM / MLP</li><li>4종 평가 및 최적 선택</li></ul></div>
  <div class="card-dark"><h3>⚙️ 피처 설계</h3><ul><li>파생 변수 10개로 이탈 패턴 정밀 포착</li><li>최종 24개 피처 학습</li></ul></div>
  <div class="card-dark"><h3>💻 플랫폼 구현</h3><ul><li>Re:tain 대시보드로 실시간 이탈 예측 제공</li><li>Streamlit 3페이지 구성</li></ul></div>
</div>

<div class="info-box">💡 <strong>'고객이 떠난 이후 대응'이 아니라 '떠나기 전에 미리 대응'</strong></div>

---

<span class="label">Team</span>

# 팀 구성

<div class="card-row">
  <div class="card"><div class="card-name">김민경 <span class="role-badge">팀장</span></div><ul><li>Feature Engineering</li><li>MLP 모델링</li><li>DB 연결 · 최종 점검</li></ul></div>
  <div class="card"><div class="card-name">박준희</div><ul><li>데이터 전처리 (결측치)</li><li>Random Forest 모델링</li></ul></div>
  <div class="card"><div class="card-name">박창제</div><ul><li>데이터 전처리 (결측치)</li><li>XGBoost 모델링</li></ul></div>
</div>
<div class="card-row">
  <div class="card"><div class="card-name">한재웅</div><ul><li>데이터 전처리 (이상치)</li><li>LightGBM 모델링</li></ul></div>
  <div class="card"><div class="card-name">임예은</div><ul><li>소비 트렌드 데이터 수집</li><li>Streamlit 개발</li></ul></div>
  <div class="card" style="background:transparent;border:1px dashed #d4e8f7;"></div>
</div>

---

<span class="label">Work Breakdown Structure</span>

# WBS — 작업 일정

<div class="tl-item">
  <div class="tl-dot">1</div>
  <div><div class="tl-date">3/26 ~ 3/27</div><div class="tl-label">분석 및 설계</div><div class="tl-chips"><span class="chip">환경 세팅</span><span class="chip">데이터 이해</span><span class="chip">기획서 작성</span><span class="chip">역할 분담</span></div></div>
</div>
<div class="tl-item">
  <div class="tl-dot">2</div>
  <div><div class="tl-date">3/27 ~ 3/31</div><div class="tl-label">전처리 & 모델링</div><div class="tl-chips"><span class="chip">결측치 / 이상치 처리</span><span class="chip">Feature Engineering</span><span class="chip">4개 모델 학습 및 성능 비교</span></div></div>
</div>
<div class="tl-item">
  <div class="tl-dot">3</div>
  <div><div class="tl-date">3/30 ~ 4/1</div><div class="tl-label">서비스 개발</div><div class="tl-chips"><span class="chip">Streamlit 3페이지 구현</span><span class="chip">PostgreSQL DB 연결</span><span class="chip">UI 통합 테스트</span></div></div>
</div>
<div class="tl-item">
  <div class="tl-dot">4</div>
  <div><div class="tl-date">4/2</div><div class="tl-label">발표 준비</div><div class="tl-chips"><span class="chip">PPT 작성</span><span class="chip">최종 시연 준비</span><span class="chip">발표 리허설</span></div></div>
</div>

---

<span class="label">Data & Preprocessing</span>

# 데이터 & 전처리

<div class="stat-row">
  <div class="stat-box"><span class="stat-num">5,630</span><span class="stat-lbl">전체 데이터 건수</span></div>
  <div class="stat-box"><span class="stat-num">20</span><span class="stat-lbl">원본 피처 수</span></div>
  <div class="stat-box"><span class="stat-num accent">16.9%</span><span class="stat-lbl">이탈 고객 비율 (Churn=1)</span></div>
  <div class="stat-box"><span class="stat-num">80/20</span><span class="stat-lbl">Train / Test 분할</span></div>
</div>

<div class="col2">
<div>
<div class="feat-header">🔧 결측치 처리 — 그룹별 중앙값 대체</div>

| 피처 | 결측률 | 처리 방법 |
|---|---|---|
| Tenure | 4.7% | NumberOfAddress 그룹 중앙값 |
| WarehouseToHome | 4.5% | 전체 중앙값 |
| DaySinceLastOrder | 5.5% | 카테고리×로그인기기 중앙값 |
| OrderCount | 4.7% | 카테고리×결제수단 중앙값 |
| OrderAmountHike | 4.6% | 카테고리 그룹 중앙값 |
| HourSpendOnApp | 4.4% | 전체 중앙값 |
| CouponUsed | 4.6% | 전체 중앙값 |

</div>
<div>
<div class="feat-header">📐 이상치 처리 — 분포 기반 차별 적용</div>

| 피처 | 처리 방식 | 변환 피처명 |
|---|---|---|
| Tenure | 로그 변환 (log1p) | Tenure_log |
| WarehouseToHome | 로그 변환 (log1p) | WH_log |
| DaySinceLastOrder | IQR 클리핑 | Days_clip |
| CashbackAmount | IQR 클리핑 | Cashback_clip |

<div class="info-box" style="font-size:15px;">💡 <strong>우편향 분포 → 로그 정규화 / 극단값 → IQR 억제</strong></div>
</div>
</div>

---

<span class="label">Feature Engineering</span>

# 피처 엔지니어링

<span class="subtitle">EDA 기반 이탈 예측력 강화 — 총 10개 파생 변수 설계</span>

<div class="card-row">
  <div class="card"><h3>🏃 행동 패턴 (4개)</h3><ul><li><strong>Dormancy Shock</strong> — 평소 대비 주문 공백의 충격 지수</li><li><strong>Recency Tenure Ratio</strong> — 가입기간 대비 최근 공백 비중</li><li><strong>MonthlyOrderFreq</strong> — 월평균 주문 빈도</li><li><strong>Stagnant Loyal</strong> — 가입은 오래됐지만 활동 평균 이하</li></ul></div>
  <div class="card"><h3>⭐ 만족도 & 경험 (3개)</h3><ul><li><strong>Satisfaction_Per_Order</strong> — 주문당 만족도 효율</li><li><strong>Silent Killer</strong> — 불만 낮지만 만족도도 낮은 잠재 이탈자</li><li><strong>IssueIndex</strong> — 불만 제기 여부 (명시적 부정 경험)</li></ul></div>
  <div class="card"><h3>💰 가치 & 반응성 (3개)</h3><ul><li><strong>CashbackPerOrder</strong> — 주문당 캐시백 체감도</li><li><strong>Promo_Sensitivity</strong> — 프로모션 민감도</li><li><strong>ManyAddressesFlag</strong> — 헤비 유저 여부 (배송지 다수)</li></ul></div>
</div>

<div class="info-box">📌 최종 처리 | 카테고리 피처 원-핫 인코딩 → 불필요 컬럼 제거 → <strong>최종 24개 피처로 모델 학습</strong></div>

---

<span class="label">Modeling & Performance</span>

# 모델링 & 성능 비교

<div class="col2">
<div>

| 모델명 | 특장점 | 사용 기법 | 하이퍼파라미터 |
|---|---|---|---|
| 🌲 **RF** | 비선형, 안정적 | Manual Search CV | `n_estimators=100, max_depth=12, class_weight='balanced'` |
| ⭐ **XGBoost** | 최고 정확도 | Grid Search CV | `colsample_bytree=0.9, lr=0.1, max_depth=5, n_est=300` |
| 🚀 **LightGBM** | 빠른 학습 | Bayesian Search CV | `max_depth=5, n_est=460, learning_rate=0.0811` |
| 🧠 **MLP** | 배포 용이 | Standard Scaler | `alpha=0.0001, hidden_layer_sizes=(50,50)` |

</div>
<div>

<div style="background:white;border:1px solid #d4e8f7;border-radius:14px;padding:16px 14px 12px;">
<div style="font-size:14px;color:#0d1f3c;font-weight:700;margin-bottom:2px;">AUC 성능 비교</div>
<div style="font-size:11px;color:#8898aa;margin-bottom:14px;">기준선: 0.88 (차이 강조)</div>

<div style="display:flex;flex-direction:column;gap:10px;">

  <div style="display:flex;align-items:center;gap:10px;">
    <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:#0d1f3c;min-width:32px;">⭐</span>
    <span style="font-size:12px;color:#555;min-width:64px;">XGBoost</span>
    <div style="flex:1;background:#e8f0f8;border-radius:4px;height:28px;overflow:hidden;">
      <div style="width:95.8%;height:100%;background:linear-gradient(to right,#0d1f3c,#1a4a8a);border-radius:4px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;">
        <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:white;">0.995</span>
      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:10px;">
    <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:#1a4a8a;min-width:32px;">🚀</span>
    <span style="font-size:12px;color:#555;min-width:64px;">LightGBM</span>
    <div style="flex:1;background:#e8f0f8;border-radius:4px;height:28px;overflow:hidden;">
      <div style="width:80%;height:100%;background:linear-gradient(to right,#1a4a8a,#1e8fc5);border-radius:4px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;">
        <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:white;">0.976</span>
      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:10px;">
    <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:#1e8fc5;min-width:32px;">🧠</span>
    <span style="font-size:12px;color:#555;min-width:64px;">MLP</span>
    <div style="flex:1;background:#e8f0f8;border-radius:4px;height:28px;overflow:hidden;">
      <div style="width:74.2%;height:100%;background:linear-gradient(to right,#1e8fc5,#4ab8e0);border-radius:4px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;">
        <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:white;">0.969</span>
      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:10px;">
    <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:#4ab8e0;min-width:32px;">🌲</span>
    <span style="font-size:12px;color:#555;min-width:64px;">R. Forest</span>
    <div style="flex:1;background:#e8f0f8;border-radius:4px;height:28px;overflow:hidden;">
      <div style="width:16.7%;height:100%;background:linear-gradient(to right,#4ab8e0,#a0d8f0);border-radius:4px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;">
        <span style="font-family:'Space Mono',monospace;font-size:11px;font-weight:700;color:white;">0.900</span>
      </div>
    </div>
  </div>

</div>
</div>

</div>
</div>

<div class="info-box">✅ <strong>최종 선택: XGBoost | AUC 0.995</strong> | 불균형 데이터(16.9% 이탈)에서도 안정적 · SHAP 해석 가능 · Streamlit 배포 용이</div>

---

<span class="label">Model Evaluation</span>

# 혼동행렬 (Confusion Matrix) 비교

<span class="subtitle">4개 모델의 예측 결과를 실제 레이블과 비교</span>

<div class="cm-row">
  <div class="cm-box"><img src="./images/output4.png" alt="Random Forest"><p>🌲 Random Forest</p></div>
  <div class="cm-box"><img src="./images/MLP_output.png" alt="MLP"><p>🧠 MLP</p></div>
  <div class="cm-box"><img src="./images/output.png" alt="LightGBM"><p>🚀 LightGBM</p></div>
  <div class="cm-box"><img src="./images/output3.png" alt="XGBoost"><p>⭐ XGBoost</p></div>
</div>

<div class="info-box">✅ <strong>XGBoost</strong>가 이탈 고객(Churn=1) 탐지에서 가장 높은 재현율(Recall) 달성 — 놓친 이탈자 최소화</div>

---

<span class="label">Service & Conclusion</span>

# 서비스 구성 & 결론

<span class="subtitle">데이터로 고객의 마음을 붙잡다</span>

<div class="platform-row">
  <div class="platform-card"><span class="picon">📊</span><h3>Churn Dashboard</h3><ul><li>고객별 이탈 확률 예측</li><li>위험군 분류 (High / Medium / Low)</li><li>실시간 예측 결과 시각화</li></ul></div>
  <div class="platform-card"><span class="picon">🔍</span><h3>Behavior Analysis</h3><ul><li>RFM 세그먼트 분석</li><li>구매 패턴 · 쿠폰 사용 트렌드</li><li>만족도 영향 분석</li></ul></div>
  <div class="platform-card"><span class="picon">📈</span><h3>Consumer Trends</h3><ul><li>한국 소비 트렌드 시각화</li><li>통계청 공공데이터 기반</li><li>경제적 맥락과 이탈 원인 해석</li></ul></div>
</div>

<div class="conclude-row">
  <div class="conclude-card"><span class="icon">🎯</span><h3>이탈 예측 정확도 극대화</h3><p>XGBoost AUC 0.995로 실용적 수준의 예측 달성</p></div>
  <div class="conclude-card"><span class="icon">💡</span><h3>파생 변수의 중요성 입증</h3><p>행동·만족도·가치 기반 10개 피처가 모델 성능 향상에 핵심 기여</p></div>
  <div class="conclude-card"><span class="icon">🚀</span><h3>Re:tain 플랫폼 구현</h3><p>Streamlit 기반 3페이지 대시보드로 현업 활용 가능한 의사결정 지원 시스템 완성</p></div>
</div>

<div class="tech-row">
  <span class="tech-badge">Streamlit</span><span class="tech-badge">XGBoost</span><span class="tech-badge">PostgreSQL</span><span class="tech-badge">Docker</span><span class="tech-badge">SHAP</span><span class="tech-badge">LightGBM</span><span class="tech-badge">Random Forest</span><span class="tech-badge">MLP</span><span class="tech-badge">Optuna</span>
</div>
