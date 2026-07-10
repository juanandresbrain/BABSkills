# dbo.HR_StoreForceBopisStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNo | int | 4 | 1 |  |  |  |
| Date | varchar | 30 | 1 |  |  |  |
| Slot | varchar | 5 | 1 |  |  |  |
| ShipFromStoreSales | numeric | 17 | 1 |  |  |  |
| ShipFromStoreTransactions | bigint | 8 | 1 |  |  |  |
| ShipFromStoreUnits | bigint | 8 | 1 |  |  |  |
| PickupFromStoreSales | numeric | 17 | 1 |  |  |  |
| PickupFromStoreTransactions | bigint | 8 | 1 |  |  |  |
| PickupFromStoreUnits | bigint | 8 | 1 |  |  |  |
| CurbsideSales | numeric | 17 | 1 |  |  |  |
| CurbsideTransactions | bigint | 8 | 1 |  |  |  |
| CurbsideUnits | bigint | 8 | 1 |  |  |  |
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
