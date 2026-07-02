# dbo.backupfilegroup

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| backup_set_id | int | 4 | 0 | YES | YES |  |
| name | nvarchar | 256 | 0 |  |  |  |
| filegroup_id | int | 4 | 0 | YES |  |  |
| filegroup_guid | uniqueidentifier | 16 | 1 |  |  |  |
| type | char | 2 | 0 |  |  |  |
| type_desc | nvarchar | 120 | 0 |  |  |  |
| is_default | bit | 1 | 0 |  |  |  |
| is_readonly | bit | 1 | 0 |  |  |  |
| log_filegroup_guid | uniqueidentifier | 16 | 1 |  |  |  |

