# dbo.tblJobStatusRequest

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobStatusRequestID | int | 4 | 0 | YES |  |  |
| JobStatusID | int | 4 | 0 |  |  |  |
| CallNumber | int | 4 | 0 |  |  |  |
| RetryNumber | int | 4 | 0 |  |  |  |
| StartTime | datetime | 8 | 0 |  |  |  |
| EndTime | datetime | 8 | 0 |  |  |  |
| UnixQueueFile | varchar | 50 | 0 |  |  |  |
| DTSMStatus | int | 4 | 0 |  |  |  |
| DTSMSubCode1 | int | 4 | 0 |  |  |  |
| DTSMSubCode2 | int | 4 | 0 |  |  |  |
| DTSMSubCode3 | int | 4 | 0 |  |  |  |
| DTSMSubCode4 | int | 4 | 0 |  |  |  |
| DTSMSubCode5 | int | 4 | 0 |  |  |  |
| DTSMBSCLineID | int | 4 | 0 |  |  |  |
| StatusFile | varchar | 255 | 0 |  |  |  |
| ErrorNumber | int | 4 | 0 |  |  |  |
| ErrorDesc | varchar | 255 | 0 |  |  |  |
| StatusTime | datetime | 8 | 0 |  |  |  |
| BytesInLastFile | int | 4 | 0 |  |  |  |
