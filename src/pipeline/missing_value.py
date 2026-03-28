from src.seed import set_seed



def MissingValue(group, overall_median, max):
    set_seed()
    if len(group) < max:
        return group.fillna(overall_median)  
    return group.fillna(group.median())      


'''
overall_median = df['Tenure'].median()
df['Tenure'] = df.groupby('NumberOfAddress')['Tenure'].transform(lambda x: MissingValue(x, overall_median, 5))

overall_median = df['DaySinceLastOrder'].median()
df['DaySinceLastOrder'] = df.groupby(['PreferedOrderCat', 'PreferredLoginDevice'])\
    ['DaySinceLastOrder'].transform(lambda x: MissingValue(x, overall_median, 10))

overall_median = df['OrderCount'].median()
df['OrderCount'] = df.groupby(['PreferedOrderCat', 'PreferredPaymentMode'])\
    ['OrderCount'].transform(lambda x: MissingValue(x, overall_median, 10))

overall_median = df['OrderAmountHikeFromlastYear'].median()
df['OrderAmountHikeFromlastYear'] = df.groupby('PreferedOrderCat')\
    ['OrderAmountHikeFromlastYear'].transform(lambda x: MissingValue(x, overall_median, 3))

overall_median = df['CouponUsed'].median()
df['CouponUsed'] = df.groupby(['PreferedOrderCat', 'PreferredPaymentMode'])\
    ['CouponUsed'].transform(lambda x: MissingValue(x, overall_median, 10))

overall_median = df['HourSpendOnApp'].median()
df['HourSpendOnApp'] = df.groupby(['PreferedOrderCat', 'PreferredPaymentMode'])\
    ['HourSpendOnApp'].transform(lambda x: MissingValue(x, overall_median, 10))

overall_median = df['WarehouseToHome'].median()
df['WarehouseToHome'] = df.groupby(['PreferedOrderCat', 'PreferredPaymentMode'])\
    ['WarehouseToHome'].transform(lambda x: MissingValue(x, overall_median, 20))


'''