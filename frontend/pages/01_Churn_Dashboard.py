import streamlit as st
from components.sidebar import render_sidebar

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Re:tain | 고객 이탈 관리", layout="wide", initial_sidebar_state="expanded")

# --- 2. 데이터 정의 및 세션 상태 초기화 ---
if "customers" not in st.session_state:
    st.session_state.customers = [
        {"id": "C001", "prob": 97, "label": "고위험", "dot": "🔥", "color": "#C0392B", "bg": "#FDEDEC", "segment": "At Risk", "day": "60일", "count": "1회", "amount": "$120", "gender": "남성", "cashback": "$0", "sat": 2},
        {"id": "C002", "prob": 85, "label": "위험",   "dot": "🔴", "color": "#D97A7A", "bg": "#FDEAEA", "segment": "At Risk", "day": "40일", "count": "3회", "amount": "$340", "gender": "여성", "cashback": "$12", "sat": 3},
        {"id": "C003", "prob": 72, "label": "주의",   "dot": "🟠", "color": "#E6C97A", "bg": "#FDF1E3", "segment": "Active",  "day": "20일", "count": "5회", "amount": "$780", "gender": "남성", "cashback": "$45", "sat": 3},
        {"id": "C004", "prob": 45, "label": "양호",   "dot": "🟡", "color": "#B8A838", "bg": "#FEF9E7", "segment": "Active",  "day": "10일", "count": "8회", "amount": "$560", "gender": "여성", "cashback": "$78", "sat": 4},
        {"id": "C005", "prob": 15, "label": "안전",   "dot": "🟢", "color": "#5FAD56", "bg": "#EEF6EE", "segment": "VIP",     "day": "3일",  "count": "15회", "amount": "$2,400", "gender": "남성", "cashback": "$210", "sat": 5},
    ]

# 개별 체크박스 상태
if "check_states" not in st.session_state:
    st.session_state.check_states = {c['id']: False for c in st.session_state.customers}
# 선택된 고객 ID (상세정보용)
if "selected_id" not in st.session_state:
    st.session_state.selected_id = "C001"

# --- 3. 이벤트 콜백 함수 (핵심 로직) ---
def update_all_checks(tab_name, display_ids):
    """전체 선택 체크박스를 클릭했을 때 실행되는 함수"""
    master_val = st.session_state[f"master_{tab_name}"]
    for cid in display_ids:
        st.session_state.check_states[cid] = master_val
        st.session_state[f"chk_{tab_name}_{cid}"] = master_val

def update_single_check(cid, tab_name):
    """개별 체크박스를 클릭했을 때 실행되는 함수"""
    st.session_state.check_states[cid] = st.session_state[f"chk_{tab_name}_{cid}"]

def set_selected_customer(cid):
    """고객 ID 버튼을 클릭했을 때 상세정보를 업데이트하는 함수"""
    st.session_state.selected_id = cid

# --- 4. 사이드바 호출 ---
render_sidebar("고객 이탈 관리")

# --- 5. CSS 스타일링 ---
st.markdown("""
    <style>
    /* 1. 외부 폰트 로드 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* 2. Tailwind 변수 정의 */
    :root {
        --font-inter: 'Inter', sans-serif;
    }

    /* 3. 전체 앱에 폰트 적용 */
    .stApp, [data-testid="stSidebar"], .stMarkdown {
        font-family: var(--font-inter) !important;
    }

    /* 4. 기존 스타일 유지 */
    .react-card-container {
        font-family: var(--font-inter);
        background: white;
        /* ... 기존 스타일 ... */
    }
    
    /* 제목이나 굵은 글씨에도 확실히 적용 */
    h1, h2, h3, b, strong {
        font-family: var(--font-inter) !important;
        font-weight: 700;
    }   
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .main .block-container { padding-top: 2rem !important; padding-left: 280px !important; padding-right: 40px !important; max-width: 1500px !important; }
    
            
    /* 1. 사이드바 접기/펴기 버튼(화살표)을 아예 삭제하여 고정 효과 */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* 2. 사이드바가 항상 일정 너비를 유지하도록 설정 (선택 사항) */
    [data-testid="stSidebar"] {
        min-width: 260px !important;
        max-width: 260px !important;
    }
    /* 상단 KPI 디자인 */
    .kpi-card { background: white; padding: 24px; border-radius: 16px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    .kpi-val { font-size: 28px; font-weight: 800; color: #1E293B; margin-top: 10px; margin-bottom: 2px; }
    
    /* 확률 바 및 배지 */
    .p-bar-bg { background: #F1F5F9; height: 6px; border-radius: 10px; width: 50px; display: inline-block; margin-right: 10px; overflow: hidden; }
    .p-bar-fill { height: 100%; border-radius: 10px; }
    .badge { padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; }
    
    /* 상세 정보 라인 */
    .detail-item { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #F1F5F9; font-size: 13px; color: #475569; }
    </style>
""", unsafe_allow_html=True)

