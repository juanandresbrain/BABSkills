# dbo.sysutility_ucp_computers_stub

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| virtual_server_name | sysname | 256 | 0 |  |  |  |
| physical_server_name | sysname | 256 | 0 |  |  |  |
| is_clustered_server | int | 4 | 1 |  |  |  |
| num_processors | int | 4 | 1 |  |  |  |
| cpu_name | nvarchar | 256 | 1 |  |  |  |
| cpu_caption | nvarchar | 256 | 1 |  |  |  |
| cpu_family | nvarchar | 256 | 1 |  |  |  |
| cpu_architecture | nvarchar | 128 | 1 |  |  |  |
| cpu_max_clock_speed | decimal | 9 | 1 |  |  |  |
| cpu_clock_speed | decimal | 9 | 1 |  |  |  |
| l2_cache_size | decimal | 9 | 1 |  |  |  |
| l3_cache_size | decimal | 9 | 1 |  |  |  |
| urn | nvarchar | 8000 | 1 |  |  |  |
| powershell_path | nvarchar | 8000 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| percent_total_cpu_utilization | real | 4 | 1 |  |  |  |

