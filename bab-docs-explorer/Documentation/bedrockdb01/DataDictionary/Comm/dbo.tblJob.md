# dbo.tblJob

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobID | int | 4 | 0 | YES |  |  |
| Name | varchar | 50 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| UnixID | int | 4 | 0 |  |  |  |
| CompanyNumber | int | 4 | 0 |  |  |  |
| TriggerPrefix | nvarchar | 4 | 0 |  |  |  |
| TriggerType | int | 4 | 0 |  |  |  |
| TriggerMachineID | int | 4 | 0 |  |  |  |
| TriggerDir | nvarchar | 510 | 0 |  |  |  |
| TriggerFile | nvarchar | 100 | 0 |  |  |  |
| JobConnectionID | int | 4 | 0 |  |  |  |
| TransferAppType | int | 4 | 0 |  |  |  |
| DUE_DAY | smallint | 2 | 0 |  |  |  |
| DUE_TIME | datetime | 8 | 0 |  |  |  |
| DUE_DAY_CUT_OFF | smallint | 2 | 0 |  |  |  |
| DUE_TIME_CUT_OFF | datetime | 8 | 0 |  |  |  |
