import pandas as pd
import numpy as np

def outlier_control(df,cols): 


  for col in cols:
    if col == 'CashbackAmount':
      df[f'{col}_clip'] = df['CashbackAmount'].clip(lower=100,upper=240)

    else:
      df[f'{col}_log'] = np.log1p(df[col])


  df.drop(cols, axis=1, inplace=True) # 원본 피처가 필요하면 이부분 주석처리하고 사용하세요




cols=['Tenure','WarehouseToHome','DaySinceLastOrder','CashbackAmount']

outlier_control(df,cols)