# --- 6. 화면 렌더링 ---
st.markdown('<h1 style="font-size: 24px; font-weight: 800; color: #1E293B; margin-bottom: 4px;">고객 이탈 관리</h1>', unsafe_allow_html=True)
st.markdown("<p style='color: #64748B; font-size: 14px; margin-bottom: 25px;'>이탈 위험 고객을 분류하고 캠페인을 실행하세요</p>", unsafe_allow_html=True)

# [상단 KPI 영역]
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="kpi-card"><div style="background:#EEF2F8; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">👥</div><div class="kpi-val">2,540</div><div style="font-size:13px; font-weight:600; color:#334155;">전체 고객 수</div><div style="font-size:12px; color:#94A3B8;">등록 고객 전체</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="kpi-card"><div style="background:#FDEAEA; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">⚠️</div><div class="kpi-val" style="color:#D97A7A;">312</div><div style="font-size:13px; font-weight:600; color:#334155;">이탈 위험 고객</div><div style="font-size:12px; color:#94A3B8;">위험 + 고위험 합산</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="kpi-card"><div style="background:#FDF1E3; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">📉</div><div class="kpi-val" style="color:#E6A050;">42%</div><div style="font-size:13px; font-weight:600; color:#334155;">평균 이탈 확률</div><div style="font-size:12px; color:#94A3B8;">전체 고객 평균</div></div>', unsafe_allow_html=True)

st.write("")

# [하단 메인 분할]
m_left, m_right = st.columns([2.6, 1])
selected_count = sum(st.session_state.check_states.values())


