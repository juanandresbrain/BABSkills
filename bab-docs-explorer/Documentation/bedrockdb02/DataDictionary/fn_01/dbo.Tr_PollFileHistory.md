# dbo.Tr_PollFileHistory

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| dir_id | int | 4 | 0 |  |  |  |
| filename | varchar | 30 | 0 |  |  |  |
| output_mask | varchar | 30 | 1 |  |  |  |
| execution_id | int | 4 | 1 |  |  |  |
| file_size | int | 4 | 0 |  |  |  |
| transactions | int | 4 | 1 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| translate_type | int | 4 | 1 |  |  |  |
| translate_version | int | 4 | 1 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| history_date_time | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [fn_01: dbo.Tr_ClosePollFile](../../StoredProcedures/fn_01/dbo.Tr_ClosePollFile.md)
- [fn_01: dbo.Tr_DirError](../../StoredProcedures/fn_01/dbo.Tr_DirError.md)
- [fn_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/fn_01/dbo.Tr_IsDirDoneAndNotClosed.md)
- [fn_01: dbo.Tr_MoveError](../../StoredProcedures/fn_01/dbo.Tr_MoveError.md)
- [fn_01: dbo.Tr_PollFileError](../../StoredProcedures/fn_01/dbo.Tr_PollFileError.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Tr_ClosePollFile](../../StoredProcedures/smartlook_01/dbo.Tr_ClosePollFile.md)
- [smartlook_01: dbo.Tr_DirError](../../StoredProcedures/smartlook_01/dbo.Tr_DirError.md)
- [smartlook_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/smartlook_01/dbo.Tr_IsDirDoneAndNotClosed.md)
- [smartlook_01: dbo.Tr_MoveError](../../StoredProcedures/smartlook_01/dbo.Tr_MoveError.md)
- [smartlook_01: dbo.Tr_PollFileError](../../StoredProcedures/smartlook_01/dbo.Tr_PollFileError.md)

