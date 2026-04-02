from connection import get_connection

def get_customer_details(customer_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    # pandas to_sql은 컬럼명을 대소문자 유지(따옴표 식별자)로 만들므로 PostgreSQL에서 소문자 참조와 불일치함.
    query = '''
    SELECT 
        cb."CustomerID" AS customer_id,

        ca."DaySinceLastOrder" AS days_since_last_order,

        ca."OrderCount" AS total_order_count,
        ca."CashbackAmount" AS cashback_amount,

        ca."CouponUsed" AS coupon_used,
        ca."Complain" AS complain,
        ca."SatisfactionScore" AS satisfaction_score,

        cm."Churn_Prob" AS churn_prob,
        chm."Cherry_Prob" AS cherry_prob,

        CASE 
            WHEN cm."Churn_Prob" > 0.8 THEN '최고위험(이탈임박)'
            WHEN cm."Churn_Prob" > 0.5 AND ca."CouponUsed" > 3 THEN '위험(체리피커형)'
            WHEN cm."Churn_Prob" > 0.5 THEN '주의(단순이탈위험)'
            ELSE '안전'
        END AS risk_segment

    FROM customer_base cb

    LEFT JOIN customer_activity ca 
        ON cb."CustomerID" = ca."CustomerID"

    LEFT JOIN churn_metrics cm 
        ON cb."CustomerID" = cm."CustomerID"

    LEFT JOIN cherry_metrics chm 
        ON cb."CustomerID" = chm."CustomerID"

    WHERE cb."CustomerID" = %s;
    '''

    try:
        cursor.execute(query, (customer_id,))
        fetched_data = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
        
    return fetched_data

