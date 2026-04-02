import pandas as pd

df1 = pd.read_excel('../data/cherrypicker_dataset.xlsx')
df2 = pd.read_excel('../data/dataset_with_prob.xlsx')

df = df1.merge(df2, on='CustomerID', how='left')

print(df.info())
