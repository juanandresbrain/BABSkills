# dbo.import_style_color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_color_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| color_short_description | nvarchar | 16 | 1 |  |  |  |
| color_long_description | nvarchar | 40 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| price_status_code | nvarchar | 6 | 1 |  |  |  |
| fashion_flag | nchar | 2 | 1 |  |  |  |
| reorder_flag | nchar | 2 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

