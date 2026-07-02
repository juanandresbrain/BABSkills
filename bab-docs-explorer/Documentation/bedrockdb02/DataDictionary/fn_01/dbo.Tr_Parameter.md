# dbo.Tr_Parameter

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_key | varchar | 30 | 0 |  |  |  |
| parameter_value | varchar | 50 | 0 |  |  |  |
| company_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [fn_01: dbo.Tr_DirError](../../StoredProcedures/fn_01/dbo.Tr_DirError.md)
- [fn_01: dbo.Tr_FileError](../../StoredProcedures/fn_01/dbo.Tr_FileError.md)
- [fn_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/fn_01/dbo.Tr_IsDirDoneAndNotClosed.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Tr_DirError](../../StoredProcedures/smartlook_01/dbo.Tr_DirError.md)
- [smartlook_01: dbo.Tr_FileError](../../StoredProcedures/smartlook_01/dbo.Tr_FileError.md)
- [smartlook_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/smartlook_01/dbo.Tr_IsDirDoneAndNotClosed.md)

