# dbo.SnapshotData

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SnapshotDataID | uniqueidentifier | 16 | 0 |  |  |  |
| CreatedDate | datetime | 8 | 0 |  |  |  |
| ParamsHash | int | 4 | 1 |  |  |  |
| QueryParams | ntext | 256 | 1 |  |  |  |
| EffectiveParams | ntext | 256 | 1 |  |  |  |
| Description | nvarchar | 1024 | 1 |  |  |  |
| DependsOnUser | bit | 1 | 1 |  |  |  |
| PermanentRefcount | int | 4 | 0 |  |  |  |
| TransientRefcount | int | 4 | 0 |  |  |  |
| ExpirationDate | datetime | 8 | 0 |  |  |  |
| PageCount | int | 4 | 1 |  |  |  |
| HasDocMap | bit | 1 | 1 |  |  |  |
| PaginationMode | smallint | 2 | 1 |  |  |  |
| ProcessingFlags | int | 4 | 1 |  |  |  |
