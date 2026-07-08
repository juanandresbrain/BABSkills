# dbo.message_list_item

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| list_id | smallint | 2 | 0 |  |  |  |
| list_item_no | smallint | 2 | 0 |  |  |  |
| sort_seq | tinyint | 1 | 0 |  |  |  |
| list_item_display_descr | nvarchar | 100 | 0 |  |  |  |
| list_item_system_descr | nvarchar | 100 | 0 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
