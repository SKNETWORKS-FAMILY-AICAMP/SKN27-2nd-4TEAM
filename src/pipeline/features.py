import pandas as pd
import numpy as np

def FeatureCreate(df, train_monthly_freq_mean=None):
    df = df.copy()

    actual_tenure = np.expm1(df['Tenure_log']).clip(lower=0.1)
    # 계산 편의를 위한 변수 설정 (나눗셈 시 0 방지를 위해 +1 처리)
    order_cnt = df['OrderCount']
    denom_order = order_cnt + 1
    # 평균 주문 주기: 전체 가입 기간 중 얼마나 자주 주문했는지 시간 간격 계산
    avg_interval = (actual_tenure / denom_order).clip(lower=0.1)

    # 1. (이탈의 핵심 징후 포착)
    # Dormancy_Shock: 평소 주기 대비 이번 공백기가 얼마나 '충격적'으로 긴지 (값 클수록 위험)
    df['Dormancy_Shock'] = df['DaySinceLastOrder_clip'] / (avg_interval + 1)
    # Recency_Tenure_Ratio: 가입 기간 대비 공백기 비중 (신규 고객의 이탈 가능성 포착)
    df['Recency_Tenure_Ratio'] = df['DaySinceLastOrder_clip'] / actual_tenure
    # MonthlyOrderFreq: 월평균 주문 빈도 (고객의 활동성 수준)
    df['MonthlyOrderFreq'] = order_cnt / actual_tenure
    
    # 2. 경험 및 심리 지표
    # IssueIndex: 불만 제기 여부 (명시적인 부정적 경험)
    df['IssueIndex'] = df['Complain'].astype(int)
    # Satisfaction_Per_Order: 주문 횟수 대비 체감 만족도 효율
    df['Satisfaction_Per_Order'] = df['SatisfactionScore'] / denom_order
    # Silent_Killer: 불만은 없으나 만족도가 낮은 '조용한 이탈자' 후보군 식별
    df['Silent_Killer'] = ((df['IssueIndex'] == 0) & (df['SatisfactionScore'] <= 2)).astype(int)
    
    # 3. 혜택 및 효율 지표
    # CashbackPerOrder: 주문 건당 평균 캐시백 혜택 체감도
    df['CashbackPerOrder'] = df['CashbackAmount_clip'] / denom_order
    # Promo_Sensitivity: 주문 대비 쿠폰 사용 빈도 (프로모션 민감도)
    df['Promo_Sensitivity'] = df['CouponUsed'] / denom_order

    # 4. 세그먼트 및 행동 플래그
    # Train 데이터의 평균 빈도를 기준으로 현재 데이터의 활동 정체 여부 판단 
    if train_monthly_freq_mean is not None:
        _mean_mof = train_monthly_freq_mean
    else:
        _mean_mof = df['MonthlyOrderFreq'].mean()
        
    # Stagnant_Loyal: 가입은 오래됐으나 활동이 평균 이하로 떨어진 '정체된 충성 고객'
    df['Stagnant_Loyal'] = ((actual_tenure >= 30) & (df['MonthlyOrderFreq'] < _mean_mof)).astype(int)
    # ManyAddressesFlag: 배송지 주소가 많음 (서비스 활용 반경이 넓은 헤비 유저 여부)
    df['ManyAddressesFlag'] = (df['NumberOfAddress'] >= 3).astype(int)

    # 6. 범주형 변수 처리 
    cat_cols = ['PreferredLoginDevice', 'PreferedOrderCat', 'MaritalStatus', 'Gender']
    available_cats = [c for c in cat_cols if c in df.columns]
    df = pd.get_dummies(df, columns=available_cats, drop_first=True)

    drop_cols = [
        'DaySinceLastOrder_clip', 'Complain', 'SatisfactionScore', 
        'CashbackAmount_clip', 'OrderCount', 'CouponUsed', 
        'WarehouseToHome_log', 'RecentActive', 'HourSpendOnApp',
        'is_newbie_risk', 'RoughLTV', 'PreferredPaymentMode'
    ]
    df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)
    
    # Boolean 타입을 0/1 정수형으로 최종 변환
    bool_cols = df.select_dtypes(include=['bool']).columns
    df[bool_cols] = df[bool_cols].astype(int)

    return df