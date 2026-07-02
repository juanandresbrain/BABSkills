# dbo.SnapshotData

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| CreatedDate | datetime | 8 | 0 |  |  |  |
| ParamsHash | int | 4 | 1 |  |  |  |
| QueryParams | ntext | 256 | 1 |  |  |  |
| EffectiveParams | ntext | 256 | 1 |  |  |  |
| Description | nvarchar | 1024 | 1 |  |  |  |
| DependsOnUser | bit | 1 | 1 |  |  |  |
| PermanentRefcount | int | 4 | 0 |  |  |  |
| TransientRefcount | int | 4 | 0 |  |  |  |
| ExpirationDate | datetime | 8 | 0 |  |  |  |
| PageCount | int | 4 | 1 |  |  |  |
| HasDocMap | bit | 1 | 1 |  |  |  |
| Machine | nvarchar | 1024 | 0 |  |  |  |
| PaginationMode | smallint | 2 | 1 |  |  |  |
| ProcessingFlags | int | 4 | 1 |  |  |  |
| IsCached | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.AddHistoryRecord](../../StoredProcedures/ReportServerBIRPT02/dbo.AddHistoryRecord.md)
- [ReportServerBIRPT02: dbo.AddReportToCache](../../StoredProcedures/ReportServerBIRPT02/dbo.AddReportToCache.md)
- [ReportServerBIRPT02: dbo.CleanBrokenSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanBrokenSnapshots.md)
- [ReportServerBIRPT02: dbo.CleanExpiredCache](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredCache.md)
- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredSessions.md)
- [ReportServerBIRPT02: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanOrphanedSnapshots.md)
- [ReportServerBIRPT02: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunksOfType.md)
- [ReportServerBIRPT02: dbo.CreateEditSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateEditSession.md)
- [ReportServerBIRPT02: dbo.CreateNewSnapshotVersion](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateNewSnapshotVersion.md)
- [ReportServerBIRPT02: dbo.CreateObject](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateObject.md)
- [ReportServerBIRPT02: dbo.CreateSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSession.md)
- [ReportServerBIRPT02: dbo.DecreaseTransientSnapshotRefcount](../../StoredProcedures/ReportServerBIRPT02/dbo.DecreaseTransientSnapshotRefcount.md)
- [ReportServerBIRPT02: dbo.DeleteObject](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteObject.md)
- [ReportServerBIRPT02: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerBIRPT02: dbo.DereferenceSessionSnapshot](../../StoredProcedures/ReportServerBIRPT02/dbo.DereferenceSessionSnapshot.md)
- [ReportServerBIRPT02: dbo.EnforceCacheLimits](../../StoredProcedures/ReportServerBIRPT02/dbo.EnforceCacheLimits.md)
- [ReportServerBIRPT02: dbo.FlushCacheByID](../../StoredProcedures/ReportServerBIRPT02/dbo.FlushCacheByID.md)
- [ReportServerBIRPT02: dbo.FlushReportFromCache](../../StoredProcedures/ReportServerBIRPT02/dbo.FlushReportFromCache.md)
- [ReportServerBIRPT02: dbo.GetDataSetForExecution](../../StoredProcedures/ReportServerBIRPT02/dbo.GetDataSetForExecution.md)
- [ReportServerBIRPT02: dbo.GetReportForExecution](../../StoredProcedures/ReportServerBIRPT02/dbo.GetReportForExecution.md)
- [ReportServerBIRPT02: dbo.GetSessionData](../../StoredProcedures/ReportServerBIRPT02/dbo.GetSessionData.md)
- [ReportServerBIRPT02: dbo.GetSnapshotFromHistory](../../StoredProcedures/ReportServerBIRPT02/dbo.GetSnapshotFromHistory.md)
- [ReportServerBIRPT02: dbo.GetSnapshotPromotedInfo](../../StoredProcedures/ReportServerBIRPT02/dbo.GetSnapshotPromotedInfo.md)
- [ReportServerBIRPT02: dbo.IncreaseTransientSnapshotRefcount](../../StoredProcedures/ReportServerBIRPT02/dbo.IncreaseTransientSnapshotRefcount.md)
- [ReportServerBIRPT02: dbo.InsertUnreferencedSnapshot](../../StoredProcedures/ReportServerBIRPT02/dbo.InsertUnreferencedSnapshot.md)
- [ReportServerBIRPT02: dbo.LoadForDefinitionCheck](../../StoredProcedures/ReportServerBIRPT02/dbo.LoadForDefinitionCheck.md)
- [ReportServerBIRPT02: dbo.LoadForRepublishing](../../StoredProcedures/ReportServerBIRPT02/dbo.LoadForRepublishing.md)
- [ReportServerBIRPT02: dbo.MarkSnapshotAsDependentOnUser](../../StoredProcedures/ReportServerBIRPT02/dbo.MarkSnapshotAsDependentOnUser.md)
- [ReportServerBIRPT02: dbo.PromoteSnapshotInfo](../../StoredProcedures/ReportServerBIRPT02/dbo.PromoteSnapshotInfo.md)
- [ReportServerBIRPT02: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveSegmentedMapping.md)
- [ReportServerBIRPT02: dbo.SetExecutionOptions](../../StoredProcedures/ReportServerBIRPT02/dbo.SetExecutionOptions.md)
- [ReportServerBIRPT02: dbo.SetObjectContent](../../StoredProcedures/ReportServerBIRPT02/dbo.SetObjectContent.md)
- [ReportServerBIRPT02: dbo.SetSessionData](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSessionData.md)
- [ReportServerBIRPT02: dbo.SetSnapshotProcessingFlags](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSnapshotProcessingFlags.md)
- [ReportServerBIRPT02: dbo.UpdateCompiledDefinition](../../StoredProcedures/ReportServerBIRPT02/dbo.UpdateCompiledDefinition.md)
- [ReportServerBIRPT02: dbo.UpdateSnapshot](../../StoredProcedures/ReportServerBIRPT02/dbo.UpdateSnapshot.md)
- [ReportServerBIRPT02: dbo.UpdateSnapshotPaginationInfo](../../StoredProcedures/ReportServerBIRPT02/dbo.UpdateSnapshotPaginationInfo.md)
- [ReportServerBIRPT02: dbo.UpdateSnapshotReferences](../../StoredProcedures/ReportServerBIRPT02/dbo.UpdateSnapshotReferences.md)

