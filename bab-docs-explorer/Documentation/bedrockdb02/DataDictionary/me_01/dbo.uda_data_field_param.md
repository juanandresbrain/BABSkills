# dbo.uda_data_field_param

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| algorithm_id | decimal | 9 | 0 | YES | YES |  |
| data_id | int | 4 | 0 | YES | YES |  |
| param_id | T_ID | 16 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| value | nvarchar | 104 | 1 |  |  |  |
| user_input_id | int | 4 | 1 |  |  |  |
| display_value | nvarchar | 100 | 1 |  |  |  |

