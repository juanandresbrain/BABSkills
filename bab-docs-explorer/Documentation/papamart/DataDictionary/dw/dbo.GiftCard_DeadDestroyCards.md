# dbo.GiftCard_DeadDestroyCards

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| type | varchar | 20 | 1 |  |  |  |
| account_number | nvarchar | 510 | 1 |  |  |  |
| tblKey | int | 4 | 0 | YES |  |  |
| balance | money | 8 | 1 |  |  |  |
| merchant_id | varchar | 20 | 1 |  |  |  |
| card_class | int | 4 | 1 |  |  |  |
| local_currency_code | char | 3 | 1 |  |  |  |
| processed | datetime | 8 | 1 |  |  |  |
