# dbo.sysutility_ucp_logfiles_stub

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| urn | nvarchar | 3000 | 1 |  |  |  |
| powershell_path | nvarchar | -1 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| database_name | sysname | 256 | 0 |  |  |  |
| parent_urn | nvarchar | 1560 | 1 |  |  |  |
| physical_server_name | sysname | 256 | 0 |  |  |  |
| volume_name | sysname | 256 | 0 |  |  |  |
| volume_device_id | sysname | 256 | 0 |  |  |  |
| Growth | real | 4 | 1 |  |  |  |
| GrowthType | smallint | 2 | 1 |  |  |  |
| MaxSize | real | 4 | 1 |  |  |  |
| Name | nvarchar | 256 | 1 |  |  |  |
| Size | real | 4 | 1 |  |  |  |
| UsedSpace | real | 4 | 1 |  |  |  |
| FileName | nvarchar | 520 | 1 |  |  |  |
| VolumeFreeSpace | bigint | 8 | 1 |  |  |  |
| available_space | real | 4 | 1 |  |  |  |

