# dbo.az_giftcards_tmpbalance

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| giftcard_no | varchar | 320 | 1 |  |  |  |
| activated_amount | decimal | 17 | 1 |  |  |  |
| discount_amount | decimal | 17 | 1 |  |  |  |
| priorPostedDiscount | decimal | 9 | 1 |  |  |  |
| thisPostedDiscount | decimal | 9 | 1 |  |  |  |
| minDate_Key | int | 4 | 1 |  |  |  |
