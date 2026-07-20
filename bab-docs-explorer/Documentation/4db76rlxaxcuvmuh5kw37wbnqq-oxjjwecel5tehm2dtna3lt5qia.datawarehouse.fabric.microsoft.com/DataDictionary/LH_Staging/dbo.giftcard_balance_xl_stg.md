# dbo.giftcard_balance_xl_stg

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| ActivationDate | datetime2 | 8 | 1 |  |  |  |
| MID | varchar | 8000 | 1 |  |  |  |
| CardNumber | varchar | 8000 | 1 |  |  |  |
| PromoCode | varchar | 8000 | 1 |  |  |  |
| BalanceOnCard | decimal | 9 | 1 |  |  |  |
| Consortium | varchar | 8000 | 1 |  |  |  |
