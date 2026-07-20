# dbo.Config_LogPipelineStatus_508

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
