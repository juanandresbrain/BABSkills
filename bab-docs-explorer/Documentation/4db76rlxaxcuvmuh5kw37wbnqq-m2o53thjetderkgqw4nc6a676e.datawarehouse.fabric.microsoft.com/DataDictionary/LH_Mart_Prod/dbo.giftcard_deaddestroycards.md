# dbo.giftcard_deaddestroycards

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| type | varchar | 8000 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| tblKey | int | 4 | 1 |  |  |  |
| balance | decimal | 9 | 1 |  |  |  |
| merchant_id | varchar | 8000 | 1 |  |  |  |
| card_class | int | 4 | 1 |  |  |  |
| local_currency_code | varchar | 8000 | 1 |  |  |  |
| processed | datetime2 | 8 | 1 |  |  |  |
