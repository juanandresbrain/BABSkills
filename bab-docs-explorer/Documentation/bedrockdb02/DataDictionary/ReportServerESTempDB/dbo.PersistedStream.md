# dbo.PersistedStream

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

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

- [ReportServerES: dbo.AddPersistedStream](../../StoredProcedures/ReportServerES/dbo.AddPersistedStream.md)
- [ReportServerES: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredSessions.md)
- [ReportServerES: dbo.CreateSession](../../StoredProcedures/ReportServerES/dbo.CreateSession.md)
- [ReportServerES: dbo.DeleteExpiredPersistedStreams](../../StoredProcedures/ReportServerES/dbo.DeleteExpiredPersistedStreams.md)
- [ReportServerES: dbo.DeletePersistedStream](../../StoredProcedures/ReportServerES/dbo.DeletePersistedStream.md)
- [ReportServerES: dbo.DeletePersistedStreams](../../StoredProcedures/ReportServerES/dbo.DeletePersistedStreams.md)
- [ReportServerES: dbo.GetFirstPortionPersistedStream](../../StoredProcedures/ReportServerES/dbo.GetFirstPortionPersistedStream.md)
- [ReportServerES: dbo.GetNextPortionPersistedStream](../../StoredProcedures/ReportServerES/dbo.GetNextPortionPersistedStream.md)
- [ReportServerES: dbo.LockPersistedStream](../../StoredProcedures/ReportServerES/dbo.LockPersistedStream.md)
- [ReportServerES: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerES/dbo.RemoveReportFromSession.md)
- [ReportServerES: dbo.SetPersistedStreamError](../../StoredProcedures/ReportServerES/dbo.SetPersistedStreamError.md)
- [ReportServerES: dbo.SetSessionData](../../StoredProcedures/ReportServerES/dbo.SetSessionData.md)
- [ReportServerES: dbo.WriteFirstPortionPersistedStream](../../StoredProcedures/ReportServerES/dbo.WriteFirstPortionPersistedStream.md)
- [ReportServerES: dbo.WriteNextPortionPersistedStream](../../StoredProcedures/ReportServerES/dbo.WriteNextPortionPersistedStream.md)