with m_left:
    with st.container(border=True):
        st.markdown(f"<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;'><b style='font-size:16px;'>고객 리스트</b><span style='font-size:12px; color:#94A3B8;'>{len(st.session_state.customers)}명 표시 · <b style='color:#3B82F6;'>{selected_count}명 선택됨</b></span></div>", unsafe_allow_html=True)
        
        tab_titles = ["전체", "안전", "양호", "주의", "위험", "고위험"]
        tabs = st.tabs(tab_titles)
        
        for idx, tab in enumerate(tabs):
            with tab:
                curr_tab_name = tab_titles[idx]
                
                # 데이터 필터링
                if curr_tab_name == "전체":
                    display_list = st.session_state.customers
                else:
                    display_list = [c for c in st.session_state.customers if c['label'] == curr_tab_name]
                
                if not display_list:
                    st.info(f"'{curr_tab_name}' 등급의 고객이 없습니다.")
                    continue
                
                display_ids = [c['id'] for c in display_list]
                
                # 🚨 [전체 선택 상태 동기화] 개별 클릭으로 모두 체크되면 전체선택 박스도 자동으로 체크되도록 처리
                all_checked = all(st.session_state.check_states[cid] for cid in display_ids)
                st.session_state[f"master_{curr_tab_name}"] = all_checked
                
                st.write("")
                # --- 리스트 헤더 ---
                h1, h2, h3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                with h1:
                    st.checkbox("전체", key=f"master_{curr_tab_name}", on_change=update_all_checks, args=(curr_tab_name, display_ids), label_visibility="collapsed")
                with h2:
                    st.markdown('<span style="color:#94A3B8; font-size:12px; font-weight:600;">고객 ID</span>', unsafe_allow_html=True)
                with h3:
                    st.markdown("""
                        <div style="display:flex; color:#94A3B8; font-size:12px; font-weight:600; padding-left:15px;">
                            <div style="flex:1.5;">이탈 확률</div>
                            <div style="flex:1.5;">위험도</div>
                            <div style="flex:1.5;">세그먼트</div>
                            <div style="flex:1.2;">경과일</div>
                            <div style="flex:1;">주문수</div>
                            <div style="flex:1.5; text-align:right;">금액</div>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("<hr style='margin: 5px 0 10px 0;'>", unsafe_allow_html=True)

                # --- 리스트 바디 ---
                for c in display_list:
                    # 1. 개별 체크박스용 고유 키 생성
                    chk_key = f"chk_{curr_tab_name}_{c['id']}"
                    
                    # 🚨 [핵심 수정 부분] if문을 지워서 화면이 렌더링될 때마다 무조건 마스터 상태를 복사해오게 만듭니다!
                    st.session_state[chk_key] = st.session_state.check_states[c['id']]
                    
                    # 3. 현재 체크 상태 확인 (배경색 변경용)
                    is_chk = st.session_state[chk_key]
                    bg_color = "#F0F7FF" if is_chk else "#FFFFFF"
                    
                    r1, r2, r3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                    
                    with r1:
                        # 🚨 value 인자 제거 (이중 설정 에러 완벽 차단)
                        st.checkbox(
                            "개별", 
                            key=chk_key, 
                            on_change=update_single_check, 
                            args=(c['id'], curr_tab_name), 
                            label_visibility="collapsed"
                        )
                    
                    with r2:
                        # 🚨 ID 버튼 클릭 시 즉시 상세정보 연동
                        st.button(
                            c['id'], 
                            key=f"btn_{curr_tab_name}_{c['id']}", 
                            on_click=set_selected_customer, 
                            args=(c['id'],), 
                            use_container_width=True
                        )
                    
                    with r3:
                        # 하이라이트가 적용된 데이터 블록
                        st.markdown(f"""
                            <div style="background-color:{bg_color}; border-radius:8px; padding:10px 15px; display:flex; align-items:center; transition:0.2s; border: 1px solid #F1F5F9;">
                                <div style="flex:1.5; display:flex; align-items:center;">
                                    <div class="p-bar-bg"><div class="p-bar-fill" style="background:{c['color']}; width:{c['prob']}%;"></div></div>
                                    <b style="color:{c['color']}; font-size:12px;">{c['prob']}%</b>
                                </div>
                                <div style="flex:1.5;"><span class="badge" style="background:{c['bg']}; color:{c['color']}">{c['dot']} {c['label']}</span></div>
                                <div style="flex:1.5;"><span class="badge" style="background:#F1F5F9; color:#475569">{c['segment']}</span></div>
                                <div style="flex:1.2; font-size:13px; color:#475569; font-weight:500;">{c['day']}</div>
                                <div style="flex:1; font-size:13px; color:#475569; font-weight:500;">{c['count']}</div>
                                <div style="flex:1.5; text-align:right; font-weight:800; font-size:14px; color:#1E293B;">{c['amount']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    st.write("") # 간격 띄우기


with m_right:
    # 👤 [우측 상단] 고객 상세 정보 (연동 완료)
    with st.container(border=True):
        st.markdown("<b style='font-size:15px; color:#1E293B;'>고객 상세 정보</b>", unsafe_allow_html=True)
        
        curr = next(c for c in st.session_state.customers if c['id'] == st.session_state.selected_id)
        st.markdown(f"""
            <div style="display:flex; align-items:center; gap:16px; margin:24px 0 30px 0;">
                <div style="width:54px; height:54px; border-radius:50%; background:{curr['bg']}; color:{curr['color']}; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:15px;">{curr['id']}</div>
                <div>
                    <div style="font-size:18px; font-weight:800; color:#1E293B; margin-bottom:4px;">{curr['id']}</div>
                    <div class="badge" style="background:{curr['bg']}; color:{curr['color']};">{curr['label']} · {curr['prob']}%</div>
                </div>
            </div>
            
            <div class="detail-item"><span>👤 성별</span><b style="color:#1E293B;">{curr['gender']}</b></div>
            <div class="detail-item"><span>📅 경과일</span><b style="color:#1E293B;">{curr['day']}</b></div>
            <div class="detail-item"><span>🛒 주문 횟수</span><b style="color:#1E293B;">{curr['count']}</b></div>
            <div class="detail-item"><span>💵 캐시백</span><b style="color:#1E293B;">{curr['cashback']}</b></div>
            <div class="detail-item" style="border:none;">
                <span>⭐ 만족도</span>
                <span style="color:#F6C23E; font-size:16px;">{"★"*curr['sat']}<span style="color:#E2E8F0;">{"★"*(5-curr['sat'])}</span></span>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    
    # ⚡ [우측 하단] 액션 추천 (카운트 연동 완료)
    with st.container(border=True):
        st.markdown("<b style='font-size:15px; color:#1E293B;'>⚡ 액션 추천</b>", unsafe_allow_html=True)
        
        status_color = "#3B82F6" if selected_count > 0 else "#94A3B8"
        bg_color = "#EFF6FF" if selected_count > 0 else "#F8FAFC"
        border_color = "#BFDBFE" if selected_count > 0 else "#E2E8F0"
        
        st.markdown(f"""
            <div style='background:{bg_color}; color:{status_color}; padding:14px; border-radius:8px; font-size:13px; font-weight:600; margin:15px 0; border: 1px solid {border_color}; display:flex; align-items:center; gap:8px;'>
                <span>👥</span> {selected_count}명 선택됨 <span style='font-weight:400; color:#94A3B8; font-size:11px; margin-left:auto;'>· 캠페인 대상을 확인하세요</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.radio("캠페인 옵션", ["10% 할인 쿠폰 발급", "20% 할인 쿠폰 발급", "무료 배송권 발송", "추천 상품 알림"], index=0, label_visibility="collapsed")
        st.write("")
        if st.button("✔ 캠페인 실행", use_container_width=True, type="primary"):
            if selected_count > 0:
                st.success(f"{selected_count}명의 고객에게 캠페인 발송이 완료되었습니다!")
            else:
                st.warning("먼저 고객 리스트에서 발송 대상을 체크해주세요.")