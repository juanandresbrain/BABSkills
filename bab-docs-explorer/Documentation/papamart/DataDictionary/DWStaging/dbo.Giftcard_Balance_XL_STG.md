# dbo.Giftcard_Balance_XL_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| ActivationDate | datetime | 8 | 1 |  |  |  |
| MID | varchar | 255 | 1 |  |  |  |
| CardNumber | varchar | 255 | 1 |  |  |  |
| PromoCode | varchar | 255 | 1 |  |  |  |
| BalanceOnCard | money | 8 | 1 |  |  |  |
| Consortium | varchar | 255 | 1 |  |  |  |
