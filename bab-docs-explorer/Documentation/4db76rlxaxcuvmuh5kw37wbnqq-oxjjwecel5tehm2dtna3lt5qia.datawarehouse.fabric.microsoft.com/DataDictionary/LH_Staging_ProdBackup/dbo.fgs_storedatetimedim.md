# dbo.fgs_storedatetimedim

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| BusinessHour | int | 4 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| FiscalYear | int | 4 | 1 |  |  |  |
| FiscalMonth | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
