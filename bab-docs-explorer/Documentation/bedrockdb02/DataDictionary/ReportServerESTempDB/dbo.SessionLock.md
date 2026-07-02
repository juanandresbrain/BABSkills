# dbo.SessionLock

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | varchar | 32 | 0 |  |  |  |
| LockVersion | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.CheckSessionLock](../../StoredProcedures/ReportServerES/dbo.CheckSessionLock.md)
- [ReportServerES: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredSessions.md)
- [ReportServerES: dbo.CreateSession](../../StoredProcedures/ReportServerES/dbo.CreateSession.md)
- [ReportServerES: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerES/dbo.RemoveReportFromSession.md)
- [ReportServerES: dbo.WriteLockSession](../../StoredProcedures/ReportServerES/dbo.WriteLockSession.md)

