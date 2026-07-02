# dbo.inventory_queued_import

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_no | nvarchar | 40 | 0 | YES |  |  |
| inventory_queue_item_id | int | 4 | 0 | YES |  |  |
| replace_or_increment | smallint | 2 | 0 |  |  |  |
| delimiter | nvarchar | 2 | 0 |  |  |  |
| sql_column_list | nvarchar | 4000 | 0 |  |  |  |
| inventory_queue_item_status | tinyint | 1 | 0 |  |  |  |
| count_data_file | nvarchar | -1 | 0 |  |  |  |
| count_format_file | nvarchar | -1 | 0 |  |  |  |
| count_error_file | nvarchar | -1 | 0 |  |  |  |
| import_error | nvarchar | -1 | 1 |  |  |  |

