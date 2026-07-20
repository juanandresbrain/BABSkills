# dbo.tmpawgcrmergesource

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| redemption_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| giftcard_no | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| activation_discount_amount | decimal | 9 | 1 |  |  |  |
| lift_amount | decimal | 9 | 1 |  |  |  |
