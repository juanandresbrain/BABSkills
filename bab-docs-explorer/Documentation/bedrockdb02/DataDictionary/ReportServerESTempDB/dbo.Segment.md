# dbo.Segment

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SegmentId | uniqueidentifier | 16 | 0 | YES |  |  |
| Content | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.CleanOrphanedSnapshots](../../StoredProcedures/ReportServerES/dbo.CleanOrphanedSnapshots.md)
- [ReportServerES: dbo.CopyChunksOfType](../../StoredProcedures/ReportServerES/dbo.CopyChunksOfType.md)
- [ReportServerES: dbo.CreateChunkSegment](../../StoredProcedures/ReportServerES/dbo.CreateChunkSegment.md)
- [ReportServerES: dbo.DeepCopySegment](../../StoredProcedures/ReportServerES/dbo.DeepCopySegment.md)
- [ReportServerES: dbo.ListHistory](../../StoredProcedures/ReportServerES/dbo.ListHistory.md)
- [ReportServerES: dbo.ReadChunkSegment](../../StoredProcedures/ReportServerES/dbo.ReadChunkSegment.md)
- [ReportServerES: dbo.RemoveSegment](../../StoredProcedures/ReportServerES/dbo.RemoveSegment.md)
- [ReportServerES: dbo.WriteChunkSegment](../../StoredProcedures/ReportServerES/dbo.WriteChunkSegment.md)

