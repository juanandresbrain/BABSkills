# dbo.tmpAWGCRMergeSource

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| redemption_amount | money | 8 | 1 |  |  |  |
| discount_amount | money | 8 | 1 |  |  |  |
| giftcard_no | varchar | 80 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| activation_discount_amount | money | 8 | 1 |  |  |  |
| lift_amount | money | 8 | 1 |  |  |  |
