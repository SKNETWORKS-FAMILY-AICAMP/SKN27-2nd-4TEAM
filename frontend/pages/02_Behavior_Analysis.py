import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.io as pio
from components.sidebar import render_sidebar

# 1. 페이지 설정
st.set_page_config(page_title="Re:tain - 행동 분석", layout="wide")

# 2. 사이드바 호출 (고정형 레이아웃 적용)
render_sidebar("행동 분석")

# 3. 전역 배경색 설정
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
    .stApp { background-color: #F8FAFC; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* 메인 화면 가려짐 방지 */
    .block-container { 
        padding-top: 2rem !important; 
        padding-left: 100px !important; 
        padding-right: 40px !important;
        max-width: 1800px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. 차트 생성용 헬퍼 함수
def get_chart_part(labels, values, colors, height=220):
    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=.65,
        marker=dict(colors=colors, line=dict(color='white', width=3)),
        opacity=0.85,
        textinfo='none'
    )])
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        height=height, showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    )
    return pio.to_html(fig, full_html=False, config={'displayModeBar': False})

# --- 메인 화면 렌더링 ---

st.markdown('<h1 style="font-size: 24px; font-weight: 800; color: #1E293B; margin-left: 10px;">고객 행동 분석</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 14px; color: #64748B; margin-bottom: 30px; margin-left: 10px;">RFM 세그먼트, 위험도 분포, 이탈 패턴을 분석합니다</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# [상단 카드 1] RFM 세그먼트
with col1:
    # 변경 후
    labels, values, colors = ['VIP', 'Platinum', 'Gold', 'Silver', 'Risk'], [2.66, 73.27, 5.68, 3.91, 14.48], ['#F6C23E', '#4A6FA5', '#E6A050', '#7FB77E', '#D97A7A']
    chart_html = get_chart_part(labels, values, colors)
    
    rfm_html = f"""
    <div style="background: white; border-radius: 16px; border: 1px solid #E2E8F0; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); font-family: 'Inter', sans-serif; min-height: 380px; margin-left: 10px;">
        <div style="font-size: 16px; font-weight: 700; color: #1E293B; margin-bottom: 2px;">고객 등급 세그먼트</div>
        <div style="font-size: 12px; color: #94A3B8; margin-bottom: 30px;">VIP · Platinum · Gold · Silver · Risk 비율</div>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="width: 100%;">{chart_html}</div>
            <div style="display: flex; gap: 16px; margin-top: 20px;">
                {''.join([f'<div style="font-size:11px; color:#64748B;"><span style="color:{c};">●</span> {l}</div>' for l, c in zip(labels, colors)])}
            </div>
        </div>
    </div>
    """
    components.html(rfm_html, height=420)

# [상단 카드 2] 위험도 분포
with col2:
    risk_data = [
        {"name": "안전", "val": 75.93, "color": "#4A6FA5"}, {"name": "양호", "val": 5.68, "color": "#7FB77E"},
        {"name": "주의", "val": 3.91, "color": "#E6C97A"}, {"name": "위험", "val": 6.04, "color": "#E09873"}, {"name": "고위험", "val": 8.44, "color": "#B85C5C"},
    ]
    risk_chart = get_chart_part([d['name'] for d in risk_data], [d['val'] for d in risk_data], [d['color'] for d in risk_data])
    
    risk_bars = "".join([f"""
        <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
                <span style="color: #475569;">{d['name']}</span>
                <span style="font-weight: 700; color: {d['color']};">{d['val']}%</span>
            </div>
            <div style="width: 100%; height: 6px; background: #F1F5F9; border-radius: 10px;">
                <div style="width: {d['val']}%; height: 100%; background: {d['color']}; border-radius: 10px;"></div>
            </div>
        </div>
    """ for d in risk_data])

    risk_html = f"""
    <div style="background: white; border-radius: 16px; border: 1px solid #E2E8F0; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); font-family: 'Inter', sans-serif; min-height: 380px; margin-right: 10px;">
        <div style="font-size: 16px; font-weight: 700; color: #1E293B; margin-bottom: 2px;">위험도 분포 (5단계)</div>
        <div style="font-size: 12px; color: #94A3B8; margin-bottom: 30px;">전체 고객의 이탈 위험 구간 분포</div>
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">
            <div style="flex: 0.9; display: flex; flex-direction: column; align-items: center; min-width: 180px;">
                <div style="flex: 1; display: flex; justify-content: center; align-items: center; overflow: hidden;">{risk_chart}</div>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 5px;">
                    {''.join([f'<div style="font-size:10px; color:#64748B;"><span style="color:{d["color"]};">●</span> {d["name"]}</div>' for d in risk_data])}
                </div>
            </div>
            <div style="flex: 1.1; min-width: 180px;">
                {risk_bars}
            </div>
        </div>
    </div>
    """
    components.html(risk_html, height=420)


st.write("")

# -------------------------------------------------------------------
# [하단 카드 1] 🤖 AI 예측 긍정 행동 패턴 Top 5 (한 줄 전체 차지)
# -------------------------------------------------------------------
features_positive = [
    {"title": "1위: 강력한 리워드 락인 (Cashback)", "desc": "주문당 캐시백 혜택을 많이 받는 고객일수록 모델이 이탈하지 않을 것으로 강하게 예측합니다.", "stat": "유지 강세", "color": "#5FAD56", "bg": "#EDF7EC", "icon": "🎁"},
    {"title": "2위: 모바일 앱 중심 이용 (Mobile Login)", "desc": "모바일 기기(Mobile Phone)를 주로 사용하는 고객은 접근성이 높아 자연스러운 잔존율 상승으로 이어집니다.", "stat": "접근성 향상", "color": "#4A6FA5", "bg": "#EEF2F8", "icon": "📱"},
    {"title": "3위: 특정 카테고리 충성도 (Laptop & Accessory)", "desc": "노트북 등 전자기기를 주로 구매하는 고객층은 타 카테고리 대비 압도적으로 이탈 확률이 낮습니다.", "stat": "VIP 징후", "color": "#8B5CF6", "bg": "#F3E8FF", "icon": "💻"},
    {"title": "4위: 장기 충성도 형성 (Tenure)", "desc": "가입 기간이 길어질수록 이탈 확률을 크게 낮추는 효과가 발생하여 탄탄한 우수 고객층으로 자리 잡습니다.", "stat": "충성도 고착", "color": "#10B981", "bg": "#D1FAE5", "icon": "📈"},
    {"title": "5위: 촘촘한 최근 활동 (Recency Ratio)", "desc": "가입 기간 대비 최근 구매 간격이 짧고 꾸준히 상호작용(Recency)할수록 가장 안정적인 유지 패턴을 보입니다.", "stat": "안정적 유지", "color": "#06B6D4", "bg": "#CFFAFE", "icon": "🔄"}
]

features_content_pos = "".join([f"""
    <div style="background-color: {f['bg']}; padding: 18px 24px; border-radius: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 20px; border: 1px solid rgba(0,0,0,0.02);">
        <div style="background: white; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.06); font-size: 20px; flex-shrink: 0;">{f['icon']}</div>
        <div style="flex-grow: 1;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 14px; font-weight: 700; color: #334155;">{f['title']}</span>
                <span style="font-size: 13px; font-weight: 800; color: {f['color']};">{f['stat']}</span>
            </div>
            <p style="font-size: 12px; color: #64748B; margin-top: 4px; margin-bottom: 0; line-height: 1.5;">{f['desc']}</p>
        </div>
    </div>
""" for f in features_positive])

churn_html_pos = f"""
<div style="background: white; border-radius: 16px; border: 1px solid #E2E8F0; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); font-family: 'Inter', sans-serif; margin-left: 10px; margin-right: 10px;">
    <div style="font-size: 16px; font-weight: 700; color: #1E293B; margin-bottom: 2px;">🤖 AI 예측 긍정 행동 패턴 Top 5</div>
    <div style="font-size: 12px; color: #94A3B8; margin-bottom: 24px;">이탈 확률을 낮추고 잔존율을 높이는 고객의 핵심 특징</div>
    <div style="display: flex; flex-direction: column;">
        {features_content_pos}
    </div>
</div>
"""
components.html(churn_html_pos, height=580)

st.write("")

# -------------------------------------------------------------------
# [하단 카드 2] 🚨 주요 이탈 위험 요인 Top 5 (한 줄 전체 차지)
# -------------------------------------------------------------------
features_risk = [
    {"title": "1위: 잦은 이슈 및 불만 경험 (IssueIndex)", "desc": "고객이 겪은 서비스 문제나 CS 이슈가 많을수록 AI 모델이 이탈 확률을 가장 가파르게 상승시킵니다.", "stat": "초고위험", "color": "#D97A7A", "bg": "#FDEAEA", "icon": "⚠️"},
    {"title": "2위: 짧은 유지 기간 (Tenure_log)", "desc": "가입 기간이 짧은 신규 고객일수록 이탈 위험이 매우 높게 나타납니다. 초기 온보딩(Onboarding)의 중요성을 시사합니다.", "stat": "고위험", "color": "#C45A5A", "bg": "#FEE2E2", "icon": "⏳"},
    {"title": "3위: 과도한 단기 주문 빈도 (MonthlyOrderFreq)", "desc": "월 주문 빈도가 극도로 높은 소수 고객군에서 목적 달성(체리피킹 등) 후 단기 이탈하는 어뷰징 위험이 감지됩니다.", "stat": "어뷰징 의심", "color": "#E6A050", "bg": "#FDF1E3", "icon": "📦"},
    {"title": "4위: 잦은 배송지 변경 (NumberOfAddress)", "desc": "등록된 주소지가 많고 행동 패턴이 복잡한 고객군에서 특정 이탈 징후 및 체리피킹 리스크가 감지됩니다.", "stat": "위험", "color": "#F59E0B", "bg": "#FEF3C7", "icon": "🏠"},
    {"title": "5위: 1인 가구 특성 (Single & CityTier)", "desc": "미혼이거나 대도시에 거주하는 고객군에서 상대적으로 특정 제품에 정착하지 못하고 환승 이탈하는 비율이 높습니다.", "stat": "주의 필요", "color": "#F97316", "bg": "#FFEDD5", "icon": "👤"}
]

features_content_risk = "".join([f"""
    <div style="background-color: {f['bg']}; padding: 18px 24px; border-radius: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 20px; border: 1px solid rgba(0,0,0,0.02);">
        <div style="background: white; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.06); font-size: 20px; flex-shrink: 0;">{f['icon']}</div>
        <div style="flex-grow: 1;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 14px; font-weight: 700; color: #334155;">{f['title']}</span>
                <span style="font-size: 13px; font-weight: 800; color: {f['color']};">{f['stat']}</span>
            </div>
            <p style="font-size: 12px; color: #64748B; margin-top: 4px; margin-bottom: 0; line-height: 1.5;">{f['desc']}</p>
        </div>
    </div>
""" for f in features_risk])

churn_html_risk = f"""
<div style="background: white; border-radius: 16px; border: 1px solid #E2E8F0; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); font-family: 'Inter', sans-serif; margin-left: 10px; margin-right: 10px;">
    <div style="font-size: 16px; font-weight: 700; color: #D97A7A; margin-bottom: 2px;">🚨 주요 이탈 위험 요인 Top 5</div>
    <div style="font-size: 12px; color: #94A3B8; margin-bottom: 24px;">머신러닝(SHAP) 분석 기반 가장 강력한 이탈 신호</div>
    <div style="display: flex; flex-direction: column;">
        {features_content_risk}
    </div>
</div>
"""
components.html(churn_html_risk, height=580)