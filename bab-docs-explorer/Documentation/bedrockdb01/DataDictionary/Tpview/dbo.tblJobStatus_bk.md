# dbo.tblJobStatus_bk

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobStatusID | int | 4 | 0 | YES |  |  |
| JobID | int | 4 | 0 |  |  |  |
| DTSMSessionNo | int | 4 | 0 |  |  |  |
| TriggerName | varchar | 255 | 0 |  |  |  |
| OverallStartTime | datetime | 8 | 0 |  |  |  |
| OverallEndTime | datetime | 8 | 0 |  |  |  |
| FinalStatus | int | 4 | 0 |  |  |  |
