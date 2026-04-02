import streamlit as st
import pandas as pd
import psycopg2
from collections import Counter
from components.sidebar import render_sidebar

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Re:tain | 고객 이탈 관리", layout="wide", initial_sidebar_state="expanded")

COMPLAINT_MAP = {
    "NumberOfAddress":          ("🚚 잦은 배송지 변경 및 오배송 경험",      "#FFF7ED", "#FFEDD5", "#C2410C"),
    "WarehouseToHome":          ("🚚 출고지 거리에 따른 배송 지연",          "#FFF7ED", "#FFEDD5", "#C2410C"),
    "Complain":                 ("📞 고객센터 대응 및 서비스 불만족",         "#FEF2F2", "#FECACA", "#991B1B"),
    "SatisfactionScore":        ("⭐ 전반적인 서비스 만족도 저하",            "#FEF2F2", "#FECACA", "#991B1B"),
    "CashbackAmount":           ("💰 캐시백 등 리워드 혜택 체감 부족",        "#F0FDF4", "#BBF7D0", "#166534"),
    "CouponUsed":               ("🎟️ 적용 가능한 쿠폰 제한 및 혜택 부족",   "#F0FDF4", "#BBF7D0", "#166534"),
    "Tenure":                   ("👑 장기 고객 대상 특별 혜택 부재",          "#EEF2FF", "#C7D2FE", "#3730A3"),
    "CityTier":                 ("🏢 거주 지역 서비스 및 배송 인프라 부족",   "#EFF6FF", "#BFDBFE", "#1D4ED8"),
    "OrderCount":               ("🛒 원하는 상품 라인업 및 재고 부족",        "#F8FAFC", "#E2E8F0", "#334155"),
    "DaysSinceLastOrder":       ("⏳ 최근 방문 및 주문 필요성 못 느낌",       "#F8FAFC", "#E2E8F0", "#334155"),
    "NumberOfDeviceRegistered": ("📱 모바일 앱/기기 연동 및 사용 불편",       "#F8FAFC", "#E2E8F0", "#334155"),
}

ACTION_MAP = {
    "NumberOfAddress":          ["배송지 정확도 확인 알림톡 발송", "안심 배송 보장(무료 반품) 쿠폰 지급"],
    "WarehouseToHome":          ["익일 배송(우선 배송) 무료 업그레이드권 발급", "배송 지연 사과 및 3,000원 보상 포인트 지급"],
    "Complain":                 ["VIP 전담 상담사 배정 알림톡 발송", "서비스 개선 약속 및 10% 사과 할인 쿠폰"],
    "SatisfactionScore":        ["만족도 설문조사 참여 시 5,000원 지급", "베스트셀러 상품 20% 특별 할인권 발급"],
    "CashbackAmount":           ["다음 주문 시 '캐시백 2배 적립' 부스터 발급", "미사용 포인트 소멸 예정 알림 및 사용 촉진"],
    "CouponUsed":               ["조건 없는(No Limit) 15% 무적 할인 쿠폰 발급", "장바구니 리마인드 및 전용 배송비 무료 쿠폰"],
    "Tenure":                   ["장기 고객 감사 VVIP 승급 및 전용 혜택 부여", "가입기념일 축하 스페셜 기프트/쿠폰 발송"],
    "CityTier":                 ["해당 지역 한정 배송비 50% 할인권 발급", "지역 제휴 오프라인 매장 픽업 할인 안내"],
    "OrderCount":               ["고객 맞춤형 신상품 입고 알림 신청 유도", "품절 상품 대체 추천 및 10% 타임 세일 안내"],
    "DaysSinceLastOrder":       ["'돌아오세요' 웰컴백 20% 파격 할인 쿠폰", "최근 본 상품 가격 인하 알림톡 발송"],
    "NumberOfDeviceRegistered": ["앱 리뉴얼 안내 및 앱 전용 3,000원 쿠폰", "간편 결제 등록 시 5% 추가 할인 혜택 제공"],
}

LABEL_CONDITIONS = {
    "안전":   'c."Churn_Prob" < 0.2',
    "양호":   'c."Churn_Prob" >= 0.2 AND c."Churn_Prob" < 0.5',
    "주의":   'c."Churn_Prob" >= 0.5 AND c."Churn_Prob" < 0.8',
    "위험":   'c."Churn_Prob" >= 0.8 AND c."Churn_Prob" < 0.95',
    "고위험": 'c."Churn_Prob" >= 0.95',
}

