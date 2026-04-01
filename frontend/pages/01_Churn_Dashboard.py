import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Re:tain | 고객 이탈 관리", layout="wide", initial_sidebar_state="expanded")

# ── COMPLAINT_MAP / ACTION_MAP (기존 유지) ──────────────────────────────
COMPLAINT_MAP = {
    "NumberOfAddress":         ("🚚 잦은 배송지 변경 및 오배송 경험",         "#FFF7ED", "#FFEDD5", "#C2410C"),
    "WarehouseToHome":         ("🚚 출고지 거리에 따른 배송 지연",             "#FFF7ED", "#FFEDD5", "#C2410C"),
    "Complain":                ("📞 고객센터 대응 및 서비스 불만족",           "#FEF2F2", "#FECACA", "#991B1B"),
    "SatisfactionScore":       ("⭐ 전반적인 서비스 만족도 저하",              "#FEF2F2", "#FECACA", "#991B1B"),
    "CashbackAmount":          ("💰 캐시백 등 리워드 혜택 체감 부족",          "#F0FDF4", "#BBF7D0", "#166534"),
    "CouponUsed":              ("🎟️ 적용 가능한 쿠폰 제한 및 혜택 부족",      "#F0FDF4", "#BBF7D0", "#166534"),
    "Tenure":                  ("👑 장기 고객 대상 특별 혜택 부재",            "#EEF2FF", "#C7D2FE", "#3730A3"),
    "CityTier":                ("🏢 거주 지역 서비스 및 배송 인프라 부족",     "#EFF6FF", "#BFDBFE", "#1D4ED8"),
    "OrderCount":              ("🛒 원하는 상품 라인업 및 재고 부족",          "#F8FAFC", "#E2E8F0", "#334155"),
    "DaysSinceLastOrder":      ("⏳ 최근 방문 및 주문 필요성 못 느낌",        "#F8FAFC", "#E2E8F0", "#334155"),
    "NumberOfDeviceRegistered":("📱 모바일 앱/기기 연동 및 사용 불편",        "#F8FAFC", "#E2E8F0", "#334155"),
    "Dormancy_Shock":          ("⏳ 최근 방문 및 주문 필요성 못 느낌",        "#F8FAFC", "#E2E8F0", "#334155"),
    "Silent_Killer":           ("😶 불만 없으나 만족도 낮은 조용한 이탈 징후","#FEF2F2", "#FECACA", "#991B1B"),
    "Stagnant_Loyal":          ("👑 장기 고객 대상 특별 혜택 부재",            "#EEF2FF", "#C7D2FE", "#3730A3"),
    "IssueIndex":              ("📞 고객센터 대응 및 서비스 불만족",           "#FEF2F2", "#FECACA", "#991B1B"),
}

ACTION_MAP = {
    "NumberOfAddress":         ["배송지 정확도 확인 알림톡 발송", "안심 배송 보장(무료 반품) 쿠폰 지급"],
    "WarehouseToHome":         ["익일 배송(우선 배송) 무료 업그레이드권 발급", "배송 지연 사과 및 3,000원 보상 포인트 지급"],
    "Complain":                ["VIP 전담 상담사 배정 알림톡 발송", "서비스 개선 약속 및 10% 사과 할인 쿠폰"],
    "SatisfactionScore":       ["만족도 설문조사 참여 시 5,000원 지급", "베스트셀러 상품 20% 특별 할인권 발급"],
    "CashbackAmount":          ["다음 주문 시 '캐시백 2배 적립' 부스터 발급", "미사용 포인트 소멸 예정 알림 및 사용 촉진"],
    "CouponUsed":              ["조건 없는(No Limit) 15% 무적 할인 쿠폰 발급", "장바구니 리마인드 및 전용 배송비 무료 쿠폰"],
    "Tenure":                  ["장기 고객 감사 VVIP 승급 및 전용 혜택 부여", "가입기념일 축하 스페셜 기프트/쿠폰 발송"],
    "CityTier":                ["해당 지역 한정 배송비 50% 할인권 발급", "지역 제휴 오프라인 매장 픽업 할인 안내"],
    "OrderCount":              ["고객 맞춤형 신상품 입고 알림 신청 유도", "품절 상품 대체 추천 및 10% 타임 세일 안내"],
    "DaysSinceLastOrder":      ["'돌아오세요' 웰컴백 20% 파격 할인 쿠폰", "최근 본 상품 가격 인하 알림톡 발송"],
    "NumberOfDeviceRegistered":["앱 리뉴얼 안내 및 앱 전용 3,000원 쿠폰", "간편 결제 등록 시 5% 추가 할인 혜택 제공"],
    "Dormancy_Shock":          ["'돌아오세요' 웰컴백 20% 파격 할인 쿠폰", "최근 본 상품 가격 인하 알림톡 발송"],
    "Silent_Killer":           ["VIP 전담 상담사 배정 알림톡 발송", "만족도 설문조사 참여 시 5,000원 지급"],
    "Stagnant_Loyal":          ["장기 고객 감사 VVIP 승급 및 전용 혜택 부여", "가입기념일 축하 스페셜 기프트/쿠폰 발송"],
    "IssueIndex":              ["VIP 전담 상담사 배정 알림톡 발송", "서비스 개선 약속 및 10% 사과 할인 쿠폰"],
}

