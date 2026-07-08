# dbo.MSsnapshot_agents

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 200 | 0 |  |  |  |
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| publication_type | int | 4 | 0 |  |  |  |
| local_job | bit | 1 | 0 |  |  |  |
| job_id | binary | 16 | 1 |  |  |  |
| profile_id | int | 4 | 0 |  |  |  |
| dynamic_filter_login | sysname | 256 | 1 |  |  |  |
| dynamic_filter_hostname | sysname | 256 | 1 |  |  |  |
| publisher_security_mode | int | 4 | 1 |  |  |  |
| publisher_login | sysname | 256 | 1 |  |  |  |
| publisher_password | nvarchar | 1048 | 1 |  |  |  |
| job_step_uid | uniqueidentifier | 16 | 1 |  |  |  |
