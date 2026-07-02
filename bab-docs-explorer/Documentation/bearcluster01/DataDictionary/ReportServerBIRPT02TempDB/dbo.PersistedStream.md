# dbo.PersistedStream

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | varchar | 32 | 0 | YES |  |  |
| Index | int | 4 | 0 | YES |  |  |
| Content | image | 16 | 1 |  |  |  |
| Name | nvarchar | 520 | 1 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| Extension | nvarchar | 520 | 1 |  |  |  |
| Encoding | nvarchar | 520 | 1 |  |  |  |
| Error | nvarchar | 1024 | 1 |  |  |  |
| RefCount | int | 4 | 0 |  |  |  |
| ExpirationDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.AddPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.AddPersistedStream.md)
- [ReportServerBIRPT02: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredSessions.md)
- [ReportServerBIRPT02: dbo.CreateSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSession.md)
- [ReportServerBIRPT02: dbo.DeleteExpiredPersistedStreams](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteExpiredPersistedStreams.md)
- [ReportServerBIRPT02: dbo.DeletePersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.DeletePersistedStream.md)
- [ReportServerBIRPT02: dbo.DeletePersistedStreams](../../StoredProcedures/ReportServerBIRPT02/dbo.DeletePersistedStreams.md)
- [ReportServerBIRPT02: dbo.GetFirstPortionPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.GetFirstPortionPersistedStream.md)
- [ReportServerBIRPT02: dbo.GetNextPortionPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.GetNextPortionPersistedStream.md)
- [ReportServerBIRPT02: dbo.LockPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.LockPersistedStream.md)
- [ReportServerBIRPT02: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveReportFromSession.md)
- [ReportServerBIRPT02: dbo.SetPersistedStreamError](../../StoredProcedures/ReportServerBIRPT02/dbo.SetPersistedStreamError.md)
- [ReportServerBIRPT02: dbo.SetSessionData](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSessionData.md)
- [ReportServerBIRPT02: dbo.WriteFirstPortionPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.WriteFirstPortionPersistedStream.md)
- [ReportServerBIRPT02: dbo.WriteNextPortionPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.WriteNextPortionPersistedStream.md)

