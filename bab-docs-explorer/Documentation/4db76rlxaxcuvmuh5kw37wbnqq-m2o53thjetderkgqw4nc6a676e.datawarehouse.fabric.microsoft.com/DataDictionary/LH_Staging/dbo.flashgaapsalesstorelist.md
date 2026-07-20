# dbo.flashgaapsalesstorelist

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreIP | varchar | 8000 | 1 |  |  |  |
| StoreGroup | bigint | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| LocationCode | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| GMT_Offset | int | 4 | 1 |  |  |  |
| CurrentStoreTime | datetime2 | 8 | 1 |  |  |  |
