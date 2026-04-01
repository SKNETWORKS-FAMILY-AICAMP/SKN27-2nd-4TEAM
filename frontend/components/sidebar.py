import streamlit as st

def render_sidebar(active_page="고객 이탈 관리"):
    st.markdown(f"""
        <style>
        /* 1. 외부 폰트 로드 */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* 2. 전역 및 사이드바 전용 폰트 설정 */
        :root {{
            --font-inter: 'Inter', sans-serif;
        }}

        /* 사이드바 내부의 모든 요소 및 메뉴 아이템에 Inter 폰트 강제 적용 */
        [data-testid="stSidebar"], 
        [data-testid="stSidebar"] *, 
        .stMarkdown, 
        .sb-menu-item {{
            font-family: var(--font-inter) !important;
        }}
                

        [data-testid="stSidebar"] {{
            background-color: #1E293B !important;
            border-right: none !important;
            width: 260px !important;
            min-width: 260px !important;
            max-width: 260px !important;
        }}
                
        /* 3. 사이드바 배경 및 기본 네비게이션 제거 */
        [data-testid="stSidebar"] {{
            background-color: #1E293B !important;
            border-right: none !important;
        }}
        [data-testid="stSidebarNav"] {{ display: none !important; }}
        [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}

        /* 4. 커스텀 메뉴 스타일 (SaaS 스타일 동기화) */
        .sb-menu-item {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 18px;
            border-radius: 10px;
            color: #F1F5F9 !important,
            font-size: 0.95rem;
            font-weight: 400;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }}
        
        /* 호버 시 효과 */
        .sb-menu-item:hover {{
            background-color: rgba(255, 255, 255, 0.05);
            color: #F1F5F9;
        }}

        /* 활성화된 메뉴 하이라이트 (Deep Blue) */
        .sb-active {{
            background-color: #4A6FA5 !important;
            color: white !important;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(74, 111, 165, 0.2);
        }}
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # 로고 영역
        st.markdown(f"""
            <div>
                <div style="display:flex; align-items:center; gap:10px; margin-top:-40px; margin-left:-5px">
                    <div style="background:#4A6FA5; width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center; color:white; font-size:18px;">💠</div>
                    <span style="font-size:1.4rem; font-weight:650; color:white; letter-spacing:-0.02em;">Re:tain</span>
                </div>
                <p style="font-size:0.85rem; color:#64748B; margin-top:8px; font-weight:500;">고객 이탈 예측 플랫폼</p>
            </div>
            
            <div style="color:#475569; font-size:0.8rem; font-weight:700; margin-left:5px; margin-top:40px; letter-spacing:0.05em; text-transform:uppercase;">대시보드</div>
            
            <a href="Churn_Dashboard" target="_self" class="sb-menu-item {'sb-active' if active_page == '고객 이탈 관리' else ''}">👤 고객 이탈 관리</a>
            <a href="Behavior_Analysis" target="_self" class="sb-menu-item {'sb-active' if active_page == '행동 분석' else ''}">📊 행동 분석</a>
            <a href="Consumer_Trends" target="_self" class="sb-menu-item {'sb-active' if active_page == '소비 트렌드' else ''}">📈 소비 트렌드</a>
            
            <div style="position: fixed; bottom: 20px; left: 20px; font-size: 0.7rem; color: #475569; font-weight: 500;">Re:tain v2.0</div>
        """, unsafe_allow_html=True)