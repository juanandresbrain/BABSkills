# dbo.smart_backup_files

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| backup_path | nvarchar | 520 | 0 | YES |  |  |
| last_modified_utc | datetime | 8 | 1 |  |  |  |
| backup_type | smallint | 2 | 1 |  |  |  |
| expiration_date | datetime | 8 | 1 |  |  |  |
| user_name | nvarchar | 256 | 1 |  |  |  |
| server_name | nvarchar | 256 | 1 |  |  |  |
| database_name | nvarchar | 256 | 1 |  |  |  |
| backup_size | numeric | 13 | 1 |  |  |  |
| first_lsn | numeric | 13 | 1 |  |  |  |
| last_lsn | numeric | 13 | 1 |  |  |  |
| database_backup_lsn | numeric | 13 | 1 |  |  |  |
| backup_start_date | datetime | 8 | 1 |  |  |  |
| backup_finish_date | datetime | 8 | 1 |  |  |  |
| machine_name | nvarchar | 256 | 1 |  |  |  |
| last_recovery_fork_id | uniqueidentifier | 16 | 1 |  |  |  |
| first_recovery_fork_id | uniqueidentifier | 16 | 1 |  |  |  |
| fork_point_lsn | numeric | 13 | 1 |  |  |  |
| availability_group_guid | uniqueidentifier | 16 | 1 |  |  |  |
| database_guid | uniqueidentifier | 16 | 1 |  |  |  |
| status | char | 1 | 1 |  |  |  |

