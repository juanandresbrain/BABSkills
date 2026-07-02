# dbo.ExecutionCache

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExecutionCacheID | uniqueidentifier | 16 | 0 | YES |  |  |
| ReportID | uniqueidentifier | 16 | 0 |  |  |  |
| ExpirationFlags | int | 4 | 0 |  |  |  |
| AbsoluteExpiration | datetime | 8 | 1 |  |  |  |
| RelativeExpiration | int | 4 | 1 |  |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| LastUsedTime | datetime | 8 | 0 |  |  |  |
| ParamsHash | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.AddReportToCache](../../StoredProcedures/ReportServerES/dbo.AddReportToCache.md)
- [ReportServerES: dbo.CleanExpiredCache](../../StoredProcedures/ReportServerES/dbo.CleanExpiredCache.md)
- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.DeleteObject](../../StoredProcedures/ReportServerES/dbo.DeleteObject.md)
- [ReportServerES: dbo.EnforceCacheLimits](../../StoredProcedures/ReportServerES/dbo.EnforceCacheLimits.md)
- [ReportServerES: dbo.FlushCacheByID](../../StoredProcedures/ReportServerES/dbo.FlushCacheByID.md)
- [ReportServerES: dbo.FlushReportFromCache](../../StoredProcedures/ReportServerES/dbo.FlushReportFromCache.md)
- [ReportServerES: dbo.GetDataSetForExecution](../../StoredProcedures/ReportServerES/dbo.GetDataSetForExecution.md)
- [ReportServerES: dbo.GetReportForExecution](../../StoredProcedures/ReportServerES/dbo.GetReportForExecution.md)
- [ReportServerES: dbo.SetCacheLastUsed](../../StoredProcedures/ReportServerES/dbo.SetCacheLastUsed.md)
- [ReportServerES: dbo.UpdateSnapshotReferences](../../StoredProcedures/ReportServerES/dbo.UpdateSnapshotReferences.md)

