# dbo.ChunkSegmentMapping

**Database:** ReportServerSATempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkId | uniqueidentifier | 16 | 0 |  |  |  |
| SegmentId | uniqueidentifier | 16 | 0 |  |  |  |
| StartByte | bigint | 8 | 0 |  |  |  |
| LogicalByteCount | int | 4 | 0 |  |  |  |
| ActualByteCount | int | 4 | 0 |  |  |  |
