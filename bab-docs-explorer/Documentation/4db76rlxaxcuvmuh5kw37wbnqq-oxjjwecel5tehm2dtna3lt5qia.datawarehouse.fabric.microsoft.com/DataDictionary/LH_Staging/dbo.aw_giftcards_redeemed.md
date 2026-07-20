# dbo.aw_giftcards_redeemed

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| priorRedemptionsThisBatch | decimal | 9 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| activation_discount_amount | decimal | 9 | 1 |  |  |  |
| liftAmount | decimal | 9 | 1 |  |  |  |
