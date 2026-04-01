import streamlit as st
from components.sidebar import render_sidebar

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Re:tain | 고객 이탈 관리", layout="wide", initial_sidebar_state="expanded")
# 🚨 [추가] 영어 원본 데이터를 한국어 불만사항 UI로 변환하는 매핑 딕셔너리
# 구조: "영어원본": ("한국어 불만사항 텍스트", "배경색", "테두리색", "글자색")
COMPLAINT_MAP = {
    # 🚚 배송/물류 관련 (오렌지 톤)
    "NumberOfAddress": ("🚚 잦은 배송지 변경 및 오배송 경험", "#FFF7ED", "#FFEDD5", "#C2410C"),
    "WarehouseToHome": ("🚚 출고지 거리에 따른 배송 지연", "#FFF7ED", "#FFEDD5", "#C2410C"),
    
    # 📞 CS/서비스 불만 관련 (레드 톤)
    "Complain": ("📞 고객센터 대응 및 서비스 불만족", "#FEF2F2", "#FECACA", "#991B1B"),
    "SatisfactionScore": ("⭐ 전반적인 서비스 만족도 저하", "#FEF2F2", "#FECACA", "#991B1B"),
    
    # 💰 금전/혜택 관련 (그린 톤)
    "CashbackAmount": ("💰 캐시백 등 리워드 혜택 체감 부족", "#F0FDF4", "#BBF7D0", "#166534"),
    "CouponUsed": ("🎟️ 적용 가능한 쿠폰 제한 및 혜택 부족", "#F0FDF4", "#BBF7D0", "#166534"),
    
    # 👑 VIP/로열티 관련 (퍼플 톤)
    "Tenure": ("👑 장기 고객 대상 특별 혜택 부재", "#EEF2FF", "#C7D2FE", "#3730A3"),
    
    # 🏢 지역/인프라 관련 (블루 톤)
    "CityTier": ("🏢 거주 지역 서비스 및 배송 인프라 부족", "#EFF6FF", "#BFDBFE", "#1D4ED8"),
    
    # 🛒 플랫폼/이용 행태 관련 (그레이/슬레이트 톤)
    "OrderCount": ("🛒 원하는 상품 라인업 및 재고 부족", "#F8FAFC", "#E2E8F0", "#334155"),
    "DaysSinceLastOrder": ("⏳ 최근 방문 및 주문 필요성 못 느낌", "#F8FAFC", "#E2E8F0", "#334155"),
    "NumberOfDeviceRegistered": ("📱 모바일 앱/기기 연동 및 사용 불편", "#F8FAFC", "#E2E8F0", "#334155")
}


