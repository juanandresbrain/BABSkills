# dbo.Ex_OutputNumber

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| file_number | numeric | 9 | 0 |  |  |  |
| object_id | int | 4 | 1 |  |  |  |
| db_group_id | int | 4 | 1 |  |  |  |
| last_updated | smalldatetime | 4 | 1 |  |  |  |
| reset_flag | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Ex_GetNextFileNum](../../StoredProcedures/fn_01/dbo.Ex_GetNextFileNum.md)
- [smartlook_01: dbo.Ex_GetNextFileNum](../../StoredProcedures/smartlook_01/dbo.Ex_GetNextFileNum.md)

