# dbo.AW_MAUnitCost_Dynamics

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | varchar | 30 | 1 |  |  |  |
| store_key | varchar | 30 | 1 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| netCost | money | 8 | 1 |  |  |  |
| netUnits | int | 4 | 1 |  |  |  |
| unitCost | money | 8 | 1 |  |  |  |
| return_units | int | 4 | 0 |  |  |  |
| prior_date_key | int | 4 | 1 |  |  |  |
