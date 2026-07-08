# dbo.MSdistribution_agents

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 200 | 0 |  |  |  |
| publisher_database_id | int | 4 | 0 |  |  |  |
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| subscriber_id | smallint | 2 | 1 |  |  |  |
| subscriber_db | sysname | 256 | 1 |  |  |  |
| subscription_type | int | 4 | 0 |  |  |  |
| local_job | bit | 1 | 1 |  |  |  |
| job_id | binary | 16 | 1 |  |  |  |
| subscription_guid | binary | 16 | 0 |  |  |  |
| profile_id | int | 4 | 0 |  |  |  |
| anonymous_subid | uniqueidentifier | 16 | 1 |  |  |  |
| subscriber_name | sysname | 256 | 1 |  |  |  |
| virtual_agent_id | int | 4 | 1 |  |  |  |
| anonymous_agent_id | int | 4 | 1 |  |  |  |
| creation_date | datetime | 8 | 0 |  |  |  |
| queue_id | sysname | 256 | 1 |  |  |  |
| queue_status | int | 4 | 0 |  |  |  |
| offload_enabled | bit | 1 | 0 |  |  |  |
| offload_server | sysname | 256 | 1 |  |  |  |
| dts_package_name | sysname | 256 | 1 |  |  |  |
| dts_package_password | nvarchar | 1048 | 1 |  |  |  |
| dts_package_location | int | 4 | 0 |  |  |  |
| sid | varbinary | 85 | 0 |  |  |  |
| queue_server | sysname | 256 | 1 |  |  |  |
| subscriber_security_mode | smallint | 2 | 1 |  |  |  |
| subscriber_login | sysname | 256 | 1 |  |  |  |
| subscriber_password | nvarchar | 1048 | 1 |  |  |  |
| reset_partial_snapshot_progress | bit | 1 | 0 |  |  |  |
| job_step_uid | uniqueidentifier | 16 | 1 |  |  |  |
| subscriptionstreams | tinyint | 1 | 1 |  |  |  |
| subscriber_type | tinyint | 1 | 1 |  |  |  |
| subscriber_provider | sysname | 256 | 1 |  |  |  |
| subscriber_datasrc | nvarchar | 8000 | 1 |  |  |  |
| subscriber_location | nvarchar | 8000 | 1 |  |  |  |
| subscriber_provider_string | nvarchar | 8000 | 1 |  |  |  |
| subscriber_catalog | sysname | 256 | 1 |  |  |  |
