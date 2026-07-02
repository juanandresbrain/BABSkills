# dbo.sysutility_mi_cpu_stage_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| num_processors | int | 4 | 0 |  |  |  |
| cpu_name | nvarchar | 256 | 0 |  |  |  |
| cpu_caption | nvarchar | 256 | 0 |  |  |  |
| cpu_family_id | decimal | 5 | 0 |  |  |  |
| cpu_architecture_id | decimal | 5 | 0 |  |  |  |
| cpu_max_clock_speed | decimal | 9 | 0 |  |  |  |
| cpu_clock_speed | decimal | 9 | 0 |  |  |  |
| l2_cache_size | decimal | 9 | 0 |  |  |  |
| l3_cache_size | decimal | 9 | 0 |  |  |  |
| instance_processor_usage_start_ticks | decimal | 13 | 0 |  |  |  |
| instance_collect_time_start_ticks | decimal | 13 | 0 |  |  |  |
| computer_processor_idle_start_ticks | decimal | 13 | 0 |  |  |  |
| computer_collect_time_start_ticks | decimal | 13 | 0 |  |  |  |
| instance_processor_usage_end_ticks | decimal | 13 | 0 |  |  |  |
| instance_collect_time_end_ticks | decimal | 13 | 0 |  |  |  |
| computer_processor_idle_end_ticks | decimal | 13 | 0 |  |  |  |
| computer_collect_time_end_ticks | decimal | 13 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 1 |  |  |  |
| virtual_server_name | sysname | 256 | 1 |  |  |  |
| physical_server_name | sysname | 256 | 1 |  |  |  |
| instance_processor_usage_percentage | real | 4 | 1 |  |  |  |
| computer_processor_usage_percentage | real | 4 | 1 |  |  |  |

