# dbo.Sv_Output

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 | YES |  |  |
| object_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| execution_date | smalldatetime | 4 | 0 |  |  |  |
| page_count | int | 4 | 0 |  |  |  |
| printed_count | smallint | 2 | 0 |  |  |  |
| previewed_count | smallint | 2 | 0 |  |  |  |
| expires | smalldatetime | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 1 |  |  |  |
| query_label | varchar | 80 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CompleteSchedule](../../StoredProcedures/fn_01/dbo.Sv_CompleteSchedule.md)
- [fn_01: dbo.Sv_DeleteObjectOutput](../../StoredProcedures/fn_01/dbo.Sv_DeleteObjectOutput.md)
- [fn_01: dbo.Sv_DeleteOldOutputs](../../StoredProcedures/fn_01/dbo.Sv_DeleteOldOutputs.md)
- [fn_01: dbo.Sv_DeleteOutput](../../StoredProcedures/fn_01/dbo.Sv_DeleteOutput.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_CompleteSchedule](../../StoredProcedures/smartlook_01/dbo.Sv_CompleteSchedule.md)
- [smartlook_01: dbo.Sv_DeleteObjectOutput](../../StoredProcedures/smartlook_01/dbo.Sv_DeleteObjectOutput.md)
- [smartlook_01: dbo.Sv_DeleteOldOutputs](../../StoredProcedures/smartlook_01/dbo.Sv_DeleteOldOutputs.md)
- [smartlook_01: dbo.Sv_DeleteOutput](../../StoredProcedures/smartlook_01/dbo.Sv_DeleteOutput.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

