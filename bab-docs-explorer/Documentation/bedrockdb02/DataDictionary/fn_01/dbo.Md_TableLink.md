# dbo.Md_TableLink

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| from_table_id | int | 4 | 0 | YES |  |  |
| from_exp | varchar | 100 | 0 |  |  |  |
| join_exp | varchar | 255 | 0 |  |  |  |
| to_table_id | int | 4 | 0 | YES |  |  |
| to_exp | varchar | 100 | 0 |  |  |  |
| temp_table_id | int | 4 | 0 | YES |  |  |
| temp_join_exp | varchar | 255 | 1 |  |  |  |
| from_temp_exp | varchar | 100 | 1 |  |  |  |
| temp_to_exp | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/fn_01/dbo.Md_PrepareTableLinks.md)
- [smartlook_01: dbo.Md_PrepareTableLinks](../../StoredProcedures/smartlook_01/dbo.Md_PrepareTableLinks.md)