# 🚨 [추가] 불만사항(영어 원본 데이터)에 따른 맞춤형 액션 2가지 매핑
ACTION_MAP = {
    # 🚚 배송/물류 관련
    "NumberOfAddress": ["배송지 정확도 확인 알림톡 발송", "안심 배송 보장(무료 반품) 쿠폰 지급"],
    "WarehouseToHome": ["익일 배송(우선 배송) 무료 업그레이드권 발급", "배송 지연 사과 및 3,000원 보상 포인트 지급"],
    
    # 📞 CS/서비스 불만 관련
    "Complain": ["VIP 전담 상담사 배정 알림톡 발송", "서비스 개선 약속 및 10% 사과 할인 쿠폰"],
    "SatisfactionScore": ["만족도 설문조사 참여 시 5,000원 지급", "베스트셀러 상품 20% 특별 할인권 발급"],
    
    # 💰 금전/혜택 관련
    "CashbackAmount": ["다음 주문 시 '캐시백 2배 적립' 부스터 발급", "미사용 포인트 소멸 예정 알림 및 사용 촉진"],
    "CouponUsed": ["조건 없는(No Limit) 15% 무적 할인 쿠폰 발급", "장바구니 리마인드 및 전용 배송비 무료 쿠폰"],
    
    # 👑 VIP/로열티 관련
    "Tenure": ["장기 고객 감사 VVIP 승급 및 전용 혜택 부여", "가입기념일 축하 스페셜 기프트/쿠폰 발송"],
    
    # 🏢 지역/인프라 관련
    "CityTier": ["해당 지역 한정 배송비 50% 할인권 발급", "지역 제휴 오프라인 매장 픽업 할인 안내"],
    
    # 🛒 플랫폼/이용 행태 관련
    "OrderCount": ["고객 맞춤형 신상품 입고 알림 신청 유도", "품절 상품 대체 추천 및 10% 타임 세일 안내"],
    "DaysSinceLastOrder": ["'돌아오세요' 웰컴백 20% 파격 할인 쿠폰", "최근 본 상품 가격 인하 알림톡 발송"],
    "NumberOfDeviceRegistered": ["앱 리뉴얼 안내 및 앱 전용 3,000원 쿠폰", "간편 결제 등록 시 5% 추가 할인 혜택 제공"]
}
# --- 2. 데이터 정의 및 세션 상태 초기화 ---
if "customers" not in st.session_state:
    st.session_state.customers = [
        {"id": "C001", "prob": 97, "label": "고위험", "dot": "🔥", "color": "#C0392B", "bg": "#FDEDEC", "segment": "At Risk", "day": "60일", "count": "1회", "amount": "$120", "gender": "남성", "cashback": "$0", "sat": 2, 
            "reason1": "NumberOfAddress", "reason2": "Complain"}, # 영어 원본 데이터 수신
        {"id": "C002", "prob": 85, "label": "위험",   "dot": "🔴", "color": "#D97A7A", "bg": "#FDEAEA", "segment": "At Risk", "day": "40일", "count": "3회", "amount": "$340", "gender": "여성", "cashback": "$12", "sat": 3, 
            "reason1": "Complain", "reason2": "CashbackAmount"},
        {"id": "C003", "prob": 72, "label": "주의",   "dot": "🟠", "color": "#E6A050", "bg": "#FDF1E3", "segment": "Active",  "day": "20일", "count": "5회", "amount": "$780", "gender": "남성", "cashback": "$45", "sat": 3, 
            "reason1": "Tenure", "reason2": "WarehouseToHome"},
        {"id": "C004", "prob": 45, "label": "양호",   "dot": "🟡", "color": "#B8A838", "bg": "#FEF9E7", "segment": "Active",  "day": "10일", "count": "8회", "amount": "$560", "gender": "여성", "cashback": "$78", "sat": 4, 
            "reason1": "OrderCount", "reason2": "CouponUsed"},
        {"id": "C005", "prob": 15, "label": "안전",   "dot": "🟢", "color": "#5FAD56", "bg": "#EEF6EE", "segment": "VIP",     "day": "3일",  "count": "15회", "amount": "$2,400", "gender": "남성", "cashback": "$210", "sat": 5, 
            "reason1": "CashbackAmount", "reason2": "NumberOfDeviceRegistered"},
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
    
    /* Primary 버튼 커스텀 (이미지 색상 반영) */
    button[kind="primary"] {
        background-color: #4F75A4 !important; /* 요청하신 스틸 블루 색상 */
        border-color: #4F75A4 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
    }
    button[kind="primary"]:hover {
        background-color: #3D5A80 !important; /* 마우스 오버 시 자연스럽게 살짝 어두워짐 */
        border-color: #3D5A80 !important;
        color: white !important;
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
    st.markdown('<div class="kpi-card"><div style="background:#EEF2F8; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">👥</div><div class="kpi-val">1,126</div><div style="font-size:13px; font-weight:600; color:#334155;">전체 고객 수</div><div style="font-size:12px; color:#94A3B8;">등록 고객 전체</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="kpi-card"><div style="background:#FDEAEA; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">⚠️</div><div class="kpi-val" style="color:#D97A7A;">16.87%</div><div style="font-size:13px; font-weight:600; color:#334155;">실제 이탈 확률</div><div style="font-size:12px; color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="kpi-card"><div style="background:#FDF1E3; width:36px; height:36px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px;">📉</div><div class="kpi-val" style="color:#E6A050;">18.38%</div><div style="font-size:13px; font-weight:600; color:#334155;">예측 이탈 확률</div><div style="font-size:12px; color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)

st.write("")

# [하단 메인 분할]
m_left, m_right = st.columns([2.6, 1])
selected_count = sum(st.session_state.check_states.values())


with m_left:
    with st.container(border=True):
        st.markdown(f"<div style='display:flex; justify-content:space-between; align-items:center; padding-bottom: 10px; margin-bottom:5px;'><b style='font-size:16px;'>고객 리스트</b><span style='font-size:12px; color:#94A3B8;'>{len(st.session_state.customers)}명 표시 · <b style='color:#3B82F6;'>{selected_count}명 선택됨</b></span></div>", unsafe_allow_html=True)
        
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
        
        # 🚨 [핵심] 영어 데이터를 한국어 및 색상 테마로 변환
        default_theme = ("분석할 수 없는 데이터", "#F8FAFC", "#E2E8F0", "#475569")
        comp1_text, comp1_bg, comp1_border, comp1_color = COMPLAINT_MAP.get(curr.get('reason1', ''), default_theme)
        comp2_text, comp2_bg, comp2_border, comp2_color = COMPLAINT_MAP.get(curr.get('reason2', ''), default_theme)

        # HTML 마크다운 렌더링 (빈 줄 없이 연속 작성하여 깨짐 방지)
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
            <div style="border-top: 1px dashed #E2E8F0; padding-top: 20px; padding-bottom: 10px; margin-top: 5px;">
                <div style="font-size: 13px; font-weight: 700; color: #475569; margin-bottom: 12px;  display: flex; align-items: center; gap: 6px;">
                    <span>💬 주요 불만사항</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="background: {comp1_bg}; border: 1px solid {comp1_border}; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 13px; font-weight: 700; color: {comp1_color};">{comp1_text}</span>
                    </div>
                    <div style="background: {comp2_bg}; border: 1px solid {comp2_border}; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 13px; font-weight: 700; color: {comp2_color};">{comp2_text}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # ⚡ [우측 하단] 액션 추천 (다중 선택 시 통계 기반 추천)
    with st.container(border=True):
        st.markdown(f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;">
                <b style='font-size:15px; color:#1E293B;'>⚡ 맞춤형 액션 추천</b>
                <span style='font-size:11px; color:#94A3B8;'>최대 2개 선택</span>
            </div>
        """, unsafe_allow_html=True)
        
        status_color = "#3B82F6" if selected_count > 0 else "#94A3B8"
        bg_color = "#EFF6FF" if selected_count > 0 else "#F8FAFC"
        border_color = "#BFDBFE" if selected_count > 0 else "#E2E8F0"
        
        st.markdown(f"""
            <div style='background:{bg_color}; color:{status_color}; padding:14px; border-radius:8px; font-size:13px; font-weight:600; margin:15px 0; border: 1px solid {border_color}; display:flex; align-items:center; gap:8px;'>
                <span>👥</span> {selected_count}명 선택됨 <span style='font-weight:400; color:#94A3B8; font-size:11px; margin-left:auto;'>· 캠페인 대상을 확인하세요</span>
            </div>
        """, unsafe_allow_html=True)
        
        default_actions = ["10% 할인 쿠폰 발급", "무료 배송권 발송"]
        suggested_actions = []

        # 🚨 [스마트 로직] 선택된 인원수에 따른 분기 처리
        if selected_count == 0:
            # 선택된 사람이 없으면 현재 클릭해서 보고 있는 1명의 액션 추천
            suggested_actions = ACTION_MAP.get(curr.get('reason1', ''), default_actions) + ACTION_MAP.get(curr.get('reason2', ''), default_actions)
        
        else:
            # 1. 체크박스로 선택된 고객들만 필터링
            from collections import Counter
            selected_customers = [c for c in st.session_state.customers if st.session_state.check_states[c['id']]]
            
            # 2. 선택된 고객들의 모든 불만사항(reason)을 하나의 리스트로 수집
            all_reasons = []
            for c in selected_customers:
                if c.get('reason1'): all_reasons.append(c['reason1'])
                if c.get('reason2'): all_reasons.append(c['reason2'])
            
            # 3. 빈도수가 가장 높은 Top 2 불만사항 추출
            top_reasons = [item[0] for item in Counter(all_reasons).most_common(2)]
            
            # 4. Top 2 불만사항에 대한 액션만 리스트에 추가
            for r in top_reasons:
                suggested_actions.extend(ACTION_MAP.get(r, default_actions))
            
            st.markdown("<div style='font-size:12px; color:#64748B; margin-bottom:10px;'>💡 선택된 고객들의 가장 큰 공통 불만에 맞춘 추천입니다.</div>", unsafe_allow_html=True)

        # 리스트 중복 제거 (순서 유지) 및 UI를 위해 최대 4개까지만 노출
        suggested_actions = list(dict.fromkeys(suggested_actions))[:4]
        
        # 다중 선택 체크박스 생성
        selected_campaigns = []
        for i, act in enumerate(suggested_actions):
            chk_key = f"action_chk_{i}"
            if chk_key not in st.session_state:
                st.session_state[chk_key] = False # 다이내믹 렌더링을 위해 기본은 False로 둡니다
                
            if st.checkbox(act, key=chk_key):
                selected_campaigns.append(act)
        
        st.write("")
        
        # 🚀 버튼 클릭 및 예외 처리 로직 (최대 2개 제한)
        if st.button("✔ 캠페인 실행 완료!", use_container_width=True, type="primary"):
            if selected_count == 0:
                st.warning("⚠️ 왼쪽 고객 리스트에서 캠페인을 발송할 대상을 체크해주세요.")
            elif len(selected_campaigns) == 0:
                st.warning("⚠️ 최소 1개의 맞춤형 액션을 선택해주세요.")
            elif len(selected_campaigns) > 2:
                st.warning("⚠️ 캠페인 액션은 최대 2개까지만 선택할 수 있습니다. 체크를 해제해주세요.")
            else:
                st.toast(f"{selected_count}명의 고객에게 맞춤형 편지가 발송되었습니다!", icon="📮")
                st.success(f"✅ {selected_count}명의 고객에게 '{', '.join(selected_campaigns)}' 캠페인 발송이 완료되었습니다!")