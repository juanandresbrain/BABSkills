# dbo.sysutility_mi_session_statistics_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collection_time | datetimeoffset | 10 | 0 | YES |  |  |
| session_id | int | 4 | 0 | YES |  |  |
| dac_instance_name | sysname | 256 | 0 | YES |  |  |
| database_name | sysname | 256 | 0 | YES |  |  |
| login_time | datetime | 8 | 0 | YES |  |  |
| cumulative_cpu_ms | int | 4 | 0 |  |  |  |

