# dbo.Giftcards_Redeemed_Bak20230620

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| redemption_amount | money | 8 | 0 |  |  |  |
| discount_amount | money | 8 | 0 |  |  |  |
| giftcard_no | varchar | 80 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 50 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 0 |  |  |  |
| lift_amount | money | 8 | 0 |  |  |  |
| activation_discount_amount | money | 8 | 0 |  |  |  |
| source | varchar | 10 | 0 |  |  |  |
| VLVerified | bit | 1 | 0 |  |  |  |
