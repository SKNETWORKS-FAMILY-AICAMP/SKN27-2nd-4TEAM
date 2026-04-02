---
marp: true
theme: default
paginate: true
html: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

  :root {
    --navy:    #0d1b4b;
    --blue:    #1a73e8;
    --blue-lt: #4a9ef5;
    --blue-bg: #e8f0fe;
    --white:   #ffffff;
    --off:     #f7f9ff;
    --gray:    #64748b;
    --gray-lt: #e8eaf0;
    --green:   #166534;
    --mono:    'JetBrains Mono', monospace;
    --hdr-h:   64px;
    --pad:     52px;
  }

  * {
    font-family: 'Noto Sans KR', sans-serif;
    box-sizing: border-box;
    margin: 0; padding: 0; border: none;
  }

  section {
    background: #ffffff;
    color: var(--navy);
    width: 1280px;
    height: 720px;
    padding: 0;
    font-size: 16px;
    overflow: hidden;
    position: relative;
  }

  section::after { color: var(--gray); font-size: 12px; }

  /* ─────────────────────────────────────
     HEADER — 모든 슬라이드 상단 고정
  ───────────────────────────────────── */
  .hdr {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: var(--hdr-h);
    background: var(--navy);
    color: #fff;
    font-size: 21px;
    font-weight: 700;
    padding: 0 var(--pad);
    display: flex;
    align-items: center;
    gap: 12px;
    letter-spacing: -0.2px;
  }
  .hdr .num {
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 700;
    color: var(--blue-lt);
    letter-spacing: 3px;
  }

  /* ─────────────────────────────────────
     BODY — 헤더 아래 본문 (항상 동일 위치)
  ───────────────────────────────────── */
  .body {
    position: absolute;
    top: calc(var(--hdr-h) + 20px);
    left: var(--pad);
    right: var(--pad);
    bottom: 24px;
  }

  /* ─────────────────────────────────────
     TITLE SLIDE
  ───────────────────────────────────── */
  section.title {
    background: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 72px 88px;
  }
  .t-tag {
    font-size: 12px; font-weight: 700;
    color: var(--blue);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .t-bar {
    width: 56px; height: 5px;
    background: var(--blue);
    border-radius: 3px;
    margin-bottom: 28px;
  }
  section.title h1 {
    font-size: 58px; font-weight: 900;
    color: var(--navy);
    line-height: 1.15;
    margin-bottom: 20px;
  }
  section.title h1 span { color: var(--blue); }
  section.title .sub {
    font-size: 19px; font-weight: 300;
    color: #666;
    margin-bottom: 44px;
    line-height: 1.6;
  }
  .t-meta {
    display: flex; align-items: center;
    font-size: 14px; color: #888;
    background: var(--off);
    border: 1px solid var(--gray-lt);
    padding: 14px 24px;
    border-radius: 8px;
    width: fit-content;
  }
  .t-meta span { margin: 0 14px; opacity: .4; }

  /* ─────────────────────────────────────
     AGENDA
  ───────────────────────────────────── */
  .agenda-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .agenda-card {
    background: var(--off);
    border-radius: 10px;
    display: flex; align-items: center; gap: 20px;
    padding: 18px 22px;
    border-left: 4px solid var(--blue);
  }
  .agenda-num {
    font-size: 30px; font-weight: 900;
    color: var(--blue);
    font-family: var(--mono);
    min-width: 40px; line-height: 1;
  }
  .agenda-text h3 {
    font-size: 16px; font-weight: 700;
    color: var(--navy); margin-bottom: 3px;
  }
  .agenda-text p { font-size: 13px; color: var(--gray); }

  /* ─────────────────────────────────────
     CARDS
  ───────────────────────────────────── */
  .card {
    background: var(--white);
    border-radius: 12px;
    border: 1px solid var(--gray-lt);
    overflow: hidden;
  }
  .card-hd {
    font-size: 14px; font-weight: 700;
    padding: 11px 20px;
    color: #fff;
    background: var(--navy);
  }
  .card-hd.blue  { background: var(--blue); }
  .card-hd.green { background: var(--green); }
  .card-bd { padding: 16px 20px; }

  /* ─────────────────────────────────────
     TABLE
  ───────────────────────────────────── */
  table { width: 100%; border-collapse: collapse; }
  thead tr { background: var(--navy); color: #fff; }
  thead th {
    padding: 10px 14px;
    text-align: left;
    font-size: 13.5px; font-weight: 700;
  }
  tbody tr { border-bottom: 1px solid var(--gray-lt); }
  tbody tr:nth-child(even) { background: #f7f9ff; }
  tbody td {
    padding: 9px 14px;
    font-size: 13.5px;
    color: #2c2c2c;
    vertical-align: middle;
    line-height: 1.55;
  }
  tbody td:first-child { font-weight: 600; color: var(--navy); }

  code {
    font-family: var(--mono);
    font-size: 12px;
    background: #f0f2f8;
    padding: 2px 5px;
    border-radius: 3px;
    color: #333;
  }

  /* ─────────────────────────────────────
     GRIDS
  ───────────────────────────────────── */
  .two-col   { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
  .three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
  .four-col  { display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; }

  /* ─────────────────────────────────────
     STAT CARDS
  ───────────────────────────────────── */
  .stat-card {
    background: var(--blue);
    border-radius: 12px;
    padding: 20px 16px 16px;
    text-align: center;
    color: #fff;
  }
  .stat-val {
    font-size: 34px; font-weight: 900;
    line-height: 1; font-family: var(--mono);
  }
  .stat-lbl { font-size: 12.5px; opacity: .88; margin-top: 7px; }

  /* ─────────────────────────────────────
     PROBLEM ROWS
  ───────────────────────────────────── */
  .prob-row {
    display: flex; align-items: flex-start; gap: 14px;
    padding: 12px 0;
    border-bottom: 1px solid var(--gray-lt);
  }
  .prob-row:last-child { border-bottom: none; }
  .prob-icon {
    font-size: 20px;
    width: 40px; height: 40px;
    background: var(--blue-bg);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
  .prob-title { font-size: 15px; font-weight: 700; color: var(--navy); margin-bottom: 3px; }
  .prob-desc  { font-size: 13px; color: var(--gray); line-height: 1.5; }

  /* ─────────────────────────────────────
     OBJECTIVE LIST
  ───────────────────────────────────── */
  .obj-item {
    display: flex; align-items: center; gap: 14px;
    background: var(--off);
    border-radius: 8px;
    padding: 12px 18px;
    margin-bottom: 10px;
  }
  .obj-item:last-child { margin-bottom: 0; }
  .obj-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--blue); flex-shrink: 0; }
  .obj-label { font-size: 14px; font-weight: 700; color: var(--navy); min-width: 80px; }
  .obj-desc  { font-size: 13.5px; color: var(--gray); }

  /* ─────────────────────────────────────
     TEAM CARDS
  ───────────────────────────────────── */
  .member-card {
    background: var(--off);
    border-radius: 12px;
    border: 1px solid var(--gray-lt);
    border-top: 4px solid var(--blue);
    padding: 22px 14px 18px;
    text-align: center;
  }
  .member-avatar {
    width: 48px; height: 48px;
    background: var(--blue-bg);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
    margin: 0 auto 12px;
  }
  .member-name { font-size: 16px; font-weight: 700; color: var(--navy); margin-bottom: 8px; }
  .member-role { font-size: 12.5px; color: var(--gray); line-height: 1.7; }

  /* ─────────────────────────────────────
     WBS TIMELINE
  ───────────────────────────────────── */
  .wbs-item {
    display: flex; align-items: stretch;
    border: 1px solid var(--gray-lt);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 12px;
  }
  .wbs-item:last-child { margin-bottom: 0; }
  .wbs-period {
    background: var(--navy); color: #fff;
    font-size: 13px; font-weight: 700;
    font-family: var(--mono);
    padding: 14px 18px;
    display: flex; align-items: center;
    min-width: 155px;
  }
  .wbs-step {
    background: var(--blue); color: #fff;
    font-size: 14px; font-weight: 700;
    padding: 14px 20px;
    display: flex; align-items: center;
    min-width: 140px;
  }
  .wbs-tasks {
    padding: 14px 22px;
    font-size: 13.5px; color: #333;
    display: flex; align-items: center;
    flex: 1; line-height: 1.6;
    background: #fff;
  }

  /* ─────────────────────────────────────
     FEATURE GROUPS
  ───────────────────────────────────── */
  .feat-group {
    background: #fff;
    border-radius: 12px;
    border: 1px solid var(--gray-lt);
    overflow: hidden;
  }
  .feat-group h3 {
    font-size: 14px; font-weight: 700;
    color: #fff;
    background: var(--blue);
    padding: 11px 16px;
  }
  .feat-group.muted h3 { background: var(--navy); }
  .feat-group.dark h3  { background: #2d6a4f; }
  .feat-group ul { list-style: none; }
  .feat-group ul li {
    font-size: 13px; color: #333;
    padding: 9px 16px;
    border-bottom: 1px solid var(--gray-lt);
    line-height: 1.55;
  }
  .feat-group ul li:last-child { border-bottom: none; }
  .feat-group ul li strong { color: var(--navy); font-weight: 700; }

  /* ─────────────────────────────────────
     AUC BARS
  ───────────────────────────────────── */
  .auc-item {
    display: flex; align-items: center; gap: 16px;
    margin-bottom: 16px;
  }
  .auc-item:last-child { margin-bottom: 0; }
  .auc-label {
    width: 210px; flex-shrink: 0;
    font-size: 15px; font-weight: 700;
    color: var(--navy);
  }
  .auc-track {
    flex: 1; height: 40px;
    background: var(--gray-lt);
    border-radius: 6px;
    overflow: hidden;
  }
  .auc-fill { height: 100%; border-radius: 6px; }
  .auc-fill.xgb  { width: 99.5%; background: var(--navy); }
  .auc-fill.lgbm { width: 97.6%; background: #2563eb; }
  .auc-fill.mlp  { width: 96.9%; background: #3b82f6; }
  .auc-fill.rf   { width: 90%;   background: #93c5fd; }
  .auc-score {
    width: 68px; text-align: right;
    font-size: 18px; font-weight: 900;
    color: var(--navy); font-family: var(--mono);
  }

  /* ─────────────────────────────────────
     CONFUSION MATRIX GRID
  ───────────────────────────────────── */
  .cm-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .cm-box {
    background: var(--off);
    border: 1px solid var(--gray-lt);
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    display: flex; flex-direction: column;
    align-items: center;
  }
  .cm-box img { width: 100%; max-height: 205px; object-fit: contain; }
  .cm-box p { margin-top: 8px; font-size: 14px; font-weight: 700; color: var(--blue); }

  /* ─────────────────────────────────────
     SERVICE PAGE CARDS
  ───────────────────────────────────── */
  .page-card {
    background: #fff;
    border-radius: 12px;
    border: 1px solid var(--gray-lt);
    overflow: hidden;
  }
  .page-card-hd {
    font-size: 15px; font-weight: 700;
    color: #fff; padding: 13px 18px;
  }
  .page-card-hd.c1 { background: var(--navy); }
  .page-card-hd.c2 { background: var(--blue); }
  .page-card-hd.c3 { background: #2d6a4f; }
  .page-card-bd {
    padding: 16px 18px;
    font-size: 14px; color: #333;
    line-height: 1.9;
  }

  /* ─────────────────────────────────────
     EFFECT CARDS
  ───────────────────────────────────── */
  .effect-card {
    background: var(--off);
    border-radius: 12px;
    border: 1px solid var(--gray-lt);
    border-top: 4px solid var(--blue);
    padding: 22px 16px 18px;
    text-align: center;
  }
  .effect-icon  { font-size: 32px; margin-bottom: 10px; }
  .effect-title { font-size: 15px; font-weight: 700; color: var(--navy); margin-bottom: 7px; }
  .effect-desc  { font-size: 13px; color: var(--gray); line-height: 1.6; }

  /* ─────────────────────────────────────
     BANNER
  ───────────────────────────────────── */
  .banner {
    background: var(--blue-bg);
    border-left: 4px solid var(--blue);
    border-radius: 0 8px 8px 0;
    padding: 11px 20px;
    font-size: 13.5px; font-weight: 500;
    color: var(--navy);
    margin-top: 14px;
  }
  .banner strong { color: var(--blue); }

  /* ─────────────────────────────────────
     AUC WINNER BOX
  ───────────────────────────────────── */
  .auc-winner {
    background: var(--blue-bg);
    border-left: 4px solid var(--blue);
    border-radius: 0 8px 8px 0;
    padding: 13px 20px;
    margin-top: 18px;
    font-size: 15px; font-weight: 700;
    color: var(--navy);
  }
  .auc-winner em { color: var(--blue); font-style: normal; }

  /* ─────────────────────────────────────
     CONCLUSION
  ───────────────────────────────────── */
  section.conclusion {
    background: var(--navy);
    overflow: hidden; position: relative;
  }
  section.conclusion::before {
    content: '';
    position: absolute;
    top: -120px; right: -120px;
    width: 440px; height: 440px;
    border-radius: 50%;
    background: rgba(26,115,232,.13);
    pointer-events: none;
  }
  .concl-wrap { padding: 52px 80px 0; }
  .concl-eyebrow {
    font-size: 12px; font-weight: 700;
    color: var(--blue-lt); letter-spacing: 4px;
    margin-bottom: 16px;
  }
  .concl-item {
    display: flex; align-items: flex-start; gap: 22px;
    padding: 16px 0;
    border-bottom: 1px solid rgba(255,255,255,.1);
  }
  .concl-item:last-child { border-bottom: none; }
  .concl-num {
    font-size: 28px; font-weight: 900;
    color: var(--blue-lt); font-family: var(--mono);
    min-width: 44px; line-height: 1;
  }
  .concl-text { font-size: 16px; color: rgba(255,255,255,.9); line-height: 1.65; padding-top: 3px; }
  .concl-text strong { color: #fff; }
  .qa-bar {
    background: var(--blue);
    padding: 20px 80px;
    font-size: 23px; font-weight: 700;
    color: #fff; text-align: center;
    margin-top: 16px;
  }

---

<!-- _class: title -->
<!-- _paginate: false -->

<div class="t-tag">🛒 E-Commerce Churn Solution</div>
<div class="t-bar"></div>

# 고객 이탈 예측 플랫폼 <span>Re:tain</span>

<p class="sub">데이터 기반 선제적 고객 유지로 이커머스의 미래를 만듭니다</p>

<div class="t-meta">
  💠 SKN27 2차 프로젝트 | 4팀
  <span>|</span>
  김민경 · 박준희 · 박창제 · 임예은 · 한재웅
  <span>|</span>
  2026. 04. 02
</div>

---

<div class="hdr"><span class="num">AGENDA</span> 목차</div>

<div class="body">
<div class="agenda-grid">
  <div class="agenda-card">
    <div class="agenda-num">01</div>
    <div class="agenda-text"><h3>프로젝트 개요</h3><p>배경 · 문제 정의 · 팀 구성</p></div>
  </div>
  <div class="agenda-card">
    <div class="agenda-num">02</div>
    <div class="agenda-text"><h3>WBS & 일정</h3><p>작업 단계 · 역할 분담</p></div>
  </div>
  <div class="agenda-card">
    <div class="agenda-num">03</div>
    <div class="agenda-text"><h3>데이터 & 전처리</h3><p>결측치 처리 · 이상치 제어 · EDA</p></div>
  </div>
  <div class="agenda-card">
    <div class="agenda-num">04</div>
    <div class="agenda-text"><h3>피처 엔지니어링</h3><p>10개 파생 변수 설계 · 최종 24개 피처</p></div>
  </div>
  <div class="agenda-card">
    <div class="agenda-num">05</div>
    <div class="agenda-text"><h3>모델링 & 성능 비교</h3><p>RF · XGBoost · LightGBM · MLP</p></div>
  </div>
  <div class="agenda-card">
    <div class="agenda-num">06</div>
    <div class="agenda-text"><h3>서비스 & 기대 효과</h3><p>Re:tain 플랫폼 · Streamlit · 결론</p></div>
  </div>
</div>
</div>

---

<div class="hdr"><span class="num">01</span> 프로젝트 개요 — 문제 정의</div>

<div class="body">
<div class="two-col" style="height:100%;">

<div>
  <p style="font-size:14px;color:var(--gray);line-height:1.7;margin-bottom:16px;">
    이커머스 시장의 플랫폼 간 경쟁이 심화되면서<br>
    <strong style="color:var(--navy);">고객 이탈(Churn)</strong>은 매출에 직결되는 핵심 과제가 되었습니다.
  </p>
  <div class="prob-row">
    <div class="prob-icon">🔍</div>
    <div>
      <div class="prob-title">사전 식별 불가</div>
      <div class="prob-desc">이탈 징후를 미리 파악하기 어려워 대응 시점을 놓침</div>
    </div>
  </div>
  <div class="prob-row">
    <div class="prob-icon">📦</div>
    <div>
      <div class="prob-title">데이터 활용 부재</div>
      <div class="prob-desc">데이터는 축적되어 있으나 실질적 의사결정으로 연결되지 않음</div>
    </div>
  </div>
  <div class="prob-row">
    <div class="prob-icon">📉</div>
    <div>
      <div class="prob-title">충성도 하락</div>
      <div class="prob-desc">가격·혜택 중심 경쟁으로 고객 Lock-in 약화</div>
    </div>
  </div>
  <div class="prob-row">
    <div class="prob-icon">💸</div>
    <div>
      <div class="prob-title">사후적 대응의 한계</div>
      <div class="prob-desc">이탈 후 대응은 LTV 감소 & 마케팅 비용 증가로 이어짐</div>
    </div>
  </div>
</div>

<div>
  <p style="font-size:15px;font-weight:700;color:var(--navy);margin-bottom:14px;">🎯 프로젝트 목적</p>
  <p style="font-size:13.5px;color:var(--gray);margin-bottom:18px;line-height:1.7;">
    <strong style="color:var(--navy);">머신러닝 기반 이탈 예측 모델</strong>로<br>선제적 고객 관리 체계를 구축합니다.
  </p>
  <div class="obj-item">
    <div class="obj-dot"></div>
    <div class="obj-label">모델 비교</div>
    <div class="obj-desc">RF / XGBoost / LightGBM / MLP 4종 평가</div>
  </div>
  <div class="obj-item">
    <div class="obj-dot"></div>
    <div class="obj-label">피처 설계</div>
    <div class="obj-desc">파생 변수 10개로 이탈 패턴 정밀 포착</div>
  </div>
  <div class="obj-item">
    <div class="obj-dot"></div>
    <div class="obj-label">플랫폼 구현</div>
    <div class="obj-desc">Re:tain 대시보드로 실시간 이탈 예측 제공</div>
  </div>
  <div class="banner" style="margin-top:16px;">
    💡 <strong>"고객이 떠난 이후 대응"</strong>이 아니라 <strong>"떠나기 전에 미리 대응"</strong>
  </div>
</div>

</div>
</div>

---

<div class="hdr"><span class="num">01</span> 팀 구성</div>

<div class="body" style="display:flex;flex-direction:column;justify-content:center;">
<div class="four-col" style="grid-template-columns:repeat(5,1fr);">

  <div class="member-card">
    <div class="member-avatar">👩</div>
    <div class="member-name">김민경</div>
    <div class="member-role">팀장<br>Feature Engineering<br>MLP 모델링<br>DB 연결 · 최종 점검</div>
  </div>

  <div class="member-card">
    <div class="member-avatar">👨</div>
    <div class="member-name">박준희</div>
    <div class="member-role">데이터 전처리<br>(결측치)<br>Random Forest<br>모델링</div>
  </div>

  <div class="member-card">
    <div class="member-avatar">👨</div>
    <div class="member-name">박창제</div>
    <div class="member-role">데이터 전처리<br>(결측치)<br>XGBoost 모델링<br>이탈 예측 UI 연결</div>
  </div>

  <div class="member-card">
    <div class="member-avatar">👨</div>
    <div class="member-name">한재웅</div>
    <div class="member-role">데이터 전처리<br>(이상치)<br>LightGBM<br>모델링</div>
  </div>

  <div class="member-card">
    <div class="member-avatar">👩</div>
    <div class="member-name">임예은</div>
    <div class="member-role">소비 트렌드<br>데이터 수집<br>Streamlit<br>개발</div>
  </div>

</div>
</div>

---

<div class="hdr"><span class="num">02</span> WBS — 작업 일정</div>

<div class="body" style="display:flex;flex-direction:column;justify-content:center;">

  <div class="wbs-item">
    <div class="wbs-period">3/26 ~ 3/27</div>
    <div class="wbs-step">분석 및 설계</div>
    <div class="wbs-tasks">환경 세팅 · 데이터 이해 · 기획서 작성 · 역할 분담</div>
  </div>

  <div class="wbs-item">
    <div class="wbs-period">3/27 ~ 3/31</div>
    <div class="wbs-step">전처리 & 모델링</div>
    <div class="wbs-tasks">결측치 / 이상치 처리 · Feature Engineering · 4개 모델 학습 및 성능 비교</div>
  </div>

  <div class="wbs-item">
    <div class="wbs-period">3/30 ~ 4/1</div>
    <div class="wbs-step">서비스 개발</div>
    <div class="wbs-tasks">Streamlit 3페이지 구현 · PostgreSQL DB 연결 · UI 통합 테스트</div>
  </div>

  <div class="wbs-item">
    <div class="wbs-period">4/2</div>
    <div class="wbs-step">발표 준비</div>
    <div class="wbs-tasks">PPT 작성 · 최종 시연 준비 · 발표 리허설</div>
  </div>

</div>

---

<div class="hdr"><span class="num">03</span> 데이터 개요</div>

<div class="body">
<div class="four-col" style="margin-bottom:18px;">
  <div class="stat-card"><div class="stat-val">5,630</div><div class="stat-lbl">전체 데이터 건수</div></div>
  <div class="stat-card"><div class="stat-val">20개</div><div class="stat-lbl">원본 피처 수</div></div>
  <div class="stat-card"><div class="stat-val">16.9%</div><div class="stat-lbl">이탈 고객 비율 (Churn=1)</div></div>
  <div class="stat-card"><div class="stat-val">80/20</div><div class="stat-lbl">Train / Test 분할</div></div>
</div>

<div class="two-col">
  <div class="card">
    <div class="card-hd">📊 E-commerce 고객 이탈 데이터</div>
    <div class="card-bd">
      <table>
        <thead><tr><th>카테고리</th><th>주요 피처</th></tr></thead>
        <tbody>
          <tr><td>구매 행동</td><td><code>OrderCount</code>, <code>DaySinceLastOrder</code></td></tr>
          <tr><td>혜택</td><td><code>CouponUsed</code>, <code>CashbackAmount</code></td></tr>
          <tr><td>고객 경험</td><td><code>SatisfactionScore</code>, <code>Complain</code></td></tr>
          <tr><td>기타</td><td><code>Tenure</code>, <code>NumberOfDeviceRegistered</code></td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="card">
    <div class="card-hd blue">📈 한국 소비 트렌드 데이터 (공공)</div>
    <div class="card-bd">
      <table>
        <thead><tr><th>출처</th><th>데이터</th></tr></thead>
        <tbody>
          <tr><td>통계청</td><td>소비 지출 데이터</td></tr>
          <tr><td>통계청</td><td>온라인 쇼핑 거래액</td></tr>
          <tr><td>소비자동향조사</td><td>소비자 심리지수</td></tr>
        </tbody>
      </table>
      <div class="banner">Churn = 1 → 이탈 고객 &nbsp;/&nbsp; Churn = 0 → 유지 고객</div>
    </div>
  </div>
</div>
</div>

---

<div class="hdr"><span class="num">03</span> 데이터 전처리</div>

<div class="body">
<div class="two-col" style="height:100%;">

  <div class="card">
    <div class="card-hd">💊 결측치 처리 — 그룹별 중앙값 대체</div>
    <div class="card-bd">
      <table>
        <thead><tr><th>피처</th><th>결측률</th><th>처리 방법</th></tr></thead>
        <tbody>
          <tr><td><code>Tenure</code></td><td>4.7%</td><td>NumberOfAddress 그룹 중앙값</td></tr>
          <tr><td><code>DaySinceLastOrder</code></td><td>5.5%</td><td>카테고리×로그인기기 중앙값</td></tr>
          <tr><td><code>OrderCount</code></td><td>4.7%</td><td>카테고리×결제수단 중앙값</td></tr>
          <tr><td><code>OrderAmountHike</code></td><td>4.6%</td><td>카테고리 그룹 중앙값</td></tr>
          <tr><td><code>HourSpendOnApp</code></td><td>4.4%</td><td>전체 중앙값</td></tr>
          <tr><td><code>CouponUsed</code></td><td>4.6%</td><td>전체 중앙값</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-hd blue">📐 이상치 처리 — 분포 기반 차별 적용</div>
    <div class="card-bd">
      <table>
        <thead><tr><th>피처</th><th>처리 방식</th><th>변환 피처명</th></tr></thead>
        <tbody>
          <tr><td><code>Tenure</code></td><td>로그 변환 (log1p)</td><td><code>Tenure_log</code></td></tr>
          <tr><td><code>WarehouseToHome</code></td><td>로그 변환 (log1p)</td><td><code>WH_log</code></td></tr>
          <tr><td><code>DaySinceLastOrder</code></td><td>IQR 클리핑</td><td><code>Days_clip</code></td></tr>
          <tr><td><code>CashbackAmount</code></td><td>IQR 클리핑</td><td><code>Cashback_clip</code></td></tr>
        </tbody>
      </table>
      <div class="banner">💡 우편향 분포 → 로그 정규화 &nbsp;/&nbsp; 극단값 → IQR 억제</div>
    </div>
  </div>

</div>
</div>

---

<div class="hdr"><span class="num">04</span> 피처 엔지니어링</div>

<div class="body">
<p style="font-size:13.5px;color:var(--gray);margin-bottom:14px;">EDA 기반 이탈 예측력 강화 — 총 <strong style="color:var(--navy);">10개 파생 변수</strong> 설계</p>

<div class="three-col">
  <div class="feat-group">
    <h3>🏃 행동 패턴 (4개)</h3>
    <ul>
      <li><strong>Dormancy Shock</strong>: 평소 대비 주문 공백의 충격 지수</li>
      <li><strong>Recency Tenure Ratio</strong>: 가입기간 대비 최근 공백 비중</li>
      <li><strong>MonthlyOrderFreq</strong>: 월평균 주문 빈도</li>
      <li><strong>Stagnant Loyal</strong>: 가입은 오래됐지만 활동 평균 이하</li>
    </ul>
  </div>
  <div class="feat-group muted">
    <h3>⭐ 만족도 & 경험 (3개)</h3>
    <ul>
      <li><strong>Satisfaction_Per_Order</strong>: 주문당 만족도 효율</li>
      <li><strong>Silent Killer</strong>: 불만 낮지만 만족도도 낮은 잠재 이탈자</li>
      <li><strong>IssueIndex</strong>: 불만 제기 여부 (명시적 부정 경험)</li>
    </ul>
  </div>
  <div class="feat-group dark">
    <h3>💰 가치 & 반응성 (3개)</h3>
    <ul>
      <li><strong>CashbackPerOrder</strong>: 주문당 캐시백 체감도</li>
      <li><strong>Promo_Sensitivity</strong>: 프로모션 민감도</li>
      <li><strong>ManyAddressesFlag</strong>: 헤비 유저 여부 (배송지 다수)</li>
    </ul>
  </div>
</div>

<div class="banner">
  <strong>최종 처리</strong> &nbsp;|&nbsp; 카테고리 피처 원-핫 인코딩 → 불필요 컬럼 제거 → 최종 <strong>24개 피처</strong>로 모델 학습
</div>
</div>

---

<div class="hdr"><span class="num">05</span> 모델링 — 4종 비교</div>

<div class="body">
<table>
  <thead>
    <tr><th>모델</th><th>담당</th><th>특장점</th><th>튜닝 기법</th><th>주요 파라미터</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>🌲 Random Forest</td><td>박준희</td><td>비선형 학습, 안정적</td>
      <td>Manual Search CV</td>
      <td><code>n_estimators=100</code> &nbsp;<code>max_depth=12</code></td>
    </tr>
    <tr>
      <td>⭐ XGBoost</td><td>박창제</td><td>최고 정확도, 정규화</td>
      <td>Grid Search CV</td>
      <td><code>lr=0.1</code> &nbsp;<code>max_depth=5</code> &nbsp;<code>n_est=300</code></td>
    </tr>
    <tr>
      <td>🚀 LightGBM</td><td>한재웅</td><td>빠른 학습, 메모리 효율</td>
      <td>Bayesian (Optuna)</td>
      <td><code>lr=0.0811</code> &nbsp;<code>n_est=460</code> &nbsp;<code>depth=5</code></td>
    </tr>
    <tr>
      <td>🧠 MLP</td><td>김민경</td><td>배포 용이, 실시간 추론</td>
      <td>Standard Scaler + Grid CV</td>
      <td><code>hidden=(50,50)</code> &nbsp;<code>alpha=0.0001</code></td>
    </tr>
  </tbody>
</table>
</div>

---

<div class="hdr"><span class="num">05</span> 모델 성능 비교 — AUC</div>

<div class="body" style="display:flex;flex-direction:column;justify-content:center;">

  <div class="auc-item">
    <div class="auc-label">⭐ XGBoost</div>
    <div class="auc-track"><div class="auc-fill xgb"></div></div>
    <div class="auc-score">0.995</div>
  </div>
  <div class="auc-item">
    <div class="auc-label">🚀 LightGBM</div>
    <div class="auc-track"><div class="auc-fill lgbm"></div></div>
    <div class="auc-score">0.976</div>
  </div>
  <div class="auc-item">
    <div class="auc-label">🧠 MLP</div>
    <div class="auc-track"><div class="auc-fill mlp"></div></div>
    <div class="auc-score">0.969</div>
  </div>
  <div class="auc-item">
    <div class="auc-label">🌲 Random Forest</div>
    <div class="auc-track"><div class="auc-fill rf"></div></div>
    <div class="auc-score">0.900</div>
  </div>

  <div class="auc-winner">
    ✓ 최종 선택: <em>XGBoost</em> &nbsp;|&nbsp; AUC <em>0.995</em> &nbsp;|&nbsp;
    불균형 데이터(16.9% 이탈)에서도 안정적 · SHAP 해석 가능 · Streamlit 배포 용이
  </div>

</div>

---

<div class="hdr"><span class="num">05</span> 혼동 행렬 (Confusion Matrix) 비교</div>

<div class="body">
<div class="cm-grid">
  <div class="cm-box">
    <img src="./images/output4.png">
    <p>Random Forest</p>
  </div>
  <div class="cm-box">
    <img src="./images/MLP_output.png">
    <p>MLP</p>
  </div>
  <div class="cm-box">
    <img src="./images/output.png">
    <p>LightGBM</p>
  </div>
  <div class="cm-box">
    <img src="./images/output3.png">
    <p>XGBoost ⭐ Best</p>
  </div>
</div>
</div>

---

<div class="hdr"><span class="num">06</span> 서비스 구성 — Re:tain 플랫폼</div>

<div class="body">
<div class="three-col" style="margin-bottom:16px;">
  <div class="page-card">
    <div class="page-card-hd c1">📊 Churn Dashboard</div>
    <div class="page-card-bd">
      고객별 <strong>이탈 확률 예측</strong><br>
      위험군 분류 (High / Medium / Low)<br>
      실시간 예측 결과 시각화
    </div>
  </div>
  <div class="page-card">
    <div class="page-card-hd c2">🔍 Behavior Analysis</div>
    <div class="page-card-bd">
      <strong>RFM 세그먼트</strong> 분석<br>
      구매 패턴 · 쿠폰 사용 트렌드<br>
      만족도 영향 분석
    </div>
  </div>
  <div class="page-card">
    <div class="page-card-hd c3">📈 Consumer Trends</div>
    <div class="page-card-bd">
      <strong>한국 소비 트렌드</strong> 시각화<br>
      통계청 공공데이터 기반<br>
      경제적 맥락과 이탈 원인 해석
    </div>
  </div>
</div>

<div class="banner">
  🏗️ <strong>Streamlit</strong> (Frontend) &nbsp;+&nbsp; <strong>XGBoost</strong> (Prediction) &nbsp;+&nbsp; <strong>PostgreSQL + Docker</strong> (Data) &nbsp;+&nbsp; <strong>SHAP</strong> (Explainability)
</div>
</div>

---

<div class="hdr"><span class="num">06</span> 기대 효과</div>

<div class="body" style="display:flex;flex-direction:column;justify-content:center;">
<div class="four-col">
  <div class="effect-card">
    <div class="effect-icon">🎯</div>
    <div class="effect-title">고객 이탈률 감소</div>
    <div class="effect-desc">사전 예측으로<br>이탈 징후 선제 대응</div>
  </div>
  <div class="effect-card">
    <div class="effect-icon">💰</div>
    <div class="effect-title">LTV 향상</div>
    <div class="effect-desc">맞춤 유지 전략으로<br>고객 생애 가치 증가</div>
  </div>
  <div class="effect-card">
    <div class="effect-icon">📣</div>
    <div class="effect-title">마케팅 효율화</div>
    <div class="effect-desc">타겟 마케팅으로<br>비용 최적화</div>
  </div>
  <div class="effect-card">
    <div class="effect-icon">🏆</div>
    <div class="effect-title">플랫폼 경쟁력</div>
    <div class="effect-desc">데이터 기반 의사결정으로<br>경쟁력 강화</div>
  </div>
</div>
<div class="banner" style="margin-top:20px;">
  신규 고객 유치 비용 ≒ 유지 비용의 <strong>5~7배</strong> &nbsp;—&nbsp; Re:tain은 유지 비용 최소화로 ROI를 극대화합니다
</div>
</div>

---

<!-- _class: conclusion -->
<!-- _paginate: false -->

<div class="concl-wrap">
<div class="concl-eyebrow">CONCLUSION · 결론</div>

<div class="concl-item">
  <div class="concl-num">01</div>
  <div class="concl-text"><strong>이탈 예측 정확도 극대화</strong> — XGBoost AUC 0.995로 실용적 수준의 예측 달성</div>
</div>
<div class="concl-item">
  <div class="concl-num">02</div>
  <div class="concl-text"><strong>파생 변수의 중요성 입증</strong> — 행동·만족도·가치 기반 10개 피처가 모델 성능 향상에 핵심 기여</div>
</div>
<div class="concl-item">
  <div class="concl-num">03</div>
  <div class="concl-text"><strong>Re:tain 플랫폼 구현</strong> — Streamlit 기반 3페이지 대시보드로 현업 활용 가능한 의사결정 지원 시스템 완성</div>
</div>

</div>

<div class="qa-bar">
  "데이터로 고객의 마음을 붙잡다" &nbsp;|&nbsp; Q &amp; A
</div>
