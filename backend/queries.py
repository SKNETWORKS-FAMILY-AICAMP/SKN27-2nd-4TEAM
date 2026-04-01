from connection import get_connection

def get_customer_details(customer_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''SELECT
        CustomerID,
        Churn
        FROM customer_base
        WHERE CustomerID = %s''', (customer_id,))

    fetched_data = cursor.fetchone()

    cursor.close()
    conn.close()
    return fetched_data

    
'''
customer_id = st.number_input("Customer ID")

if st.button("조회"):
    data = get_customer_detail(customer_id)
    st.write(data)

'''