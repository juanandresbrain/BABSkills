# dbo.tmpDynSalesTotals

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| SalesBucket | varchar | 12 | 1 |  |  |  |
| SumDynUnitGrossAmount | numeric | 17 | 1 |  |  |  |
| SumDynUnitDiscAmt | numeric | 17 | 1 |  |  |  |
| MinTransDate | date | 3 | 1 |  |  |  |
| MaxTransDate | date | 3 | 1 |  |  |  |
| SumDynSalesTotal | numeric | 17 | 1 |  |  |  |
