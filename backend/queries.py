import streamlit as st
from connection import get_connection

def get_customer_details(customer_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = '''
    SELECT 
        cb.CustomerID AS 고객ID,

        ca.DaySinceLastOrder AS 접속경과일,

        ca.OrderCount AS 총주문수,  
        ca.CashbackAmount AS 평균주문금액,

        ca.CouponUsed AS 쿠폰사용횟수,
        ca.Complain AS CS문의여부,
        ca.SatisfactionScore AS 만족도,

        cm.Churn_Prob AS 이탈확률,
        chm.Cherry_Prob AS 체리피커확률,

        CASE 
            WHEN cm.Churn_Prob > 0.8 THEN '최고위험(이탈임박)'
            WHEN cm.Churn_Prob > 0.5 AND ca.CouponUsed > 3 THEN '위험(체리피커형)'
            WHEN cm.Churn_Prob > 0.5 THEN '주의(단순이탈위험)'
            ELSE '안전'
        END AS 위험도_세그먼트

    FROM customer_base cb

    LEFT JOIN customer_activity ca 
        ON cb.CustomerID = ca.CustomerID

    LEFT JOIN churn_metrics cm 
        ON cb.CustomerID = cm.CustomerID

    LEFT JOIN cherry_metrics chm 
        ON cb.CustomerID = chm.CustomerID

    WHERE cb.CustomerID = %s;
    '''

    try:
        cursor.execute(query, (customer_id,))
        fetched_data = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
        
    return fetched_data

