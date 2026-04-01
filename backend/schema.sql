DROP TABLE IF EXISTS cherry_metrics CASCADE;
DROP TABLE IF EXISTS churn_metrics CASCADE;
DROP TABLE IF EXISTS customer_activity CASCADE;
DROP TABLE IF EXISTS customer_base CASCADE;

CREATE TABLE customer_base (
  CustomerID bigint PRIMARY KEY,
  CityTier int,
  Gender int,
  MaritalStatus varchar,
  NumberOfAddress int,
  NumberOfDeviceRegistered int,
  WarehouseToHome float,
  Churn int
);

CREATE TABLE customer_activity (
  CustomerID bigint PRIMARY KEY,
  Tenure float,
  DaysSinceLastOrder float,
  OrderAmountHikeFromLastYear float,
  CashbackAmount float,
  OrderCount int,
  CouponUsed int,
  HourSpendOnApp float,
  Complain int,
  SatisfactionScore float,
  FOREIGN KEY (CustomerID) REFERENCES customer_base(CustomerID)
);

CREATE TABLE churn_metrics (
  CustomerID bigint PRIMARY KEY,
  Churn_Prob float,
  first_leave int,
  second_leave int,
  FOREIGN KEY (CustomerID) REFERENCES customer_base(CustomerID)
);

CREATE TABLE cherry_metrics (
  CustomerID bigint PRIMARY KEY,
  Cherry_Prob float,
  Cherry_Label int,
  FOREIGN KEY (CustomerID) REFERENCES customer_base(CustomerID)
);