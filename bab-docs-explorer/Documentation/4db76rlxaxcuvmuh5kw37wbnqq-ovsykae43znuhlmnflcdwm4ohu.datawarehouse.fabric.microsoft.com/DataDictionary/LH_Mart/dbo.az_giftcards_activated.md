# dbo.az_giftcards_activated

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | varchar | 320 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| activated_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| giftcard_no | varchar | 320 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 200 | 1 |  |  |  |
| Source | varchar | 40 | 1 |  |  |  |
| VLVerified | int | 4 | 1 |  |  |  |
