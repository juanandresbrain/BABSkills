# dbo.uda_expression

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| algorithm_id | decimal | 9 | 0 | YES | YES |  |
| expression_id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| expression | nvarchar | -1 | 0 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| visual_location_x | int | 4 | 1 |  |  |  |
| visual_location_y | int | 4 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| display_order | smallint | 2 | 1 |  |  |  |

