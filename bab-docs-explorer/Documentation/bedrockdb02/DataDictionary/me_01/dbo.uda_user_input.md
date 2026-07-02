# dbo.uda_user_input

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| algorithm_id | decimal | 9 | 0 | YES | YES |  |
| user_input_id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| default_value | nvarchar | 100 | 1 |  |  |  |
| min_value | nvarchar | 100 | 1 |  |  |  |
| max_value | nvarchar | 100 | 1 |  |  |  |
| input_editor_id | T_ID | 16 | 0 |  | YES |  |
| visual_location_x | int | 4 | 1 |  |  |  |
| visual_location_y | int | 4 | 1 |  |  |  |
| data_type | smallint | 2 | 0 |  |  |  |
| display_order | smallint | 2 | 1 |  |  |  |
| display_value | nvarchar | 100 | 1 |  |  |  |
| parent_user_input_id | int | 4 | 1 |  |  |  |
| parent_constant_value | nvarchar | 100 | 1 |  |  |  |
| grandparent_constant_value | nvarchar | 100 | 1 |  |  |  |

