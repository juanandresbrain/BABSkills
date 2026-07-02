# dbo.sysutility_ucp_volumes_stub

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 |  |  |  |
| virtual_server_name | sysname | 256 | 0 |  |  |  |
| physical_server_name | sysname | 256 | 0 |  |  |  |
| volume_device_id | sysname | 256 | 0 |  |  |  |
| volume_name | sysname | 256 | 0 |  |  |  |
| total_space_available | real | 4 | 1 |  |  |  |
| free_space | real | 4 | 1 |  |  |  |
| total_space_utilized | real | 4 | 1 |  |  |  |
| percent_total_space_utilization | real | 4 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| powershell_path | nvarchar | 8000 | 1 |  |  |  |

