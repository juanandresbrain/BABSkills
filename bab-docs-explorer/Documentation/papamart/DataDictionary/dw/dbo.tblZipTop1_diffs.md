# dbo.tblZipTop1_diffs

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datestamp | datetime | 8 | 0 |  |  |  |
| country | varchar | 2 | 0 |  |  |  |
| postal_code | varchar | 10 | 0 |  |  |  |
| old_store_key | int | 4 | 1 |  |  |  |
| new_store_key | int | 4 | 1 |  |  |  |
| old_distance | float | 8 | 1 |  |  |  |
| new_distance | float | 8 | 1 |  |  |  |
