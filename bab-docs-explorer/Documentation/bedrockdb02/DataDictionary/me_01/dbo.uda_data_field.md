# dbo.uda_data_field

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| algorithm_id | decimal | 9 | 0 | YES | YES |  |
| data_id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| data_retriever_id | T_ID | 16 | 0 |  | YES |  |
| visual_location_x | int | 4 | 1 |  |  |  |
| visual_location_y | int | 4 | 1 |  |  |  |
| display_order | smallint | 2 | 1 |  |  |  |

