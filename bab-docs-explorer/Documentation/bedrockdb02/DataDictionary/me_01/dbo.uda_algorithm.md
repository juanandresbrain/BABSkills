# dbo.uda_algorithm

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| algorithm_id | decimal | 9 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| last_saved | datetime | 8 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| calculation_level_enum | smallint | 2 | 0 |  |  |  |
| update_stamp | int | 4 | 1 |  |  |  |
| algorithm_type_enum | smallint | 2 | 0 |  |  |  |
| result_expression_id | int | 4 | 1 |  |  |  |
| grading_type_enum | smallint | 2 | 1 |  |  |  |
| secondary_algorithm_id | decimal | 9 | 1 |  |  |  |

