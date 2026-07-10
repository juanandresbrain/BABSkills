# dbo.aw_Giftcards_Redeemed

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| gross_line_amount | money | 8 | 1 |  |  |  |
| pos_discount_amount | money | 8 | 1 |  |  |  |
| reference_no | varchar | 80 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| priorRedemptionsThisBatch | money | 8 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| activation_discount_amount | money | 8 | 1 |  |  |  |
| liftAmount | money | 8 | 1 |  |  |  |
