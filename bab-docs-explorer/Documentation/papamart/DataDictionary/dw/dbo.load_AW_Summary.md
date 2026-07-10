# dbo.load_AW_Summary

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store | int | 4 | 0 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| aw_units | decimal | 9 | 1 |  |  |  |
| dm_units | decimal | 9 | 1 |  |  |  |
| aw_sales | decimal | 9 | 1 |  |  |  |
| dm_sales | decimal | 9 | 1 |  |  |  |
| unit_diff | decimal | 9 | 1 |  |  |  |
| unit_pct_diff | decimal | 9 | 1 |  |  |  |
| sales_diff | decimal | 9 | 1 |  |  |  |
| sales_pct_diff | decimal | 9 | 1 |  |  |  |
