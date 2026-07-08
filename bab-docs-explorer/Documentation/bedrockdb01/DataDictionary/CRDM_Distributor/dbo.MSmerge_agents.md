# dbo.MSmerge_agents

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
| subscriber_id | smallint | 2 | 1 |  |  |  |
| subscriber_db | sysname | 256 | 1 |  |  |  |
| local_job | bit | 1 | 1 |  |  |  |
| job_id | binary | 16 | 1 |  |  |  |
| profile_id | int | 4 | 1 |  |  |  |
| anonymous_subid | uniqueidentifier | 16 | 1 |  |  |  |
| subscriber_name | sysname | 256 | 1 |  |  |  |
| creation_date | datetime | 8 | 0 |  |  |  |
| offload_enabled | bit | 1 | 0 |  |  |  |
| offload_server | sysname | 256 | 1 |  |  |  |
| sid | varbinary | 85 | 0 |  |  |  |
| subscriber_security_mode | smallint | 2 | 1 |  |  |  |
| subscriber_login | sysname | 256 | 1 |  |  |  |
| subscriber_password | nvarchar | 1048 | 1 |  |  |  |
| publisher_security_mode | smallint | 2 | 1 |  |  |  |
| publisher_login | sysname | 256 | 1 |  |  |  |
| publisher_password | nvarchar | 1048 | 1 |  |  |  |
| job_step_uid | uniqueidentifier | 16 | 1 |  |  |  |
