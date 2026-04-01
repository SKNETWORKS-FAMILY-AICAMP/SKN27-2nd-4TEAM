    import numpy as np

    def compute_cherry_picker(df):
        df = df.copy()
        # 가입 2개월 이하는 스코어링에서 제외(확률 0 처리)
        tenure_excluded = df['Tenure'] <= 2

        def pr(x):
            return x.rank(pct=True)

        # 퍼센타일(rank) 계산은 tenure>2 집단에서만 수행
        df_scored = df.loc[~tenure_excluded].copy()
        if df_scored.empty:
            # 전원이 제외 대상이면 계산 불가 → 전부 0 반환
            df['Cherry_Prob'] = 0.0
            df['Cherry_Label'] = "Normal"
            return df

        promo_score = pr(df_scored['Promo_Sensitivity'])
        cashback_score = pr(df_scored['CashbackPerOrder'])
        benefit_score = 0.8 * promo_score + 0.2 * cashback_score

        freq_score = 1 - pr(df_scored['MonthlyOrderFreq'])
        dormancy_score = pr(df_scored['Dormancy_Shock'])
        recency_score = pr(df_scored['Recency_Tenure_Ratio'])

        behavior_score = (
            0.55 * freq_score +
            0.35 * dormancy_score +
            0.1 * recency_score
        )

        cherry_prob = (0.7 * benefit_score + 0.3 * behavior_score)

        # 수식상 점수가 아무리 높아도, 실제 쿠폰 사용률(Promo_Sensitivity)이 
        # 0.4(40%) 미만인 사람은 체리피커 확률을 절반으로 깎음 (절대 기준 적용)
        cherry_prob = np.where(
            df_scored['Promo_Sensitivity'] < 0.3, 
            cherry_prob * 0.5, 
            cherry_prob
        )
        # ---------------------------------------------

        if 'Stagnant_Loyal' in df_scored.columns:
            cherry_prob = np.where(df_scored['Stagnant_Loyal'] == 1, cherry_prob * 0.3, cherry_prob)

        if 'Silent_Killer' in df_scored.columns:
            cherry_prob = np.where(df_scored['Silent_Killer'] == 1, cherry_prob * 0.2, cherry_prob)

        cherry_prob = np.clip(cherry_prob, 0, 1)

        def label(x):
            if x >= 0.8: return "High Cherry Picker"
            elif x >= 0.5: return "Potential"
            else: return "Normal"

        # 원본 df에 인덱스 기반으로 되돌려 채움(제외 대상은 0 유지)
        df['Cherry_Prob'] = 0.0
        df.loc[df_scored.index, 'Cherry_Prob'] = np.asarray(cherry_prob, dtype=float)
        df['Cherry_Label'] = df['Cherry_Prob'].apply(label)

        return df