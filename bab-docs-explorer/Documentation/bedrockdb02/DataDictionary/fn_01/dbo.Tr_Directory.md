# dbo.Tr_Directory

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| company_id | int | 4 | 0 |  |  |  |
| path | varchar | 255 | 0 |  |  |  |
| done_file_type | int | 4 | 1 |  |  |  |
| done_file_date_time | datetime | 8 | 1 |  |  |  |
| dir_close_date_time | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [fn_01: dbo.Tr_AddPollFile](../../StoredProcedures/fn_01/dbo.Tr_AddPollFile.md)
- [fn_01: dbo.Tr_CloseDir](../../StoredProcedures/fn_01/dbo.Tr_CloseDir.md)
- [fn_01: dbo.Tr_DirError](../../StoredProcedures/fn_01/dbo.Tr_DirError.md)
- [fn_01: dbo.Tr_FileError](../../StoredProcedures/fn_01/dbo.Tr_FileError.md)
- [fn_01: dbo.Tr_GetNextPollFile](../../StoredProcedures/fn_01/dbo.Tr_GetNextPollFile.md)
- [fn_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/fn_01/dbo.Tr_IsDirDoneAndNotClosed.md)
- [fn_01: dbo.Tr_MoveError](../../StoredProcedures/fn_01/dbo.Tr_MoveError.md)
- [fn_01: dbo.Tr_PollFileError](../../StoredProcedures/fn_01/dbo.Tr_PollFileError.md)
- [fn_01: dbo.Tr_ProcessError](../../StoredProcedures/fn_01/dbo.Tr_ProcessError.md)
- [fn_01: dbo.Tr_ShouldWaitOnTPDirs](../../StoredProcedures/fn_01/dbo.Tr_ShouldWaitOnTPDirs.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Tr_AddPollFile](../../StoredProcedures/smartlook_01/dbo.Tr_AddPollFile.md)
- [smartlook_01: dbo.Tr_CloseDir](../../StoredProcedures/smartlook_01/dbo.Tr_CloseDir.md)
- [smartlook_01: dbo.Tr_DirError](../../StoredProcedures/smartlook_01/dbo.Tr_DirError.md)
- [smartlook_01: dbo.Tr_FileError](../../StoredProcedures/smartlook_01/dbo.Tr_FileError.md)
- [smartlook_01: dbo.Tr_GetNextPollFile](../../StoredProcedures/smartlook_01/dbo.Tr_GetNextPollFile.md)
- [smartlook_01: dbo.Tr_IsDirDoneAndNotClosed](../../StoredProcedures/smartlook_01/dbo.Tr_IsDirDoneAndNotClosed.md)
- [smartlook_01: dbo.Tr_MoveError](../../StoredProcedures/smartlook_01/dbo.Tr_MoveError.md)
- [smartlook_01: dbo.Tr_PollFileError](../../StoredProcedures/smartlook_01/dbo.Tr_PollFileError.md)
- [smartlook_01: dbo.Tr_ProcessError](../../StoredProcedures/smartlook_01/dbo.Tr_ProcessError.md)
- [smartlook_01: dbo.Tr_ShouldWaitOnTPDirs](../../StoredProcedures/smartlook_01/dbo.Tr_ShouldWaitOnTPDirs.md)

