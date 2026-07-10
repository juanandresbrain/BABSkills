# dbo.GiftCards_Redeemed_CleanupReference

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| actual_date | datetime | 8 | 1 |  |  |  |
| recID | int | 4 | 0 |  |  |  |
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
| VLA9520_DiscAmount | money | 8 | 0 |  |  |  |
| OriginalActivationDiscountAmount | money | 8 | 1 |  |  |  |
| RemainingActivationDiscountAmount | money | 8 | 1 |  |  |  |
| ActionType | varchar | 9 | 0 |  |  |  |
| Ranking | bigint | 8 | 1 |  |  |  |
| activation_discount_amount_to_be_applied | money | 8 | 1 |  |  |  |
