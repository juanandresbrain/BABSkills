# dbo.work_TYLYresults

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| metric_dim_key | int | 4 | 0 |  |  |  |
| metric_facts_key | bigint | 8 | 0 |  |  |  |
| date_key_TY | int | 4 | 0 |  |  |  |
| date_key_LY | int | 4 | 1 |  |  |  |
| LYamount | decimal | 9 | 1 |  |  |  |
