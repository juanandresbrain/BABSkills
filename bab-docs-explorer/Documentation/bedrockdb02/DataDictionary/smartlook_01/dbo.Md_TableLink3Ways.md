# dbo.Md_TableLink3Ways

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 |  |  |  |
| from_table_id | int | 4 | 0 |  |  |  |
| middle_table_id1 | int | 4 | 0 |  |  |  |
| to_table_id | int | 4 | 0 |  |  |  |
| exclusive_count | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_GetMiddleTable1](../../StoredProcedures/fn_01/dbo.Md_GetMiddleTable1.md)
- [fn_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/fn_01/dbo.Md_PrepareTableLinks.md)
- [smartlook_01: dbo.Md_GetMiddleTable1](../../StoredProcedures/smartlook_01/dbo.Md_GetMiddleTable1.md)
- [smartlook_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/smartlook_01/dbo.Md_PrepareTableLinks.md)

