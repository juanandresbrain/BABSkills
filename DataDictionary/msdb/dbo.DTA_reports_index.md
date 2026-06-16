# dbo.DTA_reports_index

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IndexID | int | 4 | 0 | YES |  |  |
| TableID | int | 4 | 0 |  | YES |  |
| IndexName | sysname | 256 | 0 |  |  |  |
| IsClustered | bit | 1 | 0 |  |  |  |
| IsUnique | bit | 1 | 0 |  |  |  |
| IsHeap | bit | 1 | 0 |  |  |  |
| IsExisting | bit | 1 | 0 |  |  |  |
| IsFiltered | bit | 1 | 0 |  |  |  |
| Storage | float | 8 | 0 |  |  |  |
| NumRows | bigint | 8 | 0 |  |  |  |
| IsRecommended | bit | 1 | 0 |  |  |  |
| RecommendedStorage | float | 8 | 0 |  |  |  |
| PartitionSchemeID | int | 4 | 1 |  |  |  |
| SessionUniquefier | int | 4 | 1 |  |  |  |
| FilterDefinition | nvarchar | 2048 | 0 |  |  |  |

