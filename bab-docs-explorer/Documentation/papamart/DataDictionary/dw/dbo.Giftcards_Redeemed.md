# dbo.Giftcards_Redeemed

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
| daysSinceLastActivation | int | 4 | 0 |  |  | The number of days since the last activation on this card |
| lift_amount | money | 8 | 0 |  |  | The amount of lift assigned to this redemption |
| activation_discount_amount | money | 8 | 0 |  |  | The amount of the activation discount that was assigned to this redemption |
| source | varchar | 10 | 0 |  |  | Source of this record - AW = Auditworks, VLA=Valuelink Adjustment |
| VLVerified | bit | 1 | 0 |  |  | Was this Redemption verfied by Valuelink transactions? |
