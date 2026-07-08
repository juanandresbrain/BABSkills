# dbo.ChunkData

**Database:** ReportServerWebIMTempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ChunkID | uniqueidentifier | 16 | 0 |  |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| ChunkFlags | tinyint | 1 | 1 |  |  |  |
| ChunkName | nvarchar | 520 | 1 |  |  |  |
| ChunkType | int | 4 | 1 |  |  |  |
| Version | smallint | 2 | 1 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| Content | image | 16 | 1 |  |  |  |
