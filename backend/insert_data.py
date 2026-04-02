import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

_ROOT = Path(__file__).resolve().parent.parent
_DATA = _ROOT / "data"


def make_table(df, cols):
    valid = [c for c in cols if c in df.columns]
    missing = [c for c in cols if c not in df.columns]
    
    if missing:
        print(f"Missing columns: {missing}")
    
    return df[valid]

df1 = pd.read_excel(_DATA / "cherrypicker_dataset.xlsx")
df2 = pd.read_excel(_DATA / "dataset_with_prob.xlsx")

df = df1.merge(df2, on='CustomerID', how='left')

'''-------------------------------'''
# customer_base

customer_base = make_table(df, [
    'CustomerID',
    'CityTier',
    'Gender',
    'MaritalStatus',
    'NumberOfAddress',
    'NumberOfDeviceRegistered',
    'WarehouseToHome',
    'Churn',
])

'''-------------------------------'''
# customer_activity

customer_activity = make_table(df, [
    'CustomerID',
    'Tenure',
    'DaySinceLastOrder',
    'OrderAmountHikeFromlastYear',
    'CashbackAmount',
    'OrderCount',
    'CouponUsed',
    'HourSpendOnApp',
    'Complain',
    'SatisfactionScore',
])

'''-------------------------------'''
# churn_metrics

churn_metrics = make_table(df, [
    'CustomerID',
    'Churn_Prob',
    '1st_leave',
    '2nd_leave',
])


'''-------------------------------'''
# cherry_metrics

cherry_metrics = make_table(df, [
    'CustomerID',
    'Cherry_Prob',
    'Cherry_Label',
])



_db_url = os.environ.get(
    "DATABASE_URL",
    "postgresql://skn27:password123@localhost:5432/retain_db",
)
engine = create_engine(_db_url)

customer_activity.to_sql("customer_activity", engine, if_exists="replace", index=False)

churn_metrics.to_sql("churn_metrics", engine, if_exists="replace", index=False)
cherry_metrics.to_sql("cherry_metrics", engine, if_exists="replace", index=False)
customer_base.to_sql("customer_base", engine, if_exists="replace", index=False)