# ── CSV → customers 리스트 변환 함수 ────────────────────────────────────
@st.cache_data
def load_customers(csv_path: str):
    """
    customer_list.csv를 읽어서 기존 customers 딕셔너리 리스트로 변환
    노트북에서 생성한 customer_list.csv 컬럼 기준
    """
    df = pd.read_csv(csv_path)

    # ── 컬럼 매핑 ───────────────────────────────────────────────────────
    # Churn_Prob → prob (0~1 → 0~100 퍼센트 정수)
    # RiskLevel  → label (안전/관심/주의/위험/고위험)
    # CustomerGrade → segment (VIP/Platinum/Gold/Silver/Risk)
    # Tenure_log → day (역변환: e^x 개월 → 일수 근사)
    # MonthlyOrderFreq → count (월 주문 빈도로 총 주문 수 근사)
    # CashbackPerOrder * MonthlyOrderFreq → amount (총 캐시백 근사)

    # 위험도 → 색상 매핑
    risk_style = {
        "고위험": {"dot": "🔥", "color": "#C0392B", "bg": "#FDEDEC"},
        "위험":   {"dot": "🔴", "color": "#D97A7A", "bg": "#FDEAEA"},
        "주의":   {"dot": "🟠", "color": "#E6A050", "bg": "#FDF1E3"},
        "관심":   {"dot": "🟡", "color": "#B8A838", "bg": "#FEF9E7"},
        "안전":   {"dot": "🟢", "color": "#5FAD56", "bg": "#EEF6EE"},
    }

    # 불만사항 Top2 자동 추출 함수 (피처 기반)
    def get_top_reasons(row):
        """
        이탈에 기여하는 피처를 우선순위로 뽑아 reason1, reason2 결정
        """
        scores = {}
        if row.get("IssueIndex", 0) == 1:
            scores["IssueIndex"] = 0.9
        if row.get("Silent_Killer", 0) == 1:
            scores["Silent_Killer"] = 0.85
        if row.get("Stagnant_Loyal", 0) == 1:
            scores["Stagnant_Loyal"] = 0.8
        if row.get("Dormancy_Shock", 0) > 3:
            scores["Dormancy_Shock"] = min(row["Dormancy_Shock"] / 10, 0.9)
        if row.get("NumberOfAddress", 0) >= 4:
            scores["NumberOfAddress"] = 0.7
        if row.get("NumberOfDeviceRegistered", 0) >= 5:
            scores["NumberOfDeviceRegistered"] = 0.6
        if row.get("Promo_Sensitivity", 0) > 0.5:
            scores["CouponUsed"] = 0.5
        if row.get("CashbackPerOrder", 0) < 10:
            scores["CashbackAmount"] = 0.5
        if row.get("Stagnant_Loyal", 0) == 1:
            scores["Tenure"] = 0.6

        sorted_reasons = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        r1 = sorted_reasons[0][0] if len(sorted_reasons) > 0 else "DaysSinceLastOrder"
        r2 = sorted_reasons[1][0] if len(sorted_reasons) > 1 else "OrderCount"
        return r1, r2

    # 성별 복원
    def get_gender(row):
        return "남성" if row.get("Gender_Male", 0) == 1 else "여성"

    # 만족도 복원 (Satisfaction_Per_Order * (OrderCount+1) 역산)
    def get_sat(row):
        mof = row.get("MonthlyOrderFreq", 1)
        spo = row.get("Satisfaction_Per_Order", 0.5)
        # 대략적 주문 수 역산
        approx_order = max(1, round(mof))
        raw_sat = spo * (approx_order + 1)
        return max(1, min(5, round(raw_sat)))

    customers = []
    for i, row in df.iterrows():
        # CustomerID
        cid = row.get("CustomerID", f"C{str(i+1).zfill(4)}")

        # 이탈 확률
        prob_raw = row.get("Churn_Prob", 0.5)
        prob_pct = int(round(prob_raw * 100))

        # 위험도 레이블 (RiskLevel 컬럼 우선, 없으면 계산)
        if "RiskLevel" in df.columns:
            label = row["RiskLevel"]
        else:
            if prob_raw < 0.2:   label = "안전"
            elif prob_raw < 0.5: label = "관심"
            elif prob_raw < 0.8: label = "주의"
            elif prob_raw < 0.95:label = "위험"
            else:                label = "고위험"

        style = risk_style.get(label, risk_style["관심"])

        # 세그먼트 (CustomerGrade 컬럼 우선)
        if "CustomerGrade" in df.columns:
            segment = row["CustomerGrade"]
        else:
            segment = "Active"

        # 경과일: Tenure_log → e^x 개월 → *30 일수
        tenure_months = np.expm1(row.get("Tenure_log", 1))
        day_str = f"{max(1, int(tenure_months * 30))}일"

        # 주문 수: MonthlyOrderFreq * tenure_months 근사
        order_count = max(1, int(round(row.get("MonthlyOrderFreq", 0.1) * max(1, tenure_months))))
        count_str = f"{order_count}회"

        # 금액: CashbackPerOrder * order_count * 5 (캐시백 약 20% 가정)
        cashback_per = row.get("CashbackPerOrder", 0)
        approx_amount = cashback_per * order_count * 5
        amount_str = f"${int(approx_amount):,}"
        cashback_str = f"${int(cashback_per * order_count):,}"

        # 성별
        gender = get_gender(row)

        # 만족도
        sat = get_sat(row)

        # 불만사항 Top2
        reason1, reason2 = get_top_reasons(row)

        customers.append({
            "id":       cid,
            "prob":     prob_pct,
            "label":    label,
            "dot":      style["dot"],
            "color":    style["color"],
            "bg":       style["bg"],
            "segment":  segment,
            "day":      day_str,
            "count":    count_str,
            "amount":   amount_str,
            "gender":   gender,
            "cashback": cashback_str,
            "sat":      sat,
            "reason1":  reason1,
            "reason2":  reason2,
            # 원본 피처도 보관 (상세 정보 확장용)
            "dormancy_shock":       round(row.get("Dormancy_Shock", 0), 2),
            "monthly_order_freq":   round(row.get("MonthlyOrderFreq", 0), 2),
            "cashback_per_order":   round(row.get("CashbackPerOrder", 0), 2),
            "satisfaction_per_order": round(row.get("Satisfaction_Per_Order", 0), 2),
            "churn_actual":         int(row.get("Churn_Actual", row.get("Churn", -1))),
        })

    return customers


