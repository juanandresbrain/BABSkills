# dbo.HR_StoreForcePosStoreListStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| StoreIP | varchar | 15 | 1 |  |  |  |
| StoreGroup | bigint | 8 | 1 |  |  |  |
| TradingGroup | varchar | 13 | 1 |  |  |  |
| GMT_Offset | int | 4 | 1 |  |  |  |
| CurrentStoreTime | datetime | 8 | 1 |  |  |  |
