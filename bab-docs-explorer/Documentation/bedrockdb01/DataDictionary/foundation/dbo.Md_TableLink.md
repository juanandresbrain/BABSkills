# dbo.Md_TableLink

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| from_table_id | int | 4 | 0 |  |  |  |
| from_exp | varchar | 100 | 0 |  |  |  |
| join_exp | varchar | 255 | 0 |  |  |  |
| to_table_id | int | 4 | 0 |  |  |  |
| to_exp | varchar | 100 | 0 |  |  |  |
| temp_table_id | int | 4 | 0 |  |  |  |
| temp_join_exp | varchar | 255 | 1 |  |  |  |
| from_temp_exp | varchar | 100 | 1 |  |  |  |
| temp_to_exp | varchar | 100 | 1 |  |  |  |
