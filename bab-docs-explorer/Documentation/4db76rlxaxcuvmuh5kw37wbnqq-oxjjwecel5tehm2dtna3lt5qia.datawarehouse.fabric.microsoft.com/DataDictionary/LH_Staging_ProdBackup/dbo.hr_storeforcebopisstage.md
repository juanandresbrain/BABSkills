# dbo.hr_storeforcebopisstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNo | int | 4 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| ShipFromStoreSales | decimal | 17 | 1 |  |  |  |
| ShipFromStoreTransactions | bigint | 8 | 1 |  |  |  |
| ShipFromStoreUnits | bigint | 8 | 1 |  |  |  |
| PickupFromStoreSales | decimal | 17 | 1 |  |  |  |
| PickupFromStoreTransactions | bigint | 8 | 1 |  |  |  |
| PickupFromStoreUnits | bigint | 8 | 1 |  |  |  |
| CurbsideSales | decimal | 17 | 1 |  |  |  |
| CurbsideTransactions | bigint | 8 | 1 |  |  |  |
| CurbsideUnits | bigint | 8 | 1 |  |  |  |
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
