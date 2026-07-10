# dbo.tmpDwSalesTotals

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 5 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  |  |
| SumUnitGrossAmt | numeric | 17 | 1 |  |  |  |
| SumUnitDiscAmt | numeric | 17 | 1 |  |  |  |
| SumUpsellDiscAllocated | money | 8 | 1 |  |  |  |
| MinTransDate | datetime | 8 | 1 |  |  |  |
| MaxTransDate | datetime | 8 | 1 |  |  |  |
| SumSalesTotal | numeric | 17 | 1 |  |  |  |
