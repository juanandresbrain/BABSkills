# dbo.gcstage_redemptions

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| redemption_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| giftcard_no | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 8000 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| lift_amount | decimal | 9 | 1 |  |  |  |
| activation_discount_amount | decimal | 9 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| VLVerified | bit | 1 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
| vlLineID | int | 4 | 1 |  |  |  |
