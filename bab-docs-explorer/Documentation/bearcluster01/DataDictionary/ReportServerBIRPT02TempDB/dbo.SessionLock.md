# dbo.SessionLock

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | varchar | 32 | 0 |  |  |  |
| LockVersion | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CheckSessionLock](../../StoredProcedures/ReportServerBIRPT02/dbo.CheckSessionLock.md)
- [ReportServerBIRPT02: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredSessions.md)
- [ReportServerBIRPT02: dbo.CreateSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSession.md)
- [ReportServerBIRPT02: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveReportFromSession.md)
- [ReportServerBIRPT02: dbo.WriteLockSession](../../StoredProcedures/ReportServerBIRPT02/dbo.WriteLockSession.md)

