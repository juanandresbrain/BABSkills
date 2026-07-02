# dbo.count_import_def

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| count_import_def_id | decimal | 9 | 0 | YES |  |  |
| count_import_def_code | nvarchar | 16 | 0 |  |  |  |
| count_import_def_desc | nvarchar | 120 | 0 |  |  |  |
| import_type | smallint | 2 | 0 |  |  |  |
| delimiter | nvarchar | 2 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |

