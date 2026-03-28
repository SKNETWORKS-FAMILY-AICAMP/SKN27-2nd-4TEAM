import pandas as pd

from src.seed import set_seed


def CJ_MissingValue(df, col, group_cols, min_group_size, train_median, test_df=None):
    set_seed()
    group_columns = [group_cols] if isinstance(group_cols, str) else list(group_cols)

    def fill_by_group(series):
        if len(series) < min_group_size:
            return series.fillna(train_median)
        return series.fillna(series.median())

    df[col] = df.groupby(group_columns)[col].transform(fill_by_group)

    if test_df is not None:
        test_df[col] = test_df[col].fillna(train_median)
    return df


'''=============================================================================================='''


def fill_hour_spend_on_app(df, hour_mode):
    set_seed()
    df["HourSpendOnApp"] = df["HourSpendOnApp"].fillna(hour_mode)
    return df


def fill_warehouse_to_home(df, median_by_city):
    set_seed()
    df["WarehouseToHome"] = df["WarehouseToHome"].fillna(df["CityTier"].map(median_by_city))
    return df


def fill_coupon_used(df, coupon_median_by_group, coupon_median_all, cashback_split_points):
    set_seed()
    df["CashbackPerOrder"] = df["CashbackAmount"] / df["OrderCount"]
    df["_cashback_group"] = pd.cut(
        df["CashbackPerOrder"],
        bins=cashback_split_points,
        labels=False,
        include_lowest=True,
    )
    for group_id, med in coupon_median_by_group.items():
        mask = (df["_cashback_group"] == group_id) & df["CouponUsed"].isna()
        df.loc[mask, "CouponUsed"] = med
    df["CouponUsed"] = df["CouponUsed"].fillna(coupon_median_all)
    df.drop(columns=["CashbackPerOrder", "_cashback_group"], inplace=True)
    return df


def JH_MissingValue(df, hour_mode, median_by_city, coupon_median_by_group, coupon_median_all, cashback_split_points):
    fill_hour_spend_on_app(df, hour_mode)
    fill_warehouse_to_home(df, median_by_city)
    fill_coupon_used(df, coupon_median_by_group, coupon_median_all, cashback_split_points)
    return df


'''
# CJ: train_median = df_train[col].median()
#     CJ_MissingValue(df_train, col, group_cols, min_group_size, train_median, test_df=df_test)

# JH: train에서 hour_mode, median_by_city, coupon_median_by_group, coupon_median_all, cashback_split_points 계산 후
#     JH_MissingValue(df_train, ...) / JH_MissingValue(df_test, ...) 동일 인자

'''
