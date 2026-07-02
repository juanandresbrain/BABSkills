# dbo.gl_account_structure

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_account_structure_id | decimal | 9 | 0 | YES |  |  |
| gl_account_structure_label | nvarchar | 120 | 0 |  |  |  |
| gl_import_code | nvarchar | 60 | 0 |  |  |  |
| statistical_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