PAGE_SIZE  = 100
TAB_TITLES = ["전체", "안전", "양호", "주의", "위험", "고위험"]


# --- 2. DB 함수 ---
def get_conn():
    return psycopg2.connect(
        host=st.secrets["postgres"]["host"],
        port=st.secrets["postgres"]["port"],
        dbname=st.secrets["postgres"]["database"],
        user=st.secrets["postgres"]["user"],
        password=st.secrets["postgres"]["password"],
    )

@st.cache_data
def get_kpi_stats():
    conn = get_conn()
    df = pd.read_sql("""
        SELECT
            COUNT(*) AS total_cnt,
            SUM(b."Churn") AS churn_cnt,
            AVG(c."Churn_Prob") AS avg_pred_prob
        FROM customer_base b
        LEFT JOIN churn_metrics c ON b."CustomerID" = c."CustomerID"
    """, conn)
    conn.close()
    return df.iloc[0]

@st.cache_data
def get_tab_total_counts():
    conn = get_conn()
    base_q = """
        SELECT COUNT(*) AS cnt
        FROM customer_base b
        LEFT JOIN churn_metrics c ON b."CustomerID" = c."CustomerID"
    """
    counts = {}
    counts["전체"] = int(pd.read_sql(base_q, conn)['cnt'].iloc[0])
    for label, cond in LABEL_CONDITIONS.items():
        counts[label] = int(pd.read_sql(f"{base_q} WHERE {cond}", conn)['cnt'].iloc[0])
    conn.close()
    return counts

@st.cache_data
def load_customers_page(offset=0, limit=PAGE_SIZE, label_filter=None):
    conn = get_conn()
    where = f"WHERE {LABEL_CONDITIONS[label_filter]}" if label_filter else ""
    query = f"""
        SELECT
            b."CustomerID", b."Gender", b."Churn",
            a."DaySinceLastOrder", a."OrderCount", a."CashbackAmount", a."SatisfactionScore",
            c."Churn_Prob", c."1st_leave", c."2nd_leave"
        FROM customer_base b
        LEFT JOIN customer_activity a ON b."CustomerID" = a."CustomerID"
        LEFT JOIN churn_metrics c      ON b."CustomerID" = c."CustomerID"
        {where}
        ORDER BY c."Churn_Prob" DESC NULLS LAST
        LIMIT {limit} OFFSET {offset}
    """
    df = pd.read_sql(query, conn)
    conn.close()

    df = df.fillna({
        'Churn_Prob': 0, 'Churn': 0, 'DaySinceLastOrder': 0,
        'OrderCount': 0, 'CashbackAmount': 0, 'SatisfactionScore': 5,
        '1st_leave': '', '2nd_leave': '',
    })

    customers = []
    for _, row in df.iterrows():
        p = row['Churn_Prob']
        if p < 0.2:    label, dot, color, bg = "안전",   "🟢", "#5FAD56", "#EEF6EE"
        elif p < 0.5:  label, dot, color, bg = "양호",   "🟡", "#B8A838", "#FEF9E7"
        elif p < 0.8:  label, dot, color, bg = "주의",   "🟠", "#E6A050", "#FDF1E3"
        elif p < 0.95: label, dot, color, bg = "위험",   "🔴", "#D97A7A", "#FDEAEA"
        else:          label, dot, color, bg = "고위험", "🔥", "#C0392B", "#FDEDEC"

        cashback_val = int(row['CashbackAmount'])
        customers.append({
            "id":           str(row['CustomerID']),
            "prob":         int(round(p * 100)),
            "label":        label, "dot": dot, "color": color, "bg": bg,
            "segment":      "Risk" if p >= 0.7 else "Active",
            "day":          f"{int(row['DaySinceLastOrder'])}일",
            "count":        f"{int(row['OrderCount'])}회",
            "amount":       f"{cashback_val:,}원",   # 금액 컬럼 = 캐시백
            "gender":       "남성" if str(row['Gender']).lower() == "male" else "여성",
            "cashback":     f"{cashback_val:,}원",
            "sat":          int(row['SatisfactionScore']),
            "reason1":      row['1st_leave'],
            "reason2":      row['2nd_leave'],
            "churn_actual": int(row['Churn']),
        })
    return customers


