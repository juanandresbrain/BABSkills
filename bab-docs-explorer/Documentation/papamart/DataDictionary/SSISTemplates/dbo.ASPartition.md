# dbo.ASPartition

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| partID | int | 4 | 0 | YES |  |  |
| mgID | int | 4 | 1 |  |  |  |
| SSASPartitionName | varchar | 255 | 1 |  |  |  |
| fromDate_Key | int | 4 | 0 |  |  |  |
| thruDate_Key | int | 4 | 0 |  |  |  |
| aggregationID | varchar | 255 | 1 |  |  |  |
| SQLText | varchar | -1 | 1 |  |  |  |
| estimatedRows | int | 4 | 1 |  |  |  |
| PartitionSlice | varchar | -1 | 1 |  |  |  |
| createdDt | datetime | 8 | 1 |  |  |  |
