# dbo.FlashTrafficToStoreFailureLog

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| StoreIP | varchar | 15 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| FailureReason | varchar | 1000 | 1 |  |  |  |
