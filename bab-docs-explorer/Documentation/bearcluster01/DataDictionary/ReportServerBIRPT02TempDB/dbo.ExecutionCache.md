# dbo.ExecutionCache

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

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

- [ReportServerBIRPT02: dbo.AddReportToCache](../../StoredProcedures/ReportServerBIRPT02/dbo.AddReportToCache.md)
- [ReportServerBIRPT02: dbo.CleanExpiredCache](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredCache.md)
- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.CreateOrUpdateContentCache](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateOrUpdateContentCache.md)
- [ReportServerBIRPT02: dbo.DeleteObject](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteObject.md)
- [ReportServerBIRPT02: dbo.EnforceCacheLimits](../../StoredProcedures/ReportServerBIRPT02/dbo.EnforceCacheLimits.md)
- [ReportServerBIRPT02: dbo.FlushCacheByID](../../StoredProcedures/ReportServerBIRPT02/dbo.FlushCacheByID.md)
- [ReportServerBIRPT02: dbo.FlushReportFromCache](../../StoredProcedures/ReportServerBIRPT02/dbo.FlushReportFromCache.md)
- [ReportServerBIRPT02: dbo.GetDataSetForExecution](../../StoredProcedures/ReportServerBIRPT02/dbo.GetDataSetForExecution.md)
- [ReportServerBIRPT02: dbo.GetReportForExecution](../../StoredProcedures/ReportServerBIRPT02/dbo.GetReportForExecution.md)
- [ReportServerBIRPT02: dbo.SetCacheLastUsed](../../StoredProcedures/ReportServerBIRPT02/dbo.SetCacheLastUsed.md)
- [ReportServerBIRPT02: dbo.UpdateSnapshotReferences](../../StoredProcedures/ReportServerBIRPT02/dbo.UpdateSnapshotReferences.md)

