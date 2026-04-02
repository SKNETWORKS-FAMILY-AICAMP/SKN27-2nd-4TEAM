import streamlit as st

from queries import get_customer_details

st.title("고객 이탈 및 체리피커 분석 대시보드")

customer_id_input = st.number_input("조회할 Customer ID를 입력하세요", min_value=1, step=1)

if st.button("고객 정보 조회"):
    data = get_customer_details(int(customer_id_input))

    if data:
        col1, col2 = st.columns(2)

        with col1:
            st.metric("고객 ID", data[0])
            st.metric("접속 경과일", f"{data[1]}일" if data[1] is not None else "기록 없음")
            st.metric("총 주문 수", f"{data[2]}회" if data[2] is not None else "기록 없음")
            cb = data[3]
            if cb is not None:
                st.metric("캐시백 금액 (CashbackAmount)", f"{float(cb):,.2f}원")
            else:
                st.metric("캐시백 금액 (CashbackAmount)", "기록 없음")

        with col2:
            st.write(f"**위험도 세그먼트:** {data[9]}")
            sat = data[6]
            st.metric(
                "만족도 (SatisfactionScore)",
                f"{float(sat):.4f}" if sat is not None else "—",
            )
            ch0, ch1 = data[7], data[8]
            m_a, m_b = st.columns(2)
            with m_a:
                st.metric(
                    "이탈 확률 (Churn_Prob)",
                    f"{float(ch0):.6f}" if ch0 is not None else "—",
                )
            with m_b:
                st.metric(
                    "체리피커 확률 (Cherry_Prob)",
                    f"{float(ch1):.6f}" if ch1 is not None else "—",
                )
            coup = data[4]
            st.write(f"쿠폰 사용 횟수: {coup if coup is not None else '—'}회")
            st.write(f"CS 문의 횟수: {data[5] if data[5] is not None else '—'}건")

    else:
        st.error("해당 ID의 고객 정보를 찾을 수 없습니다.")