# --- 3. 세션 초기화 ---
if "tab_offsets" not in st.session_state:
    st.session_state.tab_offsets = {t: 0 for t in TAB_TITLES}

if "tab_customers" not in st.session_state:
    st.session_state.tab_customers = {
        t: load_customers_page(offset=0, label_filter=None if t == "전체" else t)
        for t in TAB_TITLES
    }

if "check_states" not in st.session_state:
    st.session_state.check_states = {}
    for t in TAB_TITLES:
        for c in st.session_state.tab_customers[t]:
            st.session_state.check_states[c['id']] = False

if "selected_id" not in st.session_state:
    first_list = st.session_state.tab_customers["전체"]
    st.session_state.selected_id = first_list[0]['id'] if first_list else None


# --- 4. 콜백 ---
def update_all_checks(tab_name, display_ids):
    val = st.session_state[f"master_{tab_name}"]
    for cid in display_ids:
        st.session_state.check_states[cid] = val
        st.session_state[f"chk_{tab_name}_{cid}"] = val

def update_single_check(cid, tab_name):
    st.session_state.check_states[cid] = st.session_state[f"chk_{tab_name}_{cid}"]

def set_selected_customer(cid):
    st.session_state.selected_id = cid

def go_prev_page(tab_name):
    st.session_state.tab_offsets[tab_name] -= PAGE_SIZE
    _reload_tab(tab_name)

def go_next_page(tab_name):
    st.session_state.tab_offsets[tab_name] += PAGE_SIZE
    _reload_tab(tab_name)

def _reload_tab(tab_name):
    new_data = load_customers_page(
        offset=st.session_state.tab_offsets[tab_name],
        label_filter=None if tab_name == "전체" else tab_name,
    )
    st.session_state.tab_customers[tab_name] = new_data
    for c in new_data:
        if c['id'] not in st.session_state.check_states:
            st.session_state.check_states[c['id']] = False
    if new_data:
        st.session_state.selected_id = new_data[0]['id']


# --- 5. KPI 데이터 ---
kpi        = get_kpi_stats()
tab_counts = get_tab_total_counts()
total_cnt  = int(kpi['total_cnt'])
actual_rate = f"{kpi['churn_cnt'] / total_cnt * 100:.2f}%" if total_cnt > 0 else "0%"
pred_rate   = f"{kpi['avg_pred_prob'] * 100:.2f}%"


# --- 6. 사이드바 ---
render_sidebar("고객 이탈 관리")


