# dbo.tblPollingPeriod

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PollingPeriodID | int | 4 | 0 | YES |  |  |
| MaxConcurrentSession | int | 4 | 0 |  |  |  |
| FTPAccount | varchar | 30 | 0 |  |  |  |
| FTPPassword | varchar | 241 | 0 |  |  |  |
| CallFrequency | int | 4 | 0 |  |  |  |
| CallDuration | int | 4 | 0 |  |  |  |
| StartDay | int | 4 | 0 |  |  |  |
| StartTime | datetime | 8 | 0 |  |  |  |
| EndDay | int | 4 | 0 |  |  |  |
| EndTime | datetime | 8 | 0 |  |  |  |
| PeriodName | varchar | 30 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| SFTP_ACNT | nvarchar | 100 | 1 |  |  |  |
| SFTP_PSWRD_SDM | nvarchar | 482 | 1 |  |  |  |
| SFTP_PSWRD_POS | nvarchar | 482 | 0 |  |  |  |
