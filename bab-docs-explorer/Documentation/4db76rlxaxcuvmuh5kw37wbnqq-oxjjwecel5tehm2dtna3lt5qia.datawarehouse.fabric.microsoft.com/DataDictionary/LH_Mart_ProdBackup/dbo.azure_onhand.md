# dbo.azure_onhand

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| workYear | varchar | 8000 | 1 |  |  |  |
| workweek | varchar | 8000 | 1 |  |  |  |
| Inv_Status | varchar | 8000 | 1 |  |  |  |
| OnHandCost | decimal | 9 | 1 |  |  |  |
| LocationType | varchar | 8000 | 1 |  |  |  |
