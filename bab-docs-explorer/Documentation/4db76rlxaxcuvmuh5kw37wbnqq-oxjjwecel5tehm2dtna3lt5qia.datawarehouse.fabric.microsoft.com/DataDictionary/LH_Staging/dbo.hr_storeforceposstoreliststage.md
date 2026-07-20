# dbo.hr_storeforceposstoreliststage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| LocationCode | varchar | 8000 | 1 |  |  |  |
| StoreIP | varchar | 8000 | 1 |  |  |  |
| StoreGroup | bigint | 8 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| GMT_Offset | int | 4 | 1 |  |  |  |
| CurrentStoreTime | datetime2 | 8 | 1 |  |  |  |