# ── 세션 초기화 ──────────────────────────────────────────────────────────
CSV_PATH = "data/customer_list.csv"   # ← 실제 경로로 변경하세요

if "customers" not in st.session_state:
    try:
        st.session_state.customers = load_customers(CSV_PATH)
    except FileNotFoundError:
        st.error(f"⚠️ '{CSV_PATH}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
        st.stop()

if "check_states" not in st.session_state:
    st.session_state.check_states = {c['id']: False for c in st.session_state.customers}

if "selected_id" not in st.session_state:
    st.session_state.selected_id = st.session_state.customers[0]['id']

# ── 콜백 함수 ────────────────────────────────────────────────────────────
def update_all_checks(tab_name, display_ids):
    master_val = st.session_state[f"master_{tab_name}"]
    for cid in display_ids:
        st.session_state.check_states[cid] = master_val
        st.session_state[f"chk_{tab_name}_{cid}"] = master_val

def update_single_check(cid, tab_name):
    st.session_state.check_states[cid] = st.session_state[f"chk_{tab_name}_{cid}"]

def set_selected_customer(cid):
    st.session_state.selected_id = cid

# ── 사이드바 ─────────────────────────────────────────────────────────────
try:
    from components.sidebar import render_sidebar
    render_sidebar("고객 이탈 관리")
except ImportError:
    pass

# ── CSS ──────────────────────────────────────────────────────────────────
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
    button[kind="primary"]:hover {
        background-color: #3D5A80 !important; border-color: #3D5A80 !important; color: white !important;
    }
    h1, h2, h3, b, strong { font-family: var(--font-inter) !important; font-weight: 700; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .main .block-container { padding-top: 2rem !important; padding-left: 280px !important; padding-right: 40px !important; max-width: 1500px !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    [data-testid="stSidebar"] { min-width: 260px !important; max-width: 260px !important; }
    .kpi-card { background: white; padding: 24px; border-radius: 16px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    .kpi-val { font-size: 28px; font-weight: 800; color: #1E293B; margin-top: 10px; margin-bottom: 2px; }
    .p-bar-bg { background: #F1F5F9; height: 6px; border-radius: 10px; width: 50px; display: inline-block; margin-right: 10px; overflow: hidden; }
    .p-bar-fill { height: 100%; border-radius: 10px; }
    .badge { padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; }
    .detail-item { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #F1F5F9; font-size: 13px; color: #475569; }
    </style>
""", unsafe_allow_html=True)

# ── KPI 계산 ─────────────────────────────────────────────────────────────
all_customers   = st.session_state.customers
total_cnt       = len(all_customers)
actual_churn    = sum(1 for c in all_customers if c["churn_actual"] == 1)
predicted_churn = sum(1 for c in all_customers if c["prob"] >= 50)
actual_rate     = actual_churn / total_cnt * 100 if total_cnt > 0 else 0
pred_rate       = predicted_churn / total_cnt * 100 if total_cnt > 0 else 0

# ── 헤더 ─────────────────────────────────────────────────────────────────
st.markdown('<h1 style="font-size:24px; font-weight:800; color:#1E293B; margin-bottom:4px;">고객 이탈 관리</h1>', unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; font-size:14px; margin-bottom:25px;'>이탈 위험 고객을 분류하고 캠페인을 실행하세요</p>", unsafe_allow_html=True)

# ── KPI 카드 ─────────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="kpi-card"><div style="background:#EEF2F8;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">👥</div><div class="kpi-val">{total_cnt:,}</div><div style="font-size:13px;font-weight:600;color:#334155;">전체 고객 수</div><div style="font-size:12px;color:#94A3B8;">등록 고객 전체</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kpi-card"><div style="background:#FDEAEA;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">⚠️</div><div class="kpi-val" style="color:#D97A7A;">{actual_rate:.2f}%</div><div style="font-size:13px;font-weight:600;color:#334155;">실제 이탈 확률</div><div style="font-size:12px;color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="kpi-card"><div style="background:#FDF1E3;width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">📉</div><div class="kpi-val" style="color:#E6A050;">{pred_rate:.2f}%</div><div style="font-size:13px;font-weight:600;color:#334155;">예측 이탈 확률</div><div style="font-size:12px;color:#94A3B8;">전체 고객 대비</div></div>', unsafe_allow_html=True)

st.write("")

# ── 메인 레이아웃 ─────────────────────────────────────────────────────────
m_left, m_right = st.columns([2.6, 1])
selected_count = sum(st.session_state.check_states.values())

# 탭별 필터 기준 (label 값 기준)
TAB_FILTER = {
    "전체":   None,
    "안전":   "안전",
    "양호":   "관심",   # 관심 → 양호 탭으로 표시
    "주의":   "주의",
    "위험":   "위험",
    "고위험": "고위험",
}

with m_left:
    with st.container(border=True):
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:10px;margin-bottom:5px;'>"
            f"<b style='font-size:16px;'>고객 리스트</b>"
            f"<span style='font-size:12px;color:#94A3B8;'>{total_cnt:,}명 표시 · <b style='color:#3B82F6;'>{selected_count}명 선택됨</b></span>"
            f"</div>",
            unsafe_allow_html=True
        )

        tab_titles = list(TAB_FILTER.keys())
        tabs = st.tabs(tab_titles)

        for idx, tab in enumerate(tabs):
            with tab:
                curr_tab_name = tab_titles[idx]
                filter_label  = TAB_FILTER[curr_tab_name]

                # 필터링
                if filter_label is None:
                    display_list = all_customers
                else:
                    display_list = [c for c in all_customers if c['label'] == filter_label]

                if not display_list:
                    st.info(f"'{curr_tab_name}' 등급의 고객이 없습니다.")
                    continue

                display_ids  = [c['id'] for c in display_list]
                all_checked  = all(st.session_state.check_states.get(cid, False) for cid in display_ids)
                st.session_state[f"master_{curr_tab_name}"] = all_checked

                st.write("")
                # 헤더
                h1, h2, h3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                with h1:
                    st.checkbox("전체", key=f"master_{curr_tab_name}", on_change=update_all_checks,
                                args=(curr_tab_name, display_ids), label_visibility="collapsed")
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
                            <div style="flex:1.5;text-align:right;">금액</div>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("<hr style='margin:5px 0 10px 0;'>", unsafe_allow_html=True)

                # 바디
                for c in display_list:
                    chk_key = f"chk_{curr_tab_name}_{c['id']}"
                    st.session_state[chk_key] = st.session_state.check_states.get(c['id'], False)
                    is_chk   = st.session_state[chk_key]
                    bg_color = "#F0F7FF" if is_chk else "#FFFFFF"

                    r1, r2, r3 = st.columns([0.05, 0.12, 0.83], vertical_alignment="center")
                    with r1:
                        st.checkbox("개별", key=chk_key, on_change=update_single_check,
                                    args=(c['id'], curr_tab_name), label_visibility="collapsed")
                    with r2:
                        st.button(c['id'], key=f"btn_{curr_tab_name}_{c['id']}",
                                  on_click=set_selected_customer, args=(c['id'],),
                                  use_container_width=True)
                    with r3:
                        st.markdown(f"""
                            <div style="background-color:{bg_color};border-radius:8px;padding:10px 15px;display:flex;align-items:center;transition:0.2s;border:1px solid #F1F5F9;">
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


with m_right:
    # 고객 상세 정보
    with st.container(border=True):
        st.markdown("<b style='font-size:15px;color:#1E293B;'>고객 상세 정보</b>", unsafe_allow_html=True)

        curr = next((c for c in all_customers if c['id'] == st.session_state.selected_id), all_customers[0])

        default_theme = ("분석할 수 없는 데이터", "#F8FAFC", "#E2E8F0", "#475569")
        comp1_text, comp1_bg, comp1_border, comp1_color = COMPLAINT_MAP.get(curr.get('reason1', ''), default_theme)
        comp2_text, comp2_bg, comp2_border, comp2_color = COMPLAINT_MAP.get(curr.get('reason2', ''), default_theme)

        st.markdown(f"""
            <div style="display:flex;align-items:center;gap:16px;margin:24px 0 30px 0;">
                <div style="width:54px;height:54px;border-radius:50%;background:{curr['bg']};color:{curr['color']};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;">{curr['id']}</div>
                <div>
                    <div style="font-size:18px;font-weight:800;color:#1E293B;margin-bottom:4px;">{curr['id']}</div>
                    <div class="badge" style="background:{curr['bg']};color:{curr['color']};">{curr['label']} · {curr['prob']}%</div>
                </div>
            </div>
            <div class="detail-item"><span>👤 성별</span><b style="color:#1E293B;">{curr['gender']}</b></div>
            <div class="detail-item"><span>📅 경과일</span><b style="color:#1E293B;">{curr['day']}</b></div>
            <div class="detail-item"><span>🛒 주문 횟수</span><b style="color:#1E293B;">{curr['count']}</b></div>
            <div class="detail-item"><span>💵 캐시백</span><b style="color:#1E293B;">{curr['cashback']}</b></div>
            <div class="detail-item"><span>📦 공백기 충격도</span><b style="color:#1E293B;">{curr['dormancy_shock']}</b></div>
            <div class="detail-item"><span>🛍️ 월 주문 빈도</span><b style="color:#1E293B;">{curr['monthly_order_freq']}</b></div>
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
        st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
                <b style='font-size:15px;color:#1E293B;'>⚡ 맞춤형 액션 추천</b>
                <span style='font-size:11px;color:#94A3B8;'>최대 2개 선택</span>
            </div>
        """, unsafe_allow_html=True)

        status_color = "#3B82F6" if selected_count > 0 else "#94A3B8"
        bg_col       = "#EFF6FF" if selected_count > 0 else "#F8FAFC"
        border_col   = "#BFDBFE" if selected_count > 0 else "#E2E8F0"

        st.markdown(f"""
            <div style='background:{bg_col};color:{status_color};padding:14px;border-radius:8px;font-size:13px;font-weight:600;margin:15px 0;border:1px solid {border_col};display:flex;align-items:center;gap:8px;'>
                <span>👥</span> {selected_count}명 선택됨 <span style='font-weight:400;color:#94A3B8;font-size:11px;margin-left:auto;'>· 캠페인 대상을 확인하세요</span>
            </div>
        """, unsafe_allow_html=True)

        default_actions = ["10% 할인 쿠폰 발급", "무료 배송권 발송"]
        suggested_actions = []

        if selected_count == 0:
            suggested_actions = (
                ACTION_MAP.get(curr.get('reason1', ''), default_actions) +
                ACTION_MAP.get(curr.get('reason2', ''), default_actions)
            )
        else:
            selected_customers = [c for c in all_customers if st.session_state.check_states.get(c['id'], False)]
            all_reasons = []
            for c in selected_customers:
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
