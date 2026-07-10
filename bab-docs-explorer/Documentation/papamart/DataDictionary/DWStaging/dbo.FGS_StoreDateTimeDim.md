# dbo.FGS_StoreDateTimeDim

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreName | varchar | 100 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| BusinessHour | int | 4 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| FiscalYear | int | 4 | 1 |  |  |  |
| FiscalMonth | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 52 | 1 |  |  |  |
| TradingGroup | varchar | 52 | 1 |  |  |  |
| Jurisdiction | varchar | 52 | 1 |  |  |  |
