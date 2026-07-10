# dbo.FlashTrafficStoreList

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 0 |  |  |  |
| StoreIP | varchar | 15 | 1 |  |  |  |
| StoreGroup | bigint | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| Jurisdiction | varchar | 20 | 1 |  |  |  |
| CurrencyCode | varchar | 3 | 1 |  |  |  |
| TradingGroup | varchar | 15 | 1 |  |  |  |
| GMT_Offset | int | 4 | 1 |  |  |  |
| CurrentStoreTime | datetime | 8 | 1 |  |  |  |
