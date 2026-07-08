# dbo.ExecutionCache

**Database:** ReportServerWebIMTempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExecutionCacheID | uniqueidentifier | 16 | 0 |  |  |  |
| ReportID | uniqueidentifier | 16 | 0 |  |  |  |
| ExpirationFlags | int | 4 | 0 |  |  |  |
| AbsoluteExpiration | datetime | 8 | 1 |  |  |  |
| RelativeExpiration | int | 4 | 1 |  |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| LastUsedTime | datetime | 8 | 0 |  |  |  |
| ParamsHash | int | 4 | 0 |  |  |  |
