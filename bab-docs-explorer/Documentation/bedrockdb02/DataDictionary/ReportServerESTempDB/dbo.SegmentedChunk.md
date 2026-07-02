# dbo.SegmentedChunk

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

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

- [ReportServerES: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanOrphanedSnapshots.md)
- [ReportServerES: dbo.CopyChunks](../../StoredProcedures/ReportServerES/dbo.CopyChunks.md)
- [ReportServerES: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerES/dbo.CopyChunksOfType.md)
- [ReportServerES: dbo.CreateRdlChunk](../../StoredProcedures/ReportServerES/dbo.CreateRdlChunk.md)
- [ReportServerES: dbo.CreateSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.CreateSegmentedChunk.md)
- [ReportServerES: dbo.DeleteOneChunk](../../StoredProcedures/ReportServerES/dbo.DeleteOneChunk.md)
- [ReportServerES: dbo.DeleteSnapshotAndChunks](../../StoredProcedures/ReportServerES/dbo.DeleteSnapshotAndChunks.md)
- [ReportServerES: dbo.IsSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.IsSegmentedChunk.md)
- [ReportServerES: dbo.ListHistory](../../StoredProcedures/ReportServerES/dbo.ListHistory.md)
- [ReportServerES: dbo.OpenSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.OpenSegmentedChunk.md)
- [ReportServerES: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerES/dbo.RemoveSegmentedMapping.md)
- [ReportServerES: dbo.SetSnapshotChunksVersion](../../StoredProcedures/ReportServerES/dbo.SetSnapshotChunksVersion.md)
- [ReportServerES: dbo.ShallowCopyChunk](../../StoredProcedures/ReportServerES/dbo.ShallowCopyChunk.md)
- [ReportServerES: dbo.TempChunkExists](../../StoredProcedures/ReportServerES/dbo.TempChunkExists.md)

