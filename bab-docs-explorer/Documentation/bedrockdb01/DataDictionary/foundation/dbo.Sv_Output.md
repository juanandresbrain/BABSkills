# dbo.Sv_Output

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| execution_date | smalldatetime | 4 | 0 |  |  |  |
| page_count | int | 4 | 0 |  |  |  |
| printed_count | smallint | 2 | 0 |  |  |  |
| previewed_count | smallint | 2 | 0 |  |  |  |
| expires | smalldatetime | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 1 |  |  |  |
| query_label | varchar | 80 | 1 |  |  |  |
