# dbo.Ld_AWtoDWprep

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 0 |  |  |  |
| Date | datetime | 8 | 0 |  |  |  |
| aw_units | numeric | 17 | 1 |  |  |  |
| dm_units | int | 4 | 1 |  |  |  |
| aw_sales | numeric | 17 | 1 |  |  |  |
| dm_sales | decimal | 17 | 1 |  |  |  |
| UnitDiff | numeric | 17 | 1 |  |  |  |
| UnitPctDiff | numeric | 17 | 1 |  |  |  |
| SalesDiff | numeric | 17 | 1 |  |  |  |
| SalesPctDiff | numeric | 17 | 1 |  |  |  |
