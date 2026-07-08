# dbo.MSpeer_conflictdetectionconfigrequest

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| sent_date | datetime | 8 | 0 |  |  |  |
| timeout | int | 4 | 0 |  |  |  |
| modified_date | datetime | 8 | 0 |  |  |  |
| progress_phase | nvarchar | 64 | 0 |  |  |  |
| phase_timed_out | bit | 1 | 0 |  |  |  |
