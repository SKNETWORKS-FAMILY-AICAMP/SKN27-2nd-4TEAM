import streamlit as st
import sys
from pathlib import Path

# 1. 페이지 설정
st.set_page_config(
    page_title="Re:tain - AI 이탈 예측 플랫폼",
    page_icon="💠",
    layout="wide",
)

# 2. React 스타일 완벽 재현을 위한 고도화된 CSS
st.markdown("""
    <style>
    /* 폰트 및 배경 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .stApp {
        background-color: #F7F9FC;
        font-family: 'Inter', sans-serif;
    }

    /* Streamlit 기본 UI 요소 제거 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important;}

    /* Header */
    .nav-bar {
        background: white;
        border-bottom: 1px solid #E2E8F0;
        padding: 0.8rem 4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 999;
    }

    .nav-link {
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        color: #4A6FA5;
        transition: color 0.2s;
    }
    .nav-link:hover { color: #3A5A8C; }

    /* Hero Section */
    .hero-section {
        padding: 100px 20px 40px 20px;
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        background: #EEF2F8;
        color: #4A6FA5;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid rgba(74, 111, 165, 0.15);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 3.8rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        line-height: 1.1;
        margin-bottom: 1.5rem;
    }

    .hero-desc {
        font-size: 1.15rem;
        color: #64748B;
        line-height: 1.6;
        margin-bottom: 3rem;
    }

    /* Stats Row */
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 60px;
        margin-top: 10px;
        padding-bottom: 60px;
    }
    .stat-box { text-align: center; }
    .stat-value { font-size: 1.8rem; font-weight: 800; color: #0F172A; }
    .stat-label { font-size: 0.85rem; color: #94A3B8; margin-top: 4px; }

    /* Features Grid */
    .features-section-title {
        text-align: center; 
        font-size: 1.7rem; 
        font-weight: 800; 
        color:#0F172A; 
        margin-top: 4rem;
        margin-bottom: 3rem;
    }

    .feature-card {
        background: white;
        padding: 32px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
    }

    /* CTA Banner Wrapper */
    .cta-wrapper {
        max-width: 1100px;
        margin: 4rem auto 6rem auto;
        padding: 0 2rem;
    }
    .cta-banner {
        background: linear-gradient(135deg, #3A5A8C 0%, #4A6FA5 60%, #5E85BF 100%);
        padding: 50px 60px;
        border-radius: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        box-shadow: 0 10px 30px rgba(74, 111, 165, 0.2);
    }

    /* Streamlit Button Overrides */
    div.stButton > button {
        background-color: #4A6FA5 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.7rem 2.2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.2s !important;
    }
    div.stButton > button:hover {
        background-color: #3A5A8C !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }
    
    /* 배너 안의 버튼 전용 스타일 */
    .cta-banner div.stButton > button {
        background-color: white !important;
        color: #4A6FA5 !important;
    }

    /* Column 정렬 */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
            
            /* 버튼을 감싸는 컨테이너를 중앙 정렬 */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 1rem;
        margin-left: 40%;
    }

    /* 버튼 자체의 크기 및 스타일 확장 */
    div.stButton > button {
        background-color: #4A6FA5 !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important; /* 더 부드러운 곡선 */
        
        /* 크기 조절 키포인트 */
        padding: 1rem 3.5rem !important; /* 상하좌우 여백 대폭 확대 */
        font-size: 1.15rem !important;   /* 글자 크기 확대 */
        font-weight: 700 !important;
        
        min-width: 280px; /* 최소 너비 지정으로 볼륨감 확보 */
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 15px -3px rgba(74, 111, 165, 0.3) !important; /* 그림자 강조 */
    }

    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        background-color: #3A5A8C !important;
        box-shadow: 0 20px 25px -5px rgba(74, 111, 165, 0.4) !important;
    }
            
            
    </style>
""", unsafe_allow_html=True)

