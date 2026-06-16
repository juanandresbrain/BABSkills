# dbo.sysutility_mi_volumes_stage_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| volume_device_id | sysname | 256 | 0 |  |  |  |
| volume_name | nvarchar | 520 | 0 |  |  |  |
| capacity_mb | decimal | 13 | 0 |  |  |  |
| free_space_mb | decimal | 13 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 1 |  |  |  |
| virtual_server_name | sysname | 256 | 1 |  |  |  |
| physical_server_name | sysname | 256 | 1 |  |  |  |

