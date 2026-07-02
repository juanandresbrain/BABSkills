# dbo.sysutility_ucp_cpu_utilization_stub

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| aggregation_type | tinyint | 1 | 0 |  |  |  |
| object_type | tinyint | 1 | 0 |  |  |  |
| physical_server_name | sysname | 256 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| database_name | sysname | 256 | 0 |  |  |  |
| percent_total_cpu_utilization | real | 4 | 1 |  |  |  |

