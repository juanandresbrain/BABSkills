# dbo.azure_merch_sales

**Database:** LH_Reporting  
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
| DateKey | date | 3 | 1 |  |  |  |
| 26WeekFactor | varchar | 8000 | 1 |  |  |  |
| 52WeekFactor | varchar | 8000 | 1 |  |  |  |
| 8WeekFactor | varchar | 8000 | 1 |  |  |  |
| PoundConversion | float | 8 | 1 |  |  |  |
| YuanConversion | float | 8 | 1 |  |  |  |
