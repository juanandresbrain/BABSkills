# dbo.sysutility_ucp_dacs_stub

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dac_id | int | 4 | 0 |  |  |  |
| physical_server_name | sysname | 256 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| dac_name | sysname | 256 | 0 |  |  |  |
| dac_deploy_date | datetime | 8 | 1 |  |  |  |
| dac_description | nvarchar | 8000 | 1 |  |  |  |
| urn | nvarchar | 8000 | 1 |  |  |  |
| powershell_path | nvarchar | 8000 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| dac_percent_total_cpu_utilization | real | 4 | 1 |  |  |  |

