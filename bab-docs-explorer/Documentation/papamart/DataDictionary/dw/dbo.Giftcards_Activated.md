# dbo.Giftcards_Activated

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| activated_amount | money | 8 | 0 |  |  |  |
| discount_amount | money | 8 | 0 |  |  |  |
| giftcard_no | varchar | 80 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 50 | 1 |  |  |  |
| Source | varchar | 10 | 0 |  |  | Source of this record - AW = Auditworks, VL=Valuelink |
| VLVerified | bit | 1 | 0 |  |  | Was this activation verfied from ValueLink transactions? |
