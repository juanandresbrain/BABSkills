# dbo.webtostorelookup

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| isPickupFromStore | int | 4 | 1 |  |  |  |
| isCurbside | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isSameDay | int | 4 | 1 |  |  |  |
| LineNote | varchar | 8000 | 1 |  |  |  |
