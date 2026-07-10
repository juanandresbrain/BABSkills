# dbo.merchSales_view_stage_padded

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 0 |  |  |  |
| StoreKey | int | 4 | 0 |  |  |  |
| FiscalYear | varchar | 4 | 1 |  |  |  |
| FiscalWeek | varchar | 2 | 1 |  |  |  |
| NetSalesUnits | numeric | 9 | 1 |  |  |  |
| NetSalesRetail | numeric | 17 | 1 |  |  |  |
| DateKey | datetime | 8 | 1 |  |  |  |
