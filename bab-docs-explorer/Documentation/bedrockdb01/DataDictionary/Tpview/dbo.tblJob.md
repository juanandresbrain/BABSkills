# dbo.tblJob

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobID | int | 4 | 0 | YES |  |  |
| Name | varchar | 50 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| UnixID | int | 4 | 0 |  |  |  |
| CompanyNumber | int | 4 | 0 |  |  |  |
| TriggerPrefix | varchar | 2 | 0 |  |  |  |
| TriggerType | int | 4 | 0 |  |  |  |
| TriggerMachineID | int | 4 | 0 |  |  |  |
| TriggerDir | varchar | 255 | 0 |  |  |  |
| TriggerFile | varchar | 50 | 0 |  |  |  |
| JobConnectionID | int | 4 | 0 |  |  |  |
| TransferAppType | int | 4 | 0 |  |  |  |
