# Loyalty.DiscountDE

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Category | varchar | -1 | 1 |  |  |  |
| certificateNumber | varchar | -1 | 1 |  |  |  |
| coupon_desc | varchar | -1 | 1 |  |  |  |
| couponNumber | varchar | -1 | 1 |  |  |  |
| DiscountAmountPerLine | decimal | 9 | 1 |  |  |  |
| DiscountTransactionLineNumber | decimal | 9 | 1 |  |  |  |
| event_name | varchar | -1 | 1 |  |  |  |
| TransactionID | varchar | -1 | 1 |  |  |  |
| UnitGrossAmount | decimal | 9 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| customerNumber | varchar | -1 | 1 |  |  |  |
| ActiveFlag | bit | 1 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| Id | int | 4 | 0 |  |  |  |
| ExternalID | varchar | -1 | 1 |  |  |  |
