# dbo.store_count_area

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_count_area_id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 120 | 0 |  |  |  |
| auditor | nvarchar | 120 | 1 |  |  |  |
| counted_flag | bit | 1 | 0 |  |  |  |
| counted_by_employee_id | decimal | 9 | 1 |  |  |  |
| verified_flag | bit | 1 | 0 |  |  |  |
| store_count_id | decimal | 9 | 0 | YES |  |  |
| total_units_counted | int | 4 | 0 |  |  |  |

