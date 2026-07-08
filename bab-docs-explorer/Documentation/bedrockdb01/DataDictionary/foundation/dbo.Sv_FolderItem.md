# dbo.Sv_FolderItem

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folder_id | int | 4 | 0 |  |  |  |
| item_sequence | smallint | 2 | 0 |  |  |  |
| item_type | smallint | 2 | 0 |  |  |  |
| item_id | int | 4 | 0 |  |  |  |
| output_data | varchar | 100 | 1 |  |  |  |
| crosstab_data | varchar | 100 | 1 |  |  |  |
| graph_data | varchar | 100 | 1 |  |  |  |
| default_data_view | char | 1 | 0 |  |  |  |
