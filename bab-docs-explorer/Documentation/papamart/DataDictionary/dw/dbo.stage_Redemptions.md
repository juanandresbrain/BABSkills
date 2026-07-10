# dbo.stage_Redemptions

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| register_num | int | 4 | 0 |  |  |  |
| TtlGiftCard | money | 8 | 1 |  |  |  |
| TtlBearBuck | money | 8 | 1 |  |  |  |
| TtlBuyStuff | money | 8 | 1 |  |  |  |
| TtlMallGC | money | 8 | 1 |  |  |  |
