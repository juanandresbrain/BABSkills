# dbo.SegmentedChunk

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

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
| SegmentedChunkId | bigint | 8 | 0 | YES |  |  |
