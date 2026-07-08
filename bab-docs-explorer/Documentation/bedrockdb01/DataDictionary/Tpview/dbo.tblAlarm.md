# dbo.tblAlarm

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AlarmID | int | 4 | 0 | YES |  |  |
| AlarmTime | datetime | 8 | 0 |  |  |  |
| Summary | varchar | 150 | 0 |  |  |  |
| Description | varchar | 400 | 0 |  |  |  |
| Severity | int | 4 | 0 |  |  |  |
| AckStatus | int | 4 | 0 |  |  |  |
| AckTime | datetime | 8 | 0 |  |  |  |
| AckPersonnelID | int | 4 | 0 |  |  |  |
| EMailStatus | int | 4 | 0 |  |  |  |
| EMailAttempts | int | 4 | 0 |  |  |  |
| EMailAddress | varchar | 75 | 0 |  |  |  |
| EMailTime | datetime | 8 | 0 |  |  |  |
| DirtyFlag | int | 4 | 0 |  |  |  |
| AlarmRuleNo | int | 4 | 0 |  |  |  |
