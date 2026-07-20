# dbo.gcstage_activations

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| activated_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| giftcard_no | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 8000 | 1 |  |  |  |
| Source | varchar | 8000 | 1 |  |  |  |
| VLVerified | bit | 1 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
| vlLineID | int | 4 | 1 |  |  |  |
