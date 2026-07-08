# dbo.tblVersionStatus

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VersionStatusID | int | 4 | 0 | YES |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| DBName | varchar | 20 | 0 |  |  |  |
| DBHost | varchar | 20 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| HostName | varchar | 20 | 0 |  |  |  |
| AppName | varchar | 20 | 0 |  |  |  |
| RemoteNumber | numeric | 9 | 0 |  |  |  |
| InstanceID | int | 4 | 0 |  |  |  |
| Action | varchar | 15 | 0 |  |  |  |