def main():
    # --- 1. Custom Header ---
    st.markdown(f"""
        <div class="nav-bar">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="background:#4A6FA5; color:white; width:34px; height:34px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:bold;">💠</div>
                <span style="font-size: 1.3rem; font-weight: 800; color: #0F172A;">Re:tain</span>
                <span style="font-size: 0.7rem; background:#EEF2F8; color:#4A6FA5; padding:2px 8px; border-radius:99px; font-weight:700;">BETA</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- 2. Hero Section ---
    st.markdown("""
        <div class="hero-section">
            <div class="hero-badge">
                <span style="width:6px; height:6px; background:#4A6FA5; border-radius:50%; margin-right:8px;"></span>
                데이터 기반 고객 이탈 예측 플랫폼
            </div>
            <h1 class="hero-title">고객이 떠나기 전에,<br><span style="color:#4A6FA5;">데이터가 먼저 알립니다.</span></h1>
            <p class="hero-desc">
                구매 데이터를 기반으로 이탈 가능성을 예측하고,<br>
                행동 패턴을 분석하여 맞춤형 유지 전략을 제공합니다.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Hero CTA Button
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        if st.button("대시보드 시작하기 ➔", key="hero_btn"):
            try:
                st.switch_page("pages/01_Churn_Dashboard.py")
            except Exception as e:
                st.error("대시보드 파일을 찾을 수 없습니다. (pages/01_Churn_Dashboard.py 확인)")

    # Stats Row
    st.markdown("""
        <div class="stats-container">
            <div class="stat-box"><div class="stat-value">2,540+</div><div class="stat-label">분석 고객 수</div></div>
            <div class="stat-box"><div class="stat-value">91%</div><div class="stat-label">이탈 예측 정확도</div></div>
            <div class="stat-box"><div class="stat-value">+34%</div><div class="stat-label">평균 리텐션 향상</div></div>
        </div>
    """, unsafe_allow_html=True)

    # --- 3. Features Section ---
    st.markdown('<div class="features-section-title">핵심 기능</div>', unsafe_allow_html=True)
    
    f_cols = st.columns([1, 1, 1])
    features = [
        {"icon": "🛡️", "title": "고객 이탈 예측", "desc": "구매 패턴 데이터를 분석해 이탈 위험 고객을 사전에 식별합니다.", "bg": "#EEF2F8"},
        {"icon": "📊", "title": "행동 분석", "desc": "RFM 세그멘테이션과 구매 주기 분석으로 고객 행동을 정밀 파악합니다.", "bg": "#EEF6EE"},
        {"icon": "📢", "title": "마케팅 전략 추천", "desc": "세그먼트별 맞춤 쿠폰, 리텐션 캠페인 전략을 자동 추천합니다.", "bg": "#F9EEEE"},
    ]

    for i, col in enumerate(f_cols):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <div style="background-color: {features[i]['bg']}; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 1.4rem;">
                        {features[i]['icon']}
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 700; color:#1E293B; margin-bottom: 0.75rem;">{features[i]['title']}</h3>
                    <p style="font-size: 0.95rem; color: #64748B; line-height: 1.6; word-break: keep-all;">{features[i]['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

    # --- 4. CTA Banner ---
    st.markdown("""
        <div class="cta-wrapper">
            <div class="cta-banner">
                <div>
                    <h3 style="color: white; font-weight: 800; margin: 0; font-size: 1.7rem; letter-spacing:-0.01em;">지금 바로 시작하세요</h3>
                    <p style="color: rgba(255,255,255,0.8); font-size: 1rem; margin-top: 8px;">고객 데이터를 연결하고 이탈 위험을 실시간으로 모니터링합니다.</p>
                </div>
    """, unsafe_allow_html=True)
    
    # 배너 내부 버튼 (Streamlit 위젯)
    if st.button("대시보드 시작하기 →", key="cta_banner_btn"):
        st.switch_page("pages/01_Churn_Dashboard.py")
        
    st.markdown("</div></div>", unsafe_allow_html=True)

    # --- 5. Footer ---
    st.markdown("""
        <div style="text-align: center; padding: 50px 0; border-top: 1px solid #E2E8F0; background: white; color: #94A3B8; font-size: 0.85rem;">
            © 2026 Re:tain. All rights reserved.
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()