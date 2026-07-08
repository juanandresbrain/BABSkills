# dbo.RunningJobs

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobID | nvarchar | 64 | 0 |  |  |  |
| StartDate | datetime | 8 | 0 |  |  |  |
| ComputerName | nvarchar | 64 | 0 |  |  |  |
| RequestName | nvarchar | 850 | 0 |  |  |  |
| RequestPath | nvarchar | 850 | 0 |  |  |  |
| UserId | uniqueidentifier | 16 | 0 |  |  |  |
| Description | ntext | 16 | 1 |  |  |  |
| Timeout | int | 4 | 0 |  |  |  |
| JobAction | smallint | 2 | 0 |  |  |  |
| JobType | smallint | 2 | 0 |  |  |  |
| JobStatus | smallint | 2 | 0 |  |  |  |
