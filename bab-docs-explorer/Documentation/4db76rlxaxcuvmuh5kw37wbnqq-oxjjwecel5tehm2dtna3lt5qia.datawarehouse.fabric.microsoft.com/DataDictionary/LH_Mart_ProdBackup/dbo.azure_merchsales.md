# dbo.azure_merchsales

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| FiscalYear | varchar | 8000 | 1 |  |  |  |
| FiscalWeek | varchar | 8000 | 1 |  |  |  |
| NetSalesUnits | int | 4 | 1 |  |  |  |
| NetSalesRetail | decimal | 17 | 1 |  |  |  |
| DateKey | datetime2 | 8 | 1 |  |  |  |
