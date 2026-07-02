# dbo.sysutility_ucp_filegroups_stub

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| urn | nvarchar | 1560 | 1 |  |  |  |
| powershell_path | nvarchar | -1 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| database_name | sysname | 256 | 0 |  |  |  |
| parent_urn | nvarchar | 1024 | 1 |  |  |  |
| Name | nvarchar | 256 | 1 |  |  |  |