# --- 7. CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root { --font-inter: 'Inter', sans-serif; }
.stApp, [data-testid="stSidebar"], .stMarkdown { font-family: var(--font-inter) !important; }
button[kind="primary"] {
    background-color: #4F75A4 !important; border-color: #4F75A4 !important;
    color: white !important; border-radius: 8px !important;
    font-weight: bold !important; padding: 10px 24px !important;
}
button[kind="primary"]:hover { background-color: #3D5A80 !important; border-color: #3D5A80 !important; }
h1,h2,h3,b,strong { font-family: var(--font-inter) !important; font-weight: 700; }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
.main .block-container { padding-top:2rem !important; padding-left:280px !important; padding-right:40px !important; max-width:1500px !important; }
[data-testid="collapsedControl"] { display:none !important; }
[data-testid="stSidebar"] { min-width:260px !important; max-width:260px !important; }
.kpi-card { background:white; padding:24px; border-radius:16px; border:1px solid #E2E8F0; box-shadow:0 1px 3px rgba(0,0,0,0.02); }
.kpi-val  { font-size:28px; font-weight:800; color:#1E293B; margin-top:10px; margin-bottom:2px; }
.p-bar-bg { background:#F1F5F9; height:6px; border-radius:10px; width:50px; display:inline-block; margin-right:10px; overflow:hidden; }
.p-bar-fill { height:100%; border-radius:10px; }
.badge { padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700; display:inline-flex; align-items:center; gap:4px; }
.detail-item { display:flex; justify-content:space-between; padding:12px 0; border-bottom:1px solid #F1F5F9; font-size:13px; color:#475569; }
</style>
""", unsafe_allow_html=True)


# --- 8. 렌더링 ---
st.markdown('<h1 style="font-size:24px; font-weight:800; color:#1E293B; margin-bottom:4px;">고객 이탈 관리</h1>', unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; font-size:14px; margin-bottom:25px;'>이탈 위험 고객을 분류하고 캠페인을 실행하세요</p>", unsafe_allow_html=True)

# KPI
k1, k2, k3 = st.columns(3)
with k1:
    st.markdown(f'<div class="kpi-card"><div style="background:#EEF2F8;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">👥</div><div class="kpi-val">{total_cnt:,}</div><div style="font-size:13px;font-weight:600;color:#334155;">전체 고객 수</div><div style="font-size:12px;color:#94A3B8;">등록 고객 전체</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="kpi-card"><div style="background:#FDEAEA;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">⚠️</div><div class="kpi-val" style="color:#D97A7A;">{actual_rate}</div><div style="font-size:13px;font-weight:600;color:#334155;">실제 이탈 확률</div><div style="font-size:12px;color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi-card"><div style="background:#FDF1E3;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">📉</div><div class="kpi-val" style="color:#E6A050;">{pred_rate}</div><div style="font-size:13px;font-weight:600;color:#334155;">예측 이탈 확률</div><div style="font-size:12px;color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)

st.write("")
m_left, m_right = st.columns([2.6, 1])
selected_count = sum(st.session_state.check_states.values())

with m_left:
    with st.container(border=True):
        st.markdown(f"<div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:10px;margin-bottom:5px;'><b style='font-size:16px;'>고객 리스트</b><span style='font-size:12px;color:#94A3B8;'>전체 {total_cnt:,}명 · <b style='color:#3B82F6;'>{selected_count}명 선택됨</b></span></div>", unsafe_allow_html=True)

        tabs = st.tabs(TAB_TITLES)

        for idx, tab in enumerate(tabs):
            with tab:
                curr_tab     = TAB_TITLES[idx]
                display_list = st.session_state.tab_customers[curr_tab]
                tab_total    = tab_counts.get(curr_tab, 0)
                tab_offset   = st.session_state.tab_offsets[curr_tab]
                cur_page     = tab_offset // PAGE_SIZE + 1
                total_pages  = max(1, (tab_total + PAGE_SIZE - 1) // PAGE_SIZE)

                if not display_list:
                    st.info(f"'{curr_tab}' 등급의 고객이 없습니다.")
                    continue

                display_ids = [c['id'] for c in display_list]
                all_checked = all(st.session_state.check_states.get(cid, False) for cid in display_ids)
                st.session_state[f"master_{curr_tab}"] = all_checked

                st.write("")

                # 헤더
                h1, h2, h3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                with h1:
                    st.checkbox("전체", key=f"master_{curr_tab}", on_change=update_all_checks,
                                args=(curr_tab, display_ids), label_visibility="collapsed")
                with h2:
                    st.markdown('<span style="color:#94A3B8;font-size:12px;font-weight:600;">고객 ID</span>', unsafe_allow_html=True)
                with h3:
                    st.markdown("""
                        <div style="display:flex;color:#94A3B8;font-size:12px;font-weight:600;padding-left:15px;">
                            <div style="flex:1.5;">이탈 확률</div>
                            <div style="flex:1.5;">위험도</div>
                            <div style="flex:1.5;">세그먼트</div>
                            <div style="flex:1.2;">경과일</div>
                            <div style="flex:1;">주문수</div>
                            <div style="flex:1.5;text-align:right;">캐시백</div>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("<hr style='margin:5px 0 10px 0;'>", unsafe_allow_html=True)

                # 바디
                for c in display_list:
                    chk_key = f"chk_{curr_tab}_{c['id']}"
                    st.session_state[chk_key] = st.session_state.check_states.get(c['id'], False)
                    row_bg = "#F0F7FF" if st.session_state[chk_key] else "#FFFFFF"

                    r1, r2, r3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                    with r1:
                        st.checkbox("개별", key=chk_key, on_change=update_single_check,
                                    args=(c['id'], curr_tab), label_visibility="collapsed")
                    with r2:
                        st.button(c['id'], key=f"btn_{curr_tab}_{c['id']}",
                                  on_click=set_selected_customer, args=(c['id'],), use_container_width=True)
                    with r3:
                        st.markdown(f"""
                            <div style="background:{row_bg};border-radius:8px;padding:10px 15px;display:flex;align-items:center;border:1px solid #F1F5F9;">
                                <div style="flex:1.5;display:flex;align-items:center;">
                                    <div class="p-bar-bg"><div class="p-bar-fill" style="background:{c['color']};width:{c['prob']}%;"></div></div>
                                    <b style="color:{c['color']};font-size:12px;">{c['prob']}%</b>
                                </div>
                                <div style="flex:1.5;"><span class="badge" style="background:{c['bg']};color:{c['color']}">{c['dot']} {c['label']}</span></div>
                                <div style="flex:1.5;"><span class="badge" style="background:#F1F5F9;color:#475569">{c['segment']}</span></div>
                                <div style="flex:1.2;font-size:13px;color:#475569;font-weight:500;">{c['day']}</div>
                                <div style="flex:1;font-size:13px;color:#475569;font-weight:500;">{c['count']}</div>
                                <div style="flex:1.5;text-align:right;font-weight:800;font-size:14px;color:#1E293B;">{c['amount']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    st.write("")

                # 페이지네이션
                st.markdown("<hr style='margin:12px 0 8px 0;'>", unsafe_allow_html=True)
                p1, p2, p3 = st.columns([1, 2, 1])
                with p1:
                    st.button("◀ 이전", key=f"prev_{curr_tab}",
                        disabled=(tab_offset == 0),
                        on_click=go_prev_page, args=(curr_tab,), use_container_width=True)
                with p2:
                    st.markdown(f"<div style='text-align:center;font-size:13px;color:#64748B;padding-top:8px;'>{cur_page} / {total_pages} 페이지 ({tab_total:,}명)</div>", unsafe_allow_html=True)
                with p3:
                    st.button("다음 ▶", key=f"next_{curr_tab}",
                    disabled=(tab_offset + PAGE_SIZE >= tab_total),
                    on_click=go_next_page, args=(curr_tab,), use_container_width=True)


with m_right:
    # 상세 정보
    with st.container(border=True):
        st.markdown("<b style='font-size:15px;color:#1E293B;'>고객 상세 정보</b>", unsafe_allow_html=True)

        curr = None
        for t in TAB_TITLES:
            curr = next((c for c in st.session_state.tab_customers[t] if c['id'] == st.session_state.selected_id), None)
            if curr:
                break
        if curr is None:
            curr = st.session_state.tab_customers["전체"][0]

        default_theme = ("분석할 수 없는 데이터", "#F8FAFC", "#E2E8F0", "#475569")
        comp1_text, comp1_bg, comp1_border, comp1_color = COMPLAINT_MAP.get(curr.get('reason1', ''), default_theme)
        comp2_text, comp2_bg, comp2_border, comp2_color = COMPLAINT_MAP.get(curr.get('reason2', ''), default_theme)

        st.markdown(f"""
            <div style="display:flex;align-items:center;gap:16px;margin:24px 0 30px 0;">
                <div style="width:54px;height:54px;border-radius:50%;background:{curr['bg']};color:{curr['color']};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;">{curr['id']}</div>
                <div>
                    <div style="font-size:18px;font-weight:800;color:#1E293B;margin-bottom:4px;">{curr['id']}</div>
                    <div class="badge" style="background:{curr['bg']};color:{curr['color']};">{curr['label']} · {curr['prob']}%</div>
                </div>
            </div>
            <div class="detail-item"><span>👤 성별</span><b style="color:#1E293B;">{curr['gender']}</b></div>
            <div class="detail-item"><span>📅 경과일</span><b style="color:#1E293B;">{curr['day']}</b></div>
            <div class="detail-item"><span>🛒 주문 횟수</span><b style="color:#1E293B;">{curr['count']}</b></div>
            <div class="detail-item"><span>💵 캐시백</span><b style="color:#1E293B;">{curr['cashback']}</b></div>
            <div class="detail-item" style="border:none;">
                <span>⭐ 만족도</span>
                <span style="color:#F6C23E;font-size:16px;">{"★"*curr['sat']}<span style="color:#E2E8F0;">{"★"*(5-curr['sat'])}</span></span>
            </div>
            <div style="border-top:1px dashed #E2E8F0;padding-top:20px;padding-bottom:10px;margin-top:5px;">
                <div style="font-size:13px;font-weight:700;color:#475569;margin-bottom:12px;display:flex;align-items:center;gap:6px;">
                    <span>💬 주요 불만사항</span>
                </div>
                <div style="display:flex;flex-direction:column;gap:8px;">
                    <div style="background:{comp1_bg};border:1px solid {comp1_border};padding:10px 14px;border-radius:8px;">
                        <span style="font-size:13px;font-weight:700;color:{comp1_color};">{comp1_text}</span>
                    </div>
                    <div style="background:{comp2_bg};border:1px solid {comp2_border};padding:10px 14px;border-radius:8px;">
                        <span style="font-size:13px;font-weight:700;color:{comp2_color};">{comp2_text}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # 액션 추천
    with st.container(border=True):
        st.markdown("""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
                <b style='font-size:15px;color:#1E293B;'>⚡ 맞춤형 액션 추천</b>
                <span style='font-size:11px;color:#94A3B8;'>최대 2개 선택</span>
            </div>
        """, unsafe_allow_html=True)

        s_color      = "#3B82F6" if selected_count > 0 else "#94A3B8"
        action_bg    = "#EFF6FF" if selected_count > 0 else "#F8FAFC"
        border_color = "#BFDBFE" if selected_count > 0 else "#E2E8F0"

        st.markdown(f"""
            <div style='background:{action_bg};color:{s_color};padding:14px;border-radius:8px;font-size:13px;font-weight:600;margin:15px 0;border:1px solid {border_color};display:flex;align-items:center;gap:8px;'>
                <span>👥</span> {selected_count}명 선택됨
                <span style='font-weight:400;color:#94A3B8;font-size:11px;margin-left:auto;'>· 캠페인 대상을 확인하세요</span>
            </div>
        """, unsafe_allow_html=True)

        default_actions   = ["10% 할인 쿠폰 발급", "무료 배송권 발송"]
        suggested_actions = []

        if selected_count == 0:
            suggested_actions = (
                ACTION_MAP.get(curr.get('reason1', ''), default_actions) +
                ACTION_MAP.get(curr.get('reason2', ''), default_actions)
            )
        else:
            all_flat = [c for t in TAB_TITLES for c in st.session_state.tab_customers[t]]
            sel_customers = [c for c in all_flat if st.session_state.check_states.get(c['id'], False)]
            all_reasons = []
            for c in sel_customers:
                if c.get('reason1'): all_reasons.append(c['reason1'])
                if c.get('reason2'): all_reasons.append(c['reason2'])
            top_reasons = [item[0] for item in Counter(all_reasons).most_common(2)]
            for r in top_reasons:
                suggested_actions.extend(ACTION_MAP.get(r, default_actions))
            st.markdown("<div style='font-size:12px;color:#64748B;margin-bottom:10px;'>💡 선택된 고객들의 가장 큰 공통 불만에 맞춘 추천입니다.</div>", unsafe_allow_html=True)

        suggested_actions = list(dict.fromkeys(suggested_actions))[:4]
        selected_campaigns = []
        for i, act in enumerate(suggested_actions):
            chk_key = f"action_chk_{i}"
            if chk_key not in st.session_state:
                st.session_state[chk_key] = False
            if st.checkbox(act, key=chk_key):
                selected_campaigns.append(act)

        st.write("")

        if st.button("✔ 캠페인 실행 완료!", use_container_width=True, type="primary"):
            if selected_count == 0:
                st.warning("⚠️ 왼쪽 고객 리스트에서 캠페인을 발송할 대상을 체크해주세요.")
            elif len(selected_campaigns) == 0:
                st.warning("⚠️ 최소 1개의 맞춤형 액션을 선택해주세요.")
            elif len(selected_campaigns) > 2:
                st.warning("⚠️ 캠페인 액션은 최대 2개까지만 선택할 수 있습니다.")
            else:
                st.toast(f"{selected_count}명의 고객에게 맞춤형 편지가 발송되었습니다!", icon="📮")
                st.success(f"✅ {selected_count}명의 고객에게 '{', '.join(selected_campaigns)}' 캠페인 발송이 완료되었습니다!")
