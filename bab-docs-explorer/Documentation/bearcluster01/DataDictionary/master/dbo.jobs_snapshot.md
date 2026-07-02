# dbo.jobs_snapshot

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 1 |  |  |  |
| date_created | datetime | 8 | 1 |  |  |  |
| date_modified | datetime | 8 | 1 |  |  |  |
| schedule_date_created | datetime | 8 | 1 |  |  |  |
| schedule_date_modified | datetime | 8 | 1 |  |  |  |
| schedule_uid | uniqueidentifier | 16 | 1 |  |  |  |

