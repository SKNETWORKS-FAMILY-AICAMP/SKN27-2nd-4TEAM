import numpy as np
from src.seed import set_seed



def OutlierControl(df,cols):

  set_seed()

  for col in cols:
    if col == 'CashbackAmount':
      df[f'{col}_clip'] = df['CashbackAmount'].clip(lower=100,upper=240) 

    elif col == 'DaySinceLastOrder':
      df[f'{col}_clip'] = df['DaySinceLastOrder'].clip(upper=18)
      
    else:
      df[f'{col}_log'] = np.log1p(df[col])


  df.drop(cols, axis=1, inplace=True) # 원본 피처가 필요하면 이부분 주석처리하고 사용하세요
  return df


