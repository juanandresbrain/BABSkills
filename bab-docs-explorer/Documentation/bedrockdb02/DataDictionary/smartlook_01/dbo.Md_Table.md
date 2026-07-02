# dbo.Md_Table

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_id | int | 4 | 0 | YES |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| pre_code | text | 16 | 1 |  |  |  |
| post_code | text | 16 | 1 |  |  |  |
| db_alias_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| apply_period | bit | 1 | 0 |  |  |  |
| multiple_names | bit | 1 | 0 |  |  |  |
| priority | int | 4 | 1 |  |  |  |
| note | varchar | 60 | 1 |  |  |  |
| where_clause | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_GetMiddleTable1](../../StoredProcedures/fn_01/dbo.Md_GetMiddleTable1.md)
- [fn_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/fn_01/dbo.Md_PrepareTableLinks.md)
- [fn_01: dbo.Md_UpdateExtendedField](../../StoredProcedures/fn_01/dbo.Md_UpdateExtendedField.md)
- [smartlook_01: dbo.Md_GetMiddleTable1](../../StoredProcedures/smartlook_01/dbo.Md_GetMiddleTable1.md)
- [smartlook_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/smartlook_01/dbo.Md_PrepareTableLinks.md)

