import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from components.sidebar import render_sidebar

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Re:tain | 소비 트렌드", layout="wide", initial_sidebar_state="expanded")

# --- 2. 사이드바 호출 ---
render_sidebar("소비 트렌드")

# --- 3. 전역 스타일 ---
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
            
    [data-testid="stSidebar"] {
        min-width: 260px !important;
        max-width: 260px !important;
    }

    /* 4. 기존 스타일 유지 */
    .react-card-container {
        font-family: var(--font-inter);
        background: white;
    }
    
    /* 제목이나 굵은 글씨에도 확실히 적용 */
    h1, h2, h3, b, strong {
        font-family: var(--font-inter) !important;
        font-weight: 700;
    }   
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    .block-container { 
        background-color: #FFFFFF !important;
        padding-top: 2rem !important; 
        padding-left: 100px !important; 
        padding-right: 40px !important;
        max-width: 1400px !important;
    }
    
    .insight-card {
        background-color: #FFFFFF !important;
        padding: 20px; border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        border: 2px solid #E2E8F0 !important;
        height: 100%;
    }
    
    div[data-testid="stSelectbox"] { margin-top: 5px; margin-bottom: 0px; }
    div[data-testid="stSelectbox"] > div > div { min-height: 38px; padding-top: 2px; padding-bottom: 2px; border-radius: 8px;}

    .title-tooltip { position: relative; display: inline-block; cursor: help; }
    .title-tooltip .tooltip-text {
        visibility: hidden; width: 340px; background-color: #1E293B; color: #F8FAFC;
        text-align: left; border-radius: 8px; padding: 14px; position: absolute;
        z-index: 9999; bottom: 140%; left: 0; opacity: 0;
        transition: opacity 0.2s, bottom 0.2s; font-size: 12px; line-height: 1.6; font-weight: 400;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .title-tooltip .tooltip-text::after {
        content: ""; position: absolute; top: 100%; left: 20px;
        border-width: 6px; border-style: solid; border-color: #1E293B transparent transparent transparent;
    }
    .title-tooltip:hover .tooltip-text { visibility: visible; opacity: 1; bottom: 120%; }
    </style>
""", unsafe_allow_html=True)

# --- 4. 데이터 로드 (월별 시계열) ---
yearly_bases = {
    2020: (159, 69.0, 89.2), 2021: (190, 71.5, 102.5), 2022: (209, 73.2, 95.4),
    2023: (228, 74.8, 92.1), 2024: (245, 76.1, 98.5),  2025: (260, 77.5, 104.2), 2026: (275, 78.2, 106.8)
}
seasonality = [0.92, 0.90, 0.95, 0.98, 1.02, 1.00, 1.01, 0.98, 1.05, 1.03, 1.08, 1.10]

MAJOR_EVENTS = {
    "2020-03": "🚨 <b>이슈: 코로나19 팬데믹 본격화</b><br>👉 오프라인 급감 및 소비심리 최저",
    "2021-11": "📈 <b>이슈: 코로나 보복 소비 확산</b><br>👉 온라인 거래액 및 심리지수 회복",
    "2022-07": "📉 <b>이슈: 고물가·고금리 3고 시대</b><br>👉 소비심리 100 붕괴 (소비 위축)",
    "2023-10": "🏷️ <b>이슈: 가성비/C커머스 플랫폼 급부상</b><br>👉 할인 혜택 의존도 극대화"
}

records = []
for y, (amt, mob, ccsi) in yearly_bases.items():
    for month in range(1, 13):
        date_key = f"{y}-{month:02d}"
        event_raw = MAJOR_EVENTS.get(date_key, "")
        event_text = f"<br><br>━━━━━━━━━━━━<br>{event_raw}" if event_raw else ""
        records.append({
            "year": y, "date_full": date_key, "month_label": f"{month}월",
            "amount": round(amt * seasonality[month-1], 1),
            "mobile": round(mob + (month - 6) * 0.1, 1),
            "ccsi": round(ccsi + (month % 4 - 1.5) * 1.2, 1),
            "event": event_text
        })
df_trend = pd.DataFrame(records)

# 🚨 이미지 수치 반영: 이탈 vs 유지 고객 데이터 업데이트
df_churn = pd.DataFrame({
    "metric": ["작년 대비 주문량", "월평균 주문 빈도", "주문당 캐시백", "쿠폰 민감도"],
    "churn": [15.51, 7.07, 51.97, 1.16],  # 이미지의 '이탈 고객' 수치
    "retain": [15.61, 1.12, 54.59, 0.96]   # 이미지의 '유지 고객' 수치
})

# 수치에 따른 세부 해석 텍스트
churn_explanations = {
    "작년 대비 주문량": "전년 대비 구매 증감폭은 이탈군과 유지군이 비슷하게 나타납니다.",
    "월평균 주문 빈도": "이탈 고객군에서 비정상적으로 높은 주문 빈도가 관찰됩니다. (체리피킹/어뷰징 의심)",
    "주문당 캐시백": "유지 고객군이 더 높은 캐시백 혜택을 받고 있어 락인 효과가 증명됩니다.",
    "쿠폰 민감도": "이탈 고객의 쿠폰 민감도가 더 높습니다. 즉, 할인 혜택이 없으면 쉽게 떠날 가능성이 큰 집단입니다."
}

def get_filtered_data(df, selected_year_str):
    if selected_year_str == "전체 기간 (2020~2026)":
        return df, "date_full"
    target_year = int(selected_year_str[:4])
    return df[df["year"] == target_year], "month_label"

# --- 5. 타이틀 & 마스터 필터 ---
year_options = ["전체 기간 (2020~2026)", "2026년", "2025년", "2024년", "2023년", "2022년", "2021년", "2020년"]

head_col1, head_col2 = st.columns([4, 1])
with head_col1:
    st.markdown("<h1 style='font-size: 24px; font-weight: 800; color: #1E293B; margin-bottom: 4px;'>소비 트렌드 분석</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size: 14px; margin-bottom: 24px;'>거시적 트렌드 변화가 고객 지표에 미치는 영향</p>", unsafe_allow_html=True)
with head_col2:
    global_year_filter = st.selectbox("기간 설정", year_options, label_visibility="collapsed")

# --- 6. 상단 핵심 인사이트 배치 ---
insight_dict = {
    "전체 기간 (2020~2026)": [
        ("#D97A7A", "🌍 거시 흐름 (Macro)", "팬데믹(2020) → 보복소비(2021) → 고물가 위축(2022~2024) → 점진적 회복(2025~)의 다이나믹한 소비 사이클을 겪었습니다."),
        ("#E6A050", "🛒 소비 패턴 (Pattern)", "거시 경제가 악화된 시기일수록 구매 빈도(OrderCount)가 감소하고 쿠폰 의존도(CouponUsed)가 급증하는 '가성비 추구 현상'이 뚜렷했습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "데이터 분석 결과, 캐시백과 리워드 혜택 체감이 낮아질 때 고객 이탈률이 가장 가파르게 상승(이탈 160원 vs 유지 180원)했습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "모바일 비중이 78%에 달하는 현재, 단순 할인 쿠폰 살포보다는 VIP 등급 혜택 강화와 개인화된 앱 푸시 알림(Lock-in)이 필수적입니다.")
    ],
    "2020년": [
        ("#D97A7A", "🌍 팬데믹 쇼크 (Macro)", "코로나19 발발로 오프라인 활동이 마비되며 CCSI(소비자심리지수)가 89.2로 역대 최저치를 기록하며 소비가 꽁꽁 얼어붙었습니다."),
        ("#E6A050", "🛒 비대면 일상화 (Pattern)", "반사 이익으로 온라인 거래액이 159조원을 돌파했고, 모바일 쇼핑 비중이 69%를 넘어서며 '디지털 전환'이 강제로 가속화되었습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "갑작스러운 트래픽 폭증으로 배송 지연 및 품절이 잦아지며, 초기 서비스 경험(Satisfaction) 불만족이 이탈의 주원인이었습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "비대면 소비로 처음 유입된 중장년층 고객이 플랫폼에 안착할 수 있도록 UI/UX 편의성을 개선하고 직관적인 혜택을 제공해야 합니다.")
    ],
    "2021년": [
        ("#D97A7A", "🌍 보복 소비 폭발 (Macro)", "백신 접종 및 일상 회복 기대감으로 CCSI가 102.5로 기준선(100)을 돌파하며 억눌렸던 소비 심리가 무섭게 분출되었습니다."),
        ("#E6A050", "🛒 거래액 퀀텀 점프 (Pattern)", "온라인 거래액이 190조원으로 전년 대비 폭발적(+19%)으로 성장했으며, 특히 패션/여행 카테고리의 반등이 돋보였습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "풍부한 유동성 덕분에 구매 빈도(OrderCount)가 전반적으로 높아져 타 연도 대비 고객 이탈 방어가 비교적 수월했습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "지갑이 열린 이 시기에 객단가(AOV)를 높일 수 있는 프리미엄 상품 제안 및 크로스셀링(Cross-selling) 캠페인을 집중해야 합니다.")
    ],
    "2022년": [
        ("#D97A7A", "🌍 3고 현상 본격화 (Macro)", "하반기부터 시작된 고물가·고금리·고환율 쇼크로 인해 CCSI가 다시 95.4로 추락하며 기나긴 소비 한파가 시작되었습니다."),
        ("#E6A050", "🛒 구매 주기 지연 (Pattern)", "실질 소득 감소로 인해 고객들의 지갑이 얇아지면서 재구매 주기(DaySinceLastOrder)가 급격히 길어지기 시작했습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "고객들이 가격 비교에 민감해지면서, 조금이라도 더 저렴한 경쟁사 플랫폼으로 갈아타는 '플랫폼 환승 이탈'이 증가했습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "이탈 징후(방문 간격 길어짐)가 감지된 고객을 타겟팅하여, 시기적절(Right-time)하게 컴백 유도 쿠폰과 알림을 발송해야 합니다.")
    ],
    "2023년": [
        ("#D97A7A", "🌍 소비 한파 지속 (Macro)", "CCSI 92.1로 바닥권을 다지며, C커머스(중국 직구) 등 초저가 플랫폼의 국내 상륙으로 이커머스 생태계 교란이 일어났습니다."),
        ("#E6A050", "🛒 체리피커 양산 (Pattern)", "할인 쿠폰 없이는 절대 구매하지 않는 극단적 '가성비 추구' 및 '체리피커' 성향의 소비 패턴이 완전히 고착화되었습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "단순한 10% 쿠폰 발급만으로는 고객의 마음을 돌릴 수 없을 정도로 쿠폰(CouponUsed)에 대한 역치와 피로도가 높아졌습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "출혈적인 할인 경쟁을 멈추고, 충성 고객에게만 파격적인 리워드(Cashback)를 제공하는 '구독형 멤버십' 도입이 시급합니다.")
    ],
    "2024년": [
        ("#D97A7A", "🌍 소비 양극화 (Macro)", "CCSI 98.5로 더딘 회복세를 보이며, 초고가 명품 아니면 초저가 생필품만 팔리는 '소비 양극화' 현상이 뚜렷하게 나타났습니다."),
        ("#E6A050", "🛒 모바일 지배력 (Pattern)", "모바일 결제 비중이 76.1%를 차지하며, PC 웹 쇼핑은 사실상 탐색 보조 수단으로 전락했습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "혜택을 200% 활용하는 체리피커 VIP는 잔류하는 반면, 일반(Active) 고객층은 무관심 속에 소리 없이 이탈하는 양상을 보였습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "수많은 상품 중 고객이 원하는 것만 골라주는 'AI 개인화 추천 시스템'을 고도화하여 탐색 피로도를 줄여주어야 합니다.")
    ],
    "2025년": [
        ("#D97A7A", "🌍 심리 해빙기 (Macro)", "금리 인하 기조와 경제 안정화 기대감으로 CCSI가 마침내 100을 돌파(104.2)하며 억눌렸던 소비가 점진적으로 기지개를 켰습니다."),
        ("#E6A050", "🛒 질적 성장 전환 (Pattern)", "거래액은 260조원으로 무난히 성장했으며, 단순한 최저가 경쟁에서 벗어나 '빠른 배송'과 '경험' 중심의 소비로 패턴이 이동했습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "이 시기의 이탈 고객은 가격 불만보다 CS(고객 응대) 지연이나 반품 불편 등 서비스 품질(Satisfaction) 불만이 주원인이었습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "리뷰와 VOC(고객의 소리) 데이터를 실시간 분석하여 서비스의 마찰(Friction) 구간을 선제적으로 제거하는 CRM이 핵심입니다.")
    ],
    "2026년": [
        ("#D97A7A", "🌍 완전한 성숙기 (Macro)", "거래액 275조원, CCSI 106.8로 시장이 완전히 성숙기에 접어들었으며, 이커머스 업체 간 '제로섬(파이 뺏기) 게임'이 치열해졌습니다."),
        ("#E6A050", "🛒 모바일 온리 (Pattern)", "모바일 비중 78.2%. 결제부터 환불까지 스마트폰 하나로 완벽한 쇼핑 여정이 이루어지는 '모바일 온리' 시대가 정착되었습니다."),
        ("#5FAD56", "🚨 이탈 시그널 (Churn)", "신규 고객 유치 비용(CAC)이 기하급수적으로 높아져, 기존 고객 한 명이 이탈할 때마다 플랫폼이 입는 재무적 타격이 극대화되었습니다."),
        ("#4A6FA5", "🎯 대응 전략 (Strategy)", "데이터 기반의 'Re:tain 이탈 예측 솔루션'을 전면 도입하여, 고객이 떠나기 2주 전에 선제적 맞춤 오퍼를 보내는 자동화가 필요합니다.")
    ]
}
current_insights = insight_dict.get(global_year_filter, insight_dict["전체 기간 (2020~2026)"])

with st.container(border=True):
    st.markdown(f"<p style='font-weight: 700; font-size: 16px; color: #1E293B; margin-bottom: 20px;'>💡 {global_year_filter} 핵심 인사이트 분석</p>", unsafe_allow_html=True)
    i_col1, i_col2 = st.columns(2); i_col3, i_col4 = st.columns(2)
    for col, (color, title, desc) in zip([i_col1, i_col2, i_col3, i_col4], current_insights):
        with col:
            st.markdown(f"""<div class="insight-card" style="border-left: 4px solid {color}; margin-bottom: 15px; min-height: 120px;">
                <p style="margin: 0 0 6px 0; font-size: 13px; font-weight: 800; color: {color};">{title}</p>
                <p style="margin: 0; font-size: 13px; font-weight: 500; color: #334155; line-height: 1.6;">{desc}</p></div>""", unsafe_allow_html=True)

# --- 7. 그래프 영역 ---
df_filtered, x_col = get_filtered_data(df_trend, global_year_filter)

# 차트 1: 온라인 쇼핑 거래액
with st.container(border=True):
    st.markdown("<p style='font-weight: 700; font-size: 15px; color: #1E293B; margin-bottom: 10px;'>온라인 거래액 & 모바일 비중 추이</p>", unsafe_allow_html=True)
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df_filtered[x_col], y=df_filtered['amount'], name='거래액(조원)', fill='tozeroy', line_color='#4A6FA5', yaxis='y1'))
    m_colors = ['#14532D' if e != "" else '#5FAD56' for e in df_filtered['event']]
    m_sizes = [12 if e != "" else 6 for e in df_filtered['event']]
    fig1.add_trace(go.Scatter(x=df_filtered[x_col], y=df_filtered['mobile'], name='모바일(%)', mode='lines+markers', line=dict(color='#5FAD56', width=2), marker=dict(color=m_colors, size=m_sizes, line=dict(color='white', width=1)), customdata=df_filtered['event'], hovertemplate="모바일: %{y:.1f}%%{customdata}<extra></extra>", yaxis='y2'))
    fig1.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0), hovermode="x unified", yaxis=dict(title="거래액(조원)", range=[130, 310]), yaxis2=dict(title="비중(%)", overlaying='y', side='right', range=[65, 80]), legend=dict(orientation="h", y=-0.2), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

# 차트 2: CCSI
st.write("")
with st.container(border=True):
    st.markdown("<p style='font-weight: 700; font-size: 15px; color: #1E293B; margin-bottom: 10px;'>소비자심리지수 (CCSI) 추이</p>", unsafe_allow_html=True)
    fig2 = go.Figure()
    c_colors = ['#7F1D1D' if e != "" else '#D97A7A' for e in df_filtered['event']]
    c_sizes = [12 if e != "" else 6 for e in df_filtered['event']]
    fig2.add_trace(go.Scatter(x=df_filtered[x_col], y=df_filtered['ccsi'], name='CCSI', mode='lines+markers', line=dict(color='#D97A7A', width=3), marker=dict(color=c_colors, size=c_sizes, line=dict(color='white', width=1)), customdata=df_filtered['event'], hovertemplate="CCSI: %{y:.1f}%{customdata}<extra></extra>"))
    fig2.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text="기준선(100)")
    fig2.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0), hovermode="x unified", yaxis=dict(range=[85, 110]), showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

    # st.markdown("<p style='font-weight: 700; font-size: 15px; color: #1E293B; margin-bottom: 10px;'>지표별 이탈 vs 유지 비교 (팀 분석 데이터 반영)</p>", unsafe_allow_html=True)
    
    # fig3 = go.Figure()
    # fig3.add_trace(go.Bar(
    #     name='이탈 고객', x=df_churn['metric'], y=df_churn['churn'], marker_color='#D97A7A',
    #     customdata=[churn_explanations[m] for m in df_churn['metric']],
    #     hovertemplate="<b>%{x} (이탈)</b><br>수치: %{y}<br>💡 %{customdata}<extra></extra>"
    # ))
    # fig3.add_trace(go.Bar(
    #     name='유지 고객', x=df_churn['metric'], y=df_churn['retain'], marker_color='#4A6FA5',
    #     hovertemplate="<b>%{x} (유지)</b><br>수치: %{y}<extra></extra>"
    # ))
    # fig3.update_layout(
    #     barmode='group', height=350, margin=dict(l=0, r=0, t=10, b=0),
    #     legend=dict(orientation="h", y=-0.2), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
    # )
    # st.plotly_chart(fig3, use_container_width=True)