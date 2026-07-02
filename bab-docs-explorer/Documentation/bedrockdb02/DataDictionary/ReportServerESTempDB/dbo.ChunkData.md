# dbo.ChunkData

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

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

- [ReportServerES: dbo.CleanBrokenSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanBrokenSnapshots.md)
- [ReportServerES: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanOrphanedSnapshots.md)
- [ReportServerES: dbo.CopyChunks](../../StoredProcedures/ReportServerES/dbo.CopyChunks.md)
- [ReportServerES: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerES/dbo.CopyChunksOfType.md)
- [ReportServerES: dbo.CreateChunkAndGetPointer](../../StoredProcedures/ReportServerES/dbo.CreateChunkAndGetPointer.md)
- [ReportServerES: dbo.CreateSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.CreateSegmentedChunk.md)
- [ReportServerES: dbo.DeleteOneChunk](../../StoredProcedures/ReportServerES/dbo.DeleteOneChunk.md)
- [ReportServerES: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerES/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerES: dbo.GetChunkInformation](../../StoredProcedures/ReportServerES/dbo.GetChunkInformation.md)
- [ReportServerES: dbo.GetChunkPointerAndLength](../../StoredProcedures/ReportServerES/dbo.GetChunkPointerAndLength.md)
- [ReportServerES: dbo.GetSnapshotChunks](../../StoredProcedures/ReportServerES/dbo.GetSnapshotChunks.md)
- [ReportServerES: dbo.IsSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.IsSegmentedChunk.md)
- [ReportServerES: dbo.ListHistory](../../StoredProcedures/ReportServerES/dbo.ListHistory.md)
- [ReportServerES: dbo.LockSnapshotForUpgrade](../../StoredProcedures/ReportServerES/dbo.LockSnapshotForUpgrade.md)
- [ReportServerES: dbo.ReadChunkPortion](../../StoredProcedures/ReportServerES/dbo.ReadChunkPortion.md)
- [ReportServerES: dbo.SetSnapshotChunksVersion](../../StoredProcedures/ReportServerES/dbo.SetSnapshotChunksVersion.md)
- [ReportServerES: dbo.WriteChunkPortion](../../StoredProcedures/ReportServerES/dbo.WriteChunkPortion.md)

