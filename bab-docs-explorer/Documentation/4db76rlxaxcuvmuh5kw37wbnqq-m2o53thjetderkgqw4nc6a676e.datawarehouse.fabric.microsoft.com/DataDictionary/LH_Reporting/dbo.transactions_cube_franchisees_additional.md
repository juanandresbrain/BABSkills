# dbo.transactions_cube_franchisees_additional

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| iscomp | int | 4 | 1 |  |  |  |
| iscompnextyear | int | 4 | 1 |  |  |  |
| calc | int | 4 | 1 |  |  |  |
| Party_Count | int | 4 | 1 |  |  |  |
| Party_Sales | decimal | 9 | 1 |  |  |  |
| Transaction_Count | int | 4 | 1 |  |  |  |
| Coupons_And_Discounts | decimal | 9 | 1 |  |  |  |
| Returns | decimal | 9 | 1 |  |  |  |
