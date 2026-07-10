# dbo.ASMeasureGroup

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mgID | int | 4 | 0 | YES |  |  |
| cubeID | int | 4 | 1 |  |  |  |
| Descr | varchar | 50 | 0 |  |  |  |
| normalPartitionFrequency | varchar | 2 | 0 |  |  | Frequency of the partitions 1-Single Partition, M = Fiscal Month, Q = Fiscal Quarter, MW = Fiscal Month using Weeks |
| numRefreshDays | int | 4 | 0 |  |  |  |
| aggregationID | varchar | 255 | 0 |  |  |  |
| SQLText | varchar | -1 | 0 |  |  |  |
| estimatedRows | int | 4 | 1 |  |  |  |
| ASMeasureGroup | varchar | 255 | 1 |  |  |  |
| ASMeasureGroupID | varchar | 255 | 1 |  |  |  |
| ASDataSourceID | varchar | 255 | 1 |  |  |  |
| PartitionPrefix | varchar | 255 | 1 |  |  | This is the prefix in formulating the Partiion Name |
