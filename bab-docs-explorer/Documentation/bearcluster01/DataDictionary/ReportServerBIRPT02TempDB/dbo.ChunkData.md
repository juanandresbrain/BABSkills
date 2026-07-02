# dbo.ChunkData

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkID | uniqueidentifier | 16 | 0 | YES |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| ChunkFlags | tinyint | 1 | 1 |  |  |  |
| ChunkName | nvarchar | 520 | 1 |  |  |  |
| ChunkType | int | 4 | 1 |  |  |  |
| Version | smallint | 2 | 1 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| Content | image | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CleanBrokenSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanBrokenSnapshots.md)
- [ReportServerBIRPT02: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanOrphanedSnapshots.md)
- [ReportServerBIRPT02: dbo.CopyChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunks.md)
- [ReportServerBIRPT02: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunksOfType.md)
- [ReportServerBIRPT02: dbo.CreateChunkAndGetPointer](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateChunkAndGetPointer.md)
- [ReportServerBIRPT02: dbo.CreateSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.DeleteOneChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteOneChunk.md)
- [ReportServerBIRPT02: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerBIRPT02: dbo.GetChunkInformation](../../StoredProcedures/ReportServerBIRPT02/dbo.GetChunkInformation.md)
- [ReportServerBIRPT02: dbo.GetChunkPointerAndLength](../../StoredProcedures/ReportServerBIRPT02/dbo.GetChunkPointerAndLength.md)
- [ReportServerBIRPT02: dbo.GetSnapshotChunks](../../StoredProcedures/ReportServerBIRPT02/dbo.GetSnapshotChunks.md)
- [ReportServerBIRPT02: dbo.IsSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.IsSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.ListHistory](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistory.md)
- [ReportServerBIRPT02: dbo.ListHistorySnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistorySnapshots.md)
- [ReportServerBIRPT02: dbo.LockSnapshotForUpgrade](../../StoredProcedures/ReportServerBIRPT02/dbo.LockSnapshotForUpgrade.md)
- [ReportServerBIRPT02: dbo.ReadChunkPortion](../../StoredProcedures/ReportServerBIRPT02/dbo.ReadChunkPortion.md)
- [ReportServerBIRPT02: dbo.SetSnapshotChunksVersion](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSnapshotChunksVersion.md)
- [ReportServerBIRPT02: dbo.WriteChunkPortion](../../StoredProcedures/ReportServerBIRPT02/dbo.WriteChunkPortion.md)

