# dbo.tblCommand

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CommandID | int | 4 | 0 | YES |  |  |
| CommandType | int | 4 | 0 |  |  |  |
| RestoreDay | datetime | 8 | 0 |  |  |  |
| RestoreFile | int | 4 | 0 |  |  |  |
| Attempt | int | 4 | 0 |  |  |  |
| Duration | int | 4 | 0 |  |  |  |
| HostFilePath | nvarchar | 510 | 0 |  |  |  |
| LocationFilePath | nvarchar | 510 | 0 |  |  |  |
| Direction | int | 4 | 0 |  |  |  |
| TimeSent | datetime | 8 | 0 |  |  |  |
| ManualPoll | int | 4 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| ScheduleType | int | 4 | 0 |  |  |  |
| TimeIntervalFrom | datetime | 8 | 0 |  |  |  |
| TimeIntervalTo | datetime | 8 | 0 |  |  |  |
