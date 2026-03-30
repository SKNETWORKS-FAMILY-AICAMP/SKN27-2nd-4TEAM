import numpy as np
import pandas as pd

def compute_cherry_picker(df):
    df = df.copy()
    # Tenure(가입기간) 2개월 이하는 "체리피커 판별에서 제외" 대상.
    # 주의: 퍼센타일(rank) 기반 점수는 분포에 민감하므로,
    # 제외 대상을 점수 계산에 포함시키면 다른 사용자 점수까지 함께 흔들릴 수 있음.
    tenure_excluded = df['Tenure'] <= 2

    # -----------------------------
    # 1. percentile 함수
    # -----------------------------
    def pr(x):
        return x.rank(pct=True)


    # -----------------------------
    # 3. 혜택 의존도 score
    # -----------------------------
    # 점수/퍼센타일 계산은 tenure>2 사용자들만 대상으로 수행 (제외대상은 아예 스코어링에서 뺌)
    df_scored = df.loc[~tenure_excluded].copy()
    if df_scored.empty:
        # 전원이 제외 대상이면 스코어링 자체가 불가하므로,
        # 확률을 모두 0(체리피커 아님)으로 두고 반환.
        df['Cherry_Prob'] = 0.0
        df['Cherry_Label'] = "Normal"
        return df

    promo_score = pr(df_scored['Promo_Sensitivity'])
    cashback_score = pr(df_scored['CashbackPerOrder'])

    benefit_score = 0.8 * promo_score + 0.2 * cashback_score

    # -----------------------------
    # 4. 비충성 행동 score
    # -----------------------------
    freq_score = 1 - pr(df_scored['MonthlyOrderFreq'])
    dormancy_score = pr(df_scored['Dormancy_Shock'])
    recency_score = pr(df_scored['Recency_Tenure_Ratio'])

    behavior_score = (
        0.55 * freq_score +
        0.35 * dormancy_score +
        0.1 * recency_score
    )


    # -----------------------------
    # 6. 최종 체리피커 확률
    # -----------------------------
    cherry_prob = (
        0.7 * benefit_score +
        0.3 * behavior_score 
    )

    # -----------------------------
    # 7. 필터 (충성/완전비활성 보정)
    # -----------------------------
    if 'Stagnant_Loyal' in df_scored.columns:
        cherry_prob = np.where(
            df_scored['Stagnant_Loyal'] == 1,
            cherry_prob * 0.3,
            cherry_prob
        )

    if 'Silent_Killer' in df_scored.columns:
        cherry_prob = np.where(
            df_scored['Silent_Killer'] == 1,
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
        if x >= 0.8:
            return "High Cherry Picker"
        elif x >= 0.5:
            return "Potential"
        else:
            return "Normal"

    # 원본 df 길이에 맞춰 결과를 되돌려 채움:
    # - tenure>2: 계산된 확률
    # - tenure<=2(제외): 0
    cherry_prob_full = np.zeros(len(df), dtype=float)
    cherry_prob_full[~tenure_excluded.to_numpy()] = np.asarray(cherry_prob, dtype=float)

    df['Cherry_Prob'] = cherry_prob_full
    df['Cherry_Label'] = df['Cherry_Prob'].apply(label)

    return df