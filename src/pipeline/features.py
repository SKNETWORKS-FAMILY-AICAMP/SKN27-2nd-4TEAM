import pandas as pd
import numpy as np
from src.seed import set_seed

def FeatureCreate(df):
    df = df.copy()
    set_seed()

    # Tenure가 0인 경우 최소값 보정
    actual_tenure = np.exp(df['Tenure_log']).clip(lower=0.1)
    order_count = df['OrderCount']
    recency = df['DaySinceLastOrder_clip']
    
    # 분모가 0이 되는 것을 방지하기 위해 +1
    denom_order = order_count + 1
    avg_order_interval = (actual_tenure / denom_order).clip(lower=0.1)

    # [Dormancy_Shock] 평소 주기 대비 현재 공백
    df['Dormancy_Shock'] = recency / (avg_order_interval + 1)
    
    # [Promo_Sensitivity] 쿠폰 사용 비중 (체리피커 식별)
    df['Promo_Sensitivity'] = df['CouponUsed'] / denom_order
    
    # [MonthlyOrderFreq] 월평균 주문 빈도 
    df['MonthlyOrderFreq'] = order_count / actual_tenure
    
    # [Recency_Tenure_Ratio] 가입 기간 대비 휴면 비중 
    df['Recency_Tenure_Ratio'] = recency / actual_tenure
    
    # [Satisfaction_Per_Order] 경험 대비 만족도
    df['Satisfaction_Per_Order'] = df['SatisfactionScore'] / denom_order

    # [Stagnant_Loyal] 장기 고객 중 활동 정체군
    freq_mean = df['MonthlyOrderFreq'].mean()
    df['Stagnant_Loyal'] = ((actual_tenure >= 30) & (df['MonthlyOrderFreq'] < freq_mean)).astype(int)
    
    # [ManyAddressesFlag] 배송지 다변화
    df['ManyAddressesFlag'] = (df['NumberOfAddress'] >= 3).astype(int)
    
    # [High_Value_Flags] 주요 지표 상위 25% 그룹화
    for col in ['OrderCount', 'CouponUsed']:
        q75 = df[col].quantile(0.75)
        df[f'High_{col}'] = (df[col] > q75).astype(int)

    # 4. 범주형 변수 처리 (One-Hot Encoding)
    cat_cols = ['PreferredLoginDevice', 'PreferredPaymentMode', 'PreferedOrderCat', 'MaritalStatus', 'Gender']
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    drop_cols = [
        'DaySinceLastOrder_clip', 'Complain', 'MaritalStatus_Single',
        'SatisfactionScore', 'HourSpendOnApp', 'CashbackAmount_clip', 
        'WarehouseToHome_log', 'OrderCount', 'CouponUsed'
    ]
    df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)
    
    return df