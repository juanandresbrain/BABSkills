# dbo.Sv_OutputIndex

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 |  |  |  |
| sequence | int | 4 | 0 |  |  |  |
| index_level | int | 4 | 0 |  |  |  |
| index_type | tinyint | 1 | 0 |  |  |  |
| index_data | varchar | 100 | 1 |  |  |  |
| page_number | int | 4 | 0 |  |  |  |
| position | int | 4 | 0 |  |  |  |
| index_field_id | int | 4 | 1 |  |  |  |
| index_node_id | int | 4 | 1 |  |  |  |

