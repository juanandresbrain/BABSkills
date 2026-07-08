# dbo.Md_ListItem

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| list_id | int | 4 | 0 |  |  |  |
| list_item_sequence | smallint | 2 | 0 |  |  |  |
| list_item_label_1 | varchar | 30 | 0 |  |  |  |
| list_item_label_2 | varchar | 30 | 0 |  |  |  |
| list_item_value | varchar | 30 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| list_item_resource_name | nvarchar | 510 | 1 |  |  |  |
