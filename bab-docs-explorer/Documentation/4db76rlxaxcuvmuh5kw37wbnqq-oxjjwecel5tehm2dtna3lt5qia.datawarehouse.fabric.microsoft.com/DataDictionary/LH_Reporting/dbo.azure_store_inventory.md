# dbo.azure_store_inventory

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| WorkYear | varchar | 8000 | 1 |  |  |  |
| WorkWeek | varchar | 8000 | 1 |  |  |  |
| DateKey | date | 3 | 1 |  |  |  |
| CHAIN Available | bigint | 8 | 1 |  |  |  |
| OUTLET Available | bigint | 8 | 1 |  |  |  |
| Store Allocated | bigint | 8 | 1 |  |  |  |
| Store Damaged | bigint | 8 | 1 |  |  |  |
| Store Discrepancy | bigint | 8 | 1 |  |  |  |
| Store In Transit | bigint | 8 | 1 |  |  |  |
| Store Pending Shrink | bigint | 8 | 1 |  |  |  |
| Store Reserved Cust Order | bigint | 8 | 1 |  |  |  |
| WEB Available | bigint | 8 | 1 |  |  |  |
