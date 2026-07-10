# dbo.GCFinalBalanceAsOfDateTmp

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| giftcard_no | varchar | 80 | 1 |  |  |  |
| Balance | money | 8 | 1 |  |  |  |
| activation_amount | money | 8 | 1 |  |  |  |
| redemption_amount | money | 8 | 1 |  |  |  |
| activation_discount_amount | money | 8 | 1 |  |  |  |
| activation_discount_redeemed | money | 8 | 1 |  |  |  |
| activation_discount_balance | money | 8 | 1 |  |  |  |
| MID | varchar | 50 | 1 |  |  |  |
| MIDDescription | varchar | 100 | 1 |  |  |  |
| CurrencyDescription | varchar | 100 | 1 |  |  |  |
| AsOfDate | datetime | 8 | 1 |  |  |  |
