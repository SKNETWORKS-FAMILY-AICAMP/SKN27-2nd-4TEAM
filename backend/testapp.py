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
            st.metric("총 주문 수", f"{data[2]}회")
            st.metric("평균 주문 금액", f"{int(data[3]):,}원")

        with col2:
            st.write(f"**위험도 세그먼트:** {data[8]}")
            st.progress(data[6], text=f"이탈 확률: {data[6]*100:.1f}%")
            st.progress(data[7], text=f"체리피커 확률: {data[7]*100:.1f}%")
            st.write(f"포인트 사용 비중: {data[4]*100:.1f}%")
            st.write(f"CS 문의 횟수: {data[5]}건")
            
    else:
        st.error("해당 ID의 고객 정보를 찾을 수 없습니다.")