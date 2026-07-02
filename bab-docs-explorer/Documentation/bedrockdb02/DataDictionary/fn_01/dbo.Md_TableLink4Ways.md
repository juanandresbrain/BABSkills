# dbo.Md_TableLink4Ways

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 |  |  |  |
| from_table_id | int | 4 | 0 |  |  |  |
| middle_table_id1 | int | 4 | 0 |  |  |  |
| middle_table_id2 | int | 4 | 0 |  |  |  |
| to_table_id | int | 4 | 0 |  |  |  |
| exclusive_count | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/fn_01/dbo.Md_PrepareTableLinks.md)
- [smartlook_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/smartlook_01/dbo.Md_PrepareTableLinks.md)

