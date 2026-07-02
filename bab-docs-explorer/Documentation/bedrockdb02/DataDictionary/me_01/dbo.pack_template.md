# dbo.pack_template

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pack_template_id | int | 4 | 0 | YES |  |  |
| template_code | nvarchar | 40 | 0 |  |  |  |
| short_description | nvarchar | 100 | 0 |  |  |  |
| long_description | nvarchar | 240 | 0 |  |  |  |
| size_category_id | decimal | 9 | 0 |  |  |  |
| size_grid_id | decimal | 9 | 1 |  |  |  |
| color_count | smallint | 2 | 0 |  |  |  |
| total_template_quantity | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

