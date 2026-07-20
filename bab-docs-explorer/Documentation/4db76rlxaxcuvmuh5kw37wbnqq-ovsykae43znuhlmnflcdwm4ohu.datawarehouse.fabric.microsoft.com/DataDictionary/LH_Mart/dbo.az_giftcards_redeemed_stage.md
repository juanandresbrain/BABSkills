# dbo.az_giftcards_redeemed_stage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_ID | varchar | 1280 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| Gross_Line_Amount | decimal | 9 | 1 |  |  |  |
| POS_Discount_Amount | decimal | 9 | 1 |  |  |  |
| Reference_No | varchar | 1280 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| priorRedemptionsThisBatch | int | 4 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| activation_discount_amount | decimal | 9 | 1 |  |  |  |
| liftAmount | decimal | 9 | 1 |  |  |  |
