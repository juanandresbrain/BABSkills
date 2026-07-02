# dbo.SegmentedChunk

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkId | uniqueidentifier | 16 | 0 |  |  |  |
| SnapshotDataId | uniqueidentifier | 16 | 0 |  |  |  |
| ChunkFlags | tinyint | 1 | 0 |  |  |  |
| ChunkName | nvarchar | 520 | 0 |  |  |  |
| ChunkType | int | 4 | 0 |  |  |  |
| Version | smallint | 2 | 0 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| Machine | nvarchar | 1024 | 0 |  |  |  |
| SegmentedChunkId | bigint | 8 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanOrphanedSnapshots.md)
- [ReportServerBIRPT02: dbo.CopyChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunks.md)
- [ReportServerBIRPT02: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunksOfType.md)
- [ReportServerBIRPT02: dbo.CreateRdlChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateRdlChunk.md)
- [ReportServerBIRPT02: dbo.CreateSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.DeleteOneChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteOneChunk.md)
- [ReportServerBIRPT02: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerBIRPT02: dbo.IsSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.IsSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.ListHistory](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistory.md)
- [ReportServerBIRPT02: dbo.ListHistorySnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistorySnapshots.md)
- [ReportServerBIRPT02: dbo.OpenSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.OpenSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveSegmentedMapping.md)
- [ReportServerBIRPT02: dbo.SetSnapshotChunksVersion](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSnapshotChunksVersion.md)
- [ReportServerBIRPT02: dbo.ShallowCopyChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.ShallowCopyChunk.md)
- [ReportServerBIRPT02: dbo.TempChunkExists](../../StoredProcedures/ReportServerBIRPT02/dbo.TempChunkExists.md)

