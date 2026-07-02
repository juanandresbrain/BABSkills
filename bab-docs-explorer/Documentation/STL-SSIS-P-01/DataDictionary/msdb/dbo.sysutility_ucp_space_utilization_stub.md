# dbo.sysutility_ucp_space_utilization_stub

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| processing_time | datetimeoffset | 10 | 0 |  |  |  |
| aggregation_type | tinyint | 1 | 0 |  |  |  |
| object_type | tinyint | 1 | 0 |  |  |  |
| virtual_server_name | sysname | 256 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| volume_device_id | sysname | 256 | 0 |  |  |  |
| database_name | sysname | 256 | 0 |  |  |  |
| filegroup_name | sysname | 256 | 0 |  |  |  |
| dbfile_name | sysname | 256 | 0 |  |  |  |
| used_space_bytes | real | 4 | 1 |  |  |  |
| allocated_space_bytes | real | 4 | 1 |  |  |  |
| total_space_bytes | real | 4 | 1 |  |  |  |
| available_space_bytes | real | 4 | 1 |  |  |  |

