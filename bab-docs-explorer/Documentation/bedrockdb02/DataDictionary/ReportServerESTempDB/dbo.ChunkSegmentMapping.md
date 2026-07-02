# dbo.ChunkSegmentMapping

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkId | uniqueidentifier | 16 | 0 | YES |  |  |
| SegmentId | uniqueidentifier | 16 | 0 | YES |  |  |
| StartByte | bigint | 8 | 0 |  |  |  |
| LogicalByteCount | int | 4 | 0 |  |  |  |
| ActualByteCount | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanOrphanedSnapshots.md)
- [ReportServerES: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerES/dbo.CopyChunksOfType.md)
- [ReportServerES: dbo.CreateChunkSegment](../../StoredProcedures/ReportServerES/dbo.CreateChunkSegment.md)
- [ReportServerES: dbo.DeepCopySegment](../../StoredProcedures/ReportServerES/dbo.DeepCopySegment.md)
- [ReportServerES: dbo.ListHistory](../../StoredProcedures/ReportServerES/dbo.ListHistory.md)
- [ReportServerES: dbo.OpenSegmentedChunk](../../StoredProcedures/ReportServerES/dbo.OpenSegmentedChunk.md)
- [ReportServerES: dbo.ReadChunkSegment](../../StoredProcedures/ReportServerES/dbo.ReadChunkSegment.md)
- [ReportServerES: dbo.RemoveSegment](../../StoredProcedures/ReportServerES/dbo.RemoveSegment.md)
- [ReportServerES: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerES/dbo.RemoveSegmentedMapping.md)
- [ReportServerES: dbo.ShallowCopyChunk](../../StoredProcedures/ReportServerES/dbo.ShallowCopyChunk.md)
- [ReportServerES: dbo.WriteChunkSegment](../../StoredProcedures/ReportServerES/dbo.WriteChunkSegment.md)

