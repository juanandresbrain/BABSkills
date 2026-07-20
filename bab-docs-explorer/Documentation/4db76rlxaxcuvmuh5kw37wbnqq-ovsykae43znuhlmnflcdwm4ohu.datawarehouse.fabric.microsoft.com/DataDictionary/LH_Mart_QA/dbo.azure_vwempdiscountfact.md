# dbo.azure_vwempdiscountfact

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | decimal | 9 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| ReferenceNumber | varchar | 8000 | 1 |  |  |  |
| LineObject | int | 4 | 1 |  |  |  |
| DiscountUnits | int | 4 | 1 |  |  |  |
| DiscountUnitGrossAmount | decimal | 5 | 1 |  |  |  |
| ExpiredFlag | bit | 1 | 1 |  |  |  |
| DiscountCategoryType | varchar | 8000 | 1 |  |  |  |
| DiscountChannelType | varchar | 8000 | 1 |  |  |  |
| DiscountFinancialGroup | varchar | 8000 | 1 |  |  |  |
| RetailPro | int | 4 | 1 |  |  |  |
| CouponDesc | varchar | 8000 | 1 |  |  |  |
