CREATE TABLE "customer_base" (
  "CustomerID" int PRIMARY KEY,
  "CityTier" int,
  "Gender_Male" int,
  "MaritalStatus_Married" int,
  "MaritalStatus_Single" int,
  "NumberOfDeviceRegistered" int,
  "NumberOfAddress" int,
  "ManyAddressesFlag" int,
  "split" varchar,
  "Churn" int
);

CREATE TABLE "cleaned_metrics" (
  "CustomerID" int PRIMARY KEY,
  "Tenure_log" float,
  "OrderAmountHikeFromlastYear" float,
  "CashbackAmount_clip" float,
  "DaySinceLastOrder_clip" float
);

CREATE TABLE "behavior_analysis" (
  "CustomerID" int PRIMARY KEY,
  "Dormancy_Shock" float,
  "Recency_Tenure_Ratio" float,
  "MonthlyOrderFreq" float,
  "Stagnant_Loyal" int,
  "IssueIndex" int,
  "Satisfaction_Per_Order" float,
  "Silent_Killer" int
);

CREATE TABLE "marketing_sensitivity" (
  "CustomerID" int PRIMARY KEY,
  "Promo_Sensitivity" float,
  "CashbackPerOrder" float,
  "PreferedOrder_Mobile_Phone" int,
  "PreferedOrder_Laptop_Accessory" int,
  "PreferedOrder_Others" int,
  "PreferredLoginDevice_Phone" int
);

COMMENT ON COLUMN "customer_base"."Gender_Male" IS '0: Female, 1: Male';

COMMENT ON COLUMN "customer_base"."ManyAddressesFlag" IS 'Address >= 3';

COMMENT ON COLUMN "customer_base"."split" IS 'train / test';

COMMENT ON COLUMN "customer_base"."Churn" IS 'Target Variable';

COMMENT ON COLUMN "cleaned_metrics"."Tenure_log" IS 'Log1p transformed';

COMMENT ON COLUMN "behavior_analysis"."Dormancy_Shock" IS 'Recent gap vs Avg interval';

COMMENT ON COLUMN "behavior_analysis"."Recency_Tenure_Ratio" IS 'Gap / Total Tenure';

COMMENT ON COLUMN "behavior_analysis"."MonthlyOrderFreq" IS 'Orders per month';

COMMENT ON COLUMN "behavior_analysis"."Stagnant_Loyal" IS 'Inactive loyal customers';

COMMENT ON COLUMN "behavior_analysis"."IssueIndex" IS 'Complain flag';

COMMENT ON COLUMN "behavior_analysis"."Silent_Killer" IS 'No complain but low satisfaction';

COMMENT ON COLUMN "marketing_sensitivity"."Promo_Sensitivity" IS 'Coupon usage ratio (Cherry-picker Key)';

ALTER TABLE "cleaned_metrics" ADD FOREIGN KEY ("CustomerID") REFERENCES "customer_base" ("CustomerID") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "behavior_analysis" ADD FOREIGN KEY ("CustomerID") REFERENCES "customer_base" ("CustomerID") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "marketing_sensitivity" ADD FOREIGN KEY ("CustomerID") REFERENCES "customer_base" ("CustomerID") DEFERRABLE INITIALLY IMMEDIATE;
