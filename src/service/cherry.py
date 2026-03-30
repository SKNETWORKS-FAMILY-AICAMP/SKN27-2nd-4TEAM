import numpy as np
import pandas as pd

def compute_cherry_picker(df):
    df = df.copy()

    # -----------------------------
    # 1. percentile 함수
    # -----------------------------
    def pr(x):
        return x.rank(pct=True)

    # -----------------------------
    # 2. 결측치 방어 (필수)
    # -----------------------------
    cols = [
        'Promo_Sensitivity', 'CashbackPerOrder',
        'MonthlyOrderFreq', 'Dormancy_Shock',
        'Recency_Tenure_Ratio', 'Satisfaction_Per_Order',
        'Stagnant_Loyal', 'Silent_Killer'
    ]
    for c in cols:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())

    # -----------------------------
    # 3. 혜택 의존도 score
    # -----------------------------
    promo_score = pr(df['Promo_Sensitivity'])
    cashback_score = pr(df['CashbackPerOrder'])

    benefit_score = 0.6 * promo_score + 0.4 * cashback_score

    # -----------------------------
    # 4. 비충성 행동 score
    # -----------------------------
    freq_score = 1 - pr(df['MonthlyOrderFreq'])
    dormancy_score = pr(df['Dormancy_Shock'])
    recency_score = pr(df['Recency_Tenure_Ratio'])

    behavior_score = (
        0.5 * freq_score +
        0.3 * dormancy_score +
        0.2 * recency_score
    )

    # -----------------------------
    # 5. 고객 가치 score
    # -----------------------------
    value_score = 1 - pr(df['Satisfaction_Per_Order'])

    # -----------------------------
    # 6. 최종 체리피커 확률
    # -----------------------------
    cherry_prob = (
        0.5 * benefit_score +
        0.35 * behavior_score +
        0.15 * value_score
    )

    # -----------------------------
    # 7. 필터 (충성/완전비활성 보정)
    # -----------------------------
    if 'Stagnant_Loyal' in df.columns:
        cherry_prob = np.where(
            df['Stagnant_Loyal'] == 1,
            cherry_prob * 0.3,
            cherry_prob
        )

    if 'Silent_Killer' in df.columns:
        cherry_prob = np.where(
            df['Silent_Killer'] == 1,
            cherry_prob * 0.2,
            cherry_prob
        )

    # -----------------------------
    # 8. 클리핑
    # -----------------------------
    cherry_prob = np.clip(cherry_prob, 0, 1)

    # -----------------------------
    # 9. 라벨링
    # -----------------------------
    def label(x):
        if x >= 0.7:
            return "High Cherry Picker"
        elif x >= 0.4:
            return "Potential"
        else:
            return "Normal"

    df['Cherry_Prob'] = cherry_prob
    df['Cherry_Label'] = df['Cherry_Prob'].apply(label)

    return df