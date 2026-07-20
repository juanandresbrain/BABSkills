# dbo.giftcard_activated_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| activated_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| giftcardtype | varchar | 8000 | 1 |  |  |  |
| calc | int | 4 | 1 |  |  |  |
| iscomp | int | 4 | 1 |  |  |  |
| iscompnextyear | int | 4 | 1 |  |  |  |
