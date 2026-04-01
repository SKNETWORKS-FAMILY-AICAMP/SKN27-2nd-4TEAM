import streamlit as st

def render_sidebar(active_page="행동 분석"):
    st.markdown(f"""
        <style>
        /* 1. 사이드바 배경색만 변경 (Streamlit 기본 레이아웃 유지 -> 겹침 절대 발생 안함) */
        [data-testid="stSidebar"] {{
            background-color: #1E293B !important;
            border-right: none !important;
        }}
        
        /* 2. 기본 네비게이션 숨김 */
        [data-testid="stSidebarNav"] {{ display: none !important; }}
        
        /* 3. 커스텀 메뉴 스타일 */
        .sb-menu-item {{
            display: flex; align-items: center; gap: 12px;
            padding: 12px 20px; margin: 4px 12px;
            border-radius: 10px; color: #94A3B8; font-size: 0.9rem;
            text-decoration: none !important; transition: all 0.2s;
        }}
        .sb-menu-item:hover {{ background-color: rgba(255,255,255,0.05); color: white; }}
        .sb-active {{ background-color: #4A6FA5 !important; color: white !important; font-weight: 600; }}
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 20px 0 30px 20px;">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="background:#4A6FA5; width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold;">💠</div>
                    <span style="font-size:1.2rem; font-weight:800; color:white;">Re:tain</span>
                </div>
                <p style="font-size:0.75rem; color:#64748B; margin-top:8px; margin-left:2px;">고객 이탈 예측 플랫폼</p>
            </div>
            <div style="color:#475569; font-size:0.7rem; font-weight:700; margin-left:20px; margin-bottom:10px;">대시보드</div>
            
            <a href="Churn_Dashboard" target="_self" class="sb-menu-item {'sb-active' if active_page == '고객 이탈 관리' else ''}">👤 고객 이탈 관리</a>
            <a href="Behavior_Analysis" target="_self" class="sb-menu-item {'sb-active' if active_page == '행동 분석' else ''}">📊 행동 분석</a>
            <a href="Consumer_Trends" target="_self" class="sb-menu-item {'sb-active' if active_page == '소비 트렌드' else ''}">📈 소비 트렌드</a>
            
        """, unsafe_allow_html=True)