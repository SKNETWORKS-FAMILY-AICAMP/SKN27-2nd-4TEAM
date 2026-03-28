import pandas as pd
import numpy as np
from src.seed import set_seed

def FeatureCreate(df):

    df = df.copy()
    set_seed()

    # 0으로 나누기 방지 (로그 변환된 값이라도 안전하게 처리)
    # 로그 변환된 Tenure는 보통 0 근처일 수 있으므로 주의
    tenure_safe = df['Tenure_log'].replace(0, 0.1) 
    
    # --- 1. 활동성 및 이탈 신호 ---
    # MonthlyOrderFreq: 가입 기간 대비 구매 빈도 (Tenure_log 활용)
    df['MonthlyOrderFreq'] = df['OrderCount'] / tenure_safe
    # InactiveRatio: 가입 기간 중 주문 안 한 기간 비중 (DaySinceLastOrder_clip 활용)
    df['InactiveRatio'] = df['DaySinceLastOrder_clip'] / (np.exp(df['Tenure_log']) * 30)
    # RecentActive: 최근 30일 내 주문 기록 여부
    df['RecentActive'] = (df['DaySinceLastOrder_clip'] < 30).astype(int)
    
    q75_order = df['OrderCount'].quantile(0.75)
    df['HighFreqBuyer'] = (df['OrderCount'] > q75_order).astype(int)
    df['LoyalActive'] = ((df['RecentActive'] == 1) & (df['HighFreqBuyer'] == 1)).astype(int)

    # --- 2. 매출 및 혜택 민감도 ---
    # RoughLTV: CashbackAmount_clip 활용
    df['RoughLTV'] = df['CashbackAmount_clip'] + df['OrderAmountHikeFromlastYear']
    df['CashbackPerOrder'] = df['CashbackAmount_clip'] / (df['OrderCount'] + 1)
    df['CouponPerOrder'] = df['CouponUsed'] / (df['OrderCount'] + 1)
    df['PositiveOrderGrowth'] = (df['OrderAmountHikeFromlastYear'] > 0).astype(int)
    
    df['HeavyCouponUser'] = (df['CouponUsed'] > df['CouponUsed'].quantile(0.75)).astype(int)
    df['HeavyCashbackUser'] = (df['CashbackAmount_clip'] > df['CashbackAmount_clip'].quantile(0.75)).astype(int)

    # --- 3. 서비스 경험 및 리스크 ---
    df['IssueIndex'] = df['Complain'].astype(int)
    df['LowSatisfactionFlag'] = (df['SatisfactionScore'] <= 2).astype(int)
    df['LowSatAndComplain'] = ((df['LowSatisfactionFlag'] == 1) & (df['Complain'] == 1)).astype(int)
    # WarehouseToHome_log 활용
    df['FarFromWarehouse'] = (df['WarehouseToHome_log'] > df['WarehouseToHome_log'].quantile(0.75)).astype(int)

    # --- 4. 앱/기기 사용 패턴 ---
    df['AppTimePerOrder'] = df['HourSpendOnApp'] / (df['OrderCount'] + 1)
    df['OrdersPerDevice'] = df['OrderCount'] / (df['NumberOfDeviceRegistered'] + 1)
    df['ManyAddressesFlag'] = (df['NumberOfAddress'] >= 3).astype(int)

    # --- 5. 가입 기간 구간화 (Tenure_log를 다시 지수화해서 원래 기간 기준으로 구분) ---
    original_tenure = np.exp(df['Tenure_log'])
    df['is_newbie_risk'] = (original_tenure <= 5).astype(int)
    df['is_loyal_vvip'] = (original_tenure >= 30).astype(int)
    df['Tenure_Group'] = pd.cut(original_tenure, bins=[-1, 5, 20, 200], labels=['New', 'Mid', 'Loyal'])

    # --- 6. 행동 기반 우수 고객 ---
    df['VIP_LikeCustomer'] = ((df['HighFreqBuyer'] == 1) & (df['SatisfactionScore'] >= 4)).astype(int)

    # --- 7. 범주형 변수 처리 (Encoding) ---
    cat_cols = ['PreferredLoginDevice', 'PreferredPaymentMode', 'PreferedOrderCat', 
                'Tenure_Group', 'MaritalStatus', 'Gender']
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # --- 8. 최종 데이터 정제 (Cleaning) ---
    # 특수문자 및 공백 제거
    df.columns = [c.replace(' ', '_').replace('/', '_').replace('-', '_') for c in df.columns]
    
    # bool 타입을 int로 변환
    bool_cols = df.select_dtypes(include=['bool']).columns
    df[bool_cols] = df[bool_cols].astype(int)

    return df