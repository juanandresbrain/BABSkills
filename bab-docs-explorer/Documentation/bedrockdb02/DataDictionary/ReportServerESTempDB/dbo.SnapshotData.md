# dbo.SnapshotData

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

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

- [ReportServerES: dbo.AddHistoryRecord](../../StoredProcedures/ReportServerES/dbo.AddHistoryRecord.md)
- [ReportServerES: dbo.AddReportToCache](../../StoredProcedures/ReportServerES/dbo.AddReportToCache.md)
- [ReportServerES: dbo.CleanBrokenSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanBrokenSnapshots.md)
- [ReportServerES: dbo.CleanExpiredCache](../../StoredProcedures/ReportServerES/dbo.CleanExpiredCache.md)
- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredSessions.md)
- [ReportServerES: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanOrphanedSnapshots.md)
- [ReportServerES: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerES/dbo.CopyChunksOfType.md)
- [ReportServerES: dbo.CreateEditSession](../../StoredProcedures/ReportServerES/dbo.CreateEditSession.md)
- [ReportServerES: dbo.CreateNewSnapshotVersion](../../StoredProcedures/ReportServerES/dbo.CreateNewSnapshotVersion.md)
- [ReportServerES: dbo.CreateObject](../../StoredProcedures/ReportServerES/dbo.CreateObject.md)
- [ReportServerES: dbo.CreateSession](../../StoredProcedures/ReportServerES/dbo.CreateSession.md)
- [ReportServerES: dbo.DecreaseTransientSnapshotRefcount](../../StoredProcedures/ReportServerES/dbo.DecreaseTransientSnapshotRefcount.md)
- [ReportServerES: dbo.DeleteObject](../../StoredProcedures/ReportServerES/dbo.DeleteObject.md)
- [ReportServerES: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerES/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerES: dbo.DereferenceSessionSnapshot](../../StoredProcedures/ReportServerES/dbo.DereferenceSessionSnapshot.md)
- [ReportServerES: dbo.EnforceCacheLimits](../../StoredProcedures/ReportServerES/dbo.EnforceCacheLimits.md)
- [ReportServerES: dbo.FlushCacheByID](../../StoredProcedures/ReportServerES/dbo.FlushCacheByID.md)
- [ReportServerES: dbo.FlushReportFromCache](../../StoredProcedures/ReportServerES/dbo.FlushReportFromCache.md)
- [ReportServerES: dbo.GetDataSetForExecution](../../StoredProcedures/ReportServerES/dbo.GetDataSetForExecution.md)
- [ReportServerES: dbo.GetReportForExecution](../../StoredProcedures/ReportServerES/dbo.GetReportForExecution.md)
- [ReportServerES: dbo.GetSessionData](../../StoredProcedures/ReportServerES/dbo.GetSessionData.md)
- [ReportServerES: dbo.GetSnapshotFromHistory](../../StoredProcedures/ReportServerES/dbo.GetSnapshotFromHistory.md)
- [ReportServerES: dbo.GetSnapshotPromotedInfo](../../StoredProcedures/ReportServerES/dbo.GetSnapshotPromotedInfo.md)
- [ReportServerES: dbo.IncreaseTransientSnapshotRefcount](../../StoredProcedures/ReportServerES/dbo.IncreaseTransientSnapshotRefcount.md)
- [ReportServerES: dbo.InsertUnreferencedSnapshot](../../StoredProcedures/ReportServerES/dbo.InsertUnreferencedSnapshot.md)
- [ReportServerES: dbo.LoadForDefinitionCheck](../../StoredProcedures/ReportServerES/dbo.LoadForDefinitionCheck.md)
- [ReportServerES: dbo.LoadForRepublishing](../../StoredProcedures/ReportServerES/dbo.LoadForRepublishing.md)
- [ReportServerES: dbo.MarkSnapshotAsDependentOnUser](../../StoredProcedures/ReportServerES/dbo.MarkSnapshotAsDependentOnUser.md)
- [ReportServerES: dbo.PromoteSnapshotInfo](../../StoredProcedures/ReportServerES/dbo.PromoteSnapshotInfo.md)
- [ReportServerES: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerES/dbo.RemoveSegmentedMapping.md)
- [ReportServerES: dbo.SetExecutionOptions](../../StoredProcedures/ReportServerES/dbo.SetExecutionOptions.md)
- [ReportServerES: dbo.SetObjectContent](../../StoredProcedures/ReportServerES/dbo.SetObjectContent.md)
- [ReportServerES: dbo.SetSessionData](../../StoredProcedures/ReportServerES/dbo.SetSessionData.md)
- [ReportServerES: dbo.SetSnapshotProcessingFlags](../../StoredProcedures/ReportServerES/dbo.SetSnapshotProcessingFlags.md)
- [ReportServerES: dbo.UpdateCompiledDefinition](../../StoredProcedures/ReportServerES/dbo.UpdateCompiledDefinition.md)
- [ReportServerES: dbo.UpdateSnapshot](../../StoredProcedures/ReportServerES/dbo.UpdateSnapshot.md)
- [ReportServerES: dbo.UpdateSnapshotPaginationInfo](../../StoredProcedures/ReportServerES/dbo.UpdateSnapshotPaginationInfo.md)
- [ReportServerES: dbo.UpdateSnapshotReferences](../../StoredProcedures/ReportServerES/dbo.UpdateSnapshotReferences.md)

