# dbo.Config_LogPipelineStatus_1022

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ControlID | int | 4 | 1 |  |  |  |
| PipelineRunID | varchar | 8000 | 1 |  |  |  |
| PipelineStatus | varchar | 8000 | 1 |  |  |  |
| IsMergeStarted | int | 4 | 1 |  |  |  |
| Merge_Status | varchar | 8000 | 1 |  |  |  |
| BatchID | int | 4 | 1 |  |  |  |
| Comments | varchar | 8000 | 1 |  |  |  |
