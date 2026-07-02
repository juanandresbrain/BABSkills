# dbo.ChunkSegmentMapping

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkId | uniqueidentifier | 16 | 0 | YES |  |  |
| SegmentId | uniqueidentifier | 16 | 0 | YES |  |  |
| StartByte | bigint | 8 | 0 |  |  |  |
| LogicalByteCount | int | 4 | 0 |  |  |  |
| ActualByteCount | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanOrphanedSnapshots.md)
- [ReportServerBIRPT02: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerBIRPT02/dbo.CopyChunksOfType.md)
- [ReportServerBIRPT02: dbo.CreateChunkSegment](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateChunkSegment.md)
- [ReportServerBIRPT02: dbo.DeepCopySegment](../../StoredProcedures/ReportServerBIRPT02/dbo.DeepCopySegment.md)
- [ReportServerBIRPT02: dbo.ListHistory](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistory.md)
- [ReportServerBIRPT02: dbo.ListHistorySnapshots](../../StoredProcedures/ReportServerBIRPT02/dbo.ListHistorySnapshots.md)
- [ReportServerBIRPT02: dbo.OpenSegmentedChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.OpenSegmentedChunk.md)
- [ReportServerBIRPT02: dbo.ReadChunkSegment](../../StoredProcedures/ReportServerBIRPT02/dbo.ReadChunkSegment.md)
- [ReportServerBIRPT02: dbo.RemoveSegment](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveSegment.md)
- [ReportServerBIRPT02: dbo.RemoveSegmentedMapping](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveSegmentedMapping.md)
- [ReportServerBIRPT02: dbo.ShallowCopyChunk](../../StoredProcedures/ReportServerBIRPT02/dbo.ShallowCopyChunk.md)
- [ReportServerBIRPT02: dbo.WriteChunkSegment](../../StoredProcedures/ReportServerBIRPT02/dbo.WriteChunkSegment.md)

