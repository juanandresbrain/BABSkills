# dbo.gl_account_structure_dtl

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_account_structure_dtl_id | decimal | 9 | 0 | YES |  |  |
| gl_account_structure_id | decimal | 9 | 0 |  |  |  |
| bookmark | nvarchar | 20 | 0 |  |  |  |
| leading_key | nvarchar | 20 | 1 |  |  |  |
| no_of_characters | tinyint | 1 | 0 |  |  |  |
| structure_type | tinyint | 1 | 0 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| constant_label | nvarchar | 120 | 1 |  |  |  |

