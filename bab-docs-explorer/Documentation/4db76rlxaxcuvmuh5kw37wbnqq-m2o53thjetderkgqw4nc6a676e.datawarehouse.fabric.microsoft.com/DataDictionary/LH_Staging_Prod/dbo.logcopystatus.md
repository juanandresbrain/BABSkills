# dbo.logcopystatus

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BatchID | int | 4 | 1 |  |  |  |
| ControlID | int | 4 | 1 |  |  |  |
| BusinessArea | varchar | 8000 | 1 |  |  |  |
| SrcTableSchema | varchar | 8000 | 1 |  |  |  |
| SrcTableName | varchar | 8000 | 1 |  |  |  |
| LatestFilePath | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| LogDate | datetime2 | 8 | 1 |  |  |  |
