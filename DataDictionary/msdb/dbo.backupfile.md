# dbo.backupfile

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| backup_set_id | int | 4 | 0 | YES | YES |  |
| first_family_number | tinyint | 1 | 1 |  |  |  |
| first_media_number | smallint | 2 | 1 |  |  |  |
| filegroup_name | nvarchar | 256 | 1 |  |  |  |
| page_size | int | 4 | 1 |  |  |  |
| file_number | numeric | 9 | 0 | YES |  |  |
| backed_up_page_count | numeric | 9 | 1 |  |  |  |
| file_type | char | 1 | 1 |  |  |  |
| source_file_block_size | numeric | 9 | 1 |  |  |  |
| file_size | numeric | 13 | 1 |  |  |  |
| logical_name | nvarchar | 256 | 1 |  |  |  |
| physical_drive | nvarchar | 520 | 1 |  |  |  |
| physical_name | nvarchar | 520 | 1 |  |  |  |
| state | tinyint | 1 | 1 |  |  |  |
| state_desc | nvarchar | 128 | 1 |  |  |  |
| create_lsn | numeric | 13 | 1 |  |  |  |
| drop_lsn | numeric | 13 | 1 |  |  |  |
| file_guid | uniqueidentifier | 16 | 1 |  |  |  |
| read_only_lsn | numeric | 13 | 1 |  |  |  |
| read_write_lsn | numeric | 13 | 1 |  |  |  |
| differential_base_lsn | numeric | 13 | 1 |  |  |  |
| differential_base_guid | uniqueidentifier | 16 | 1 |  |  |  |
| backup_size | numeric | 13 | 1 |  |  |  |
| filegroup_guid | uniqueidentifier | 16 | 1 |  |  |  |
| is_readonly | bit | 1 | 1 |  |  |  |
| is_present | bit | 1 | 1 |  |  |  |

