# dbo.log_shipping_monitor_error_detail

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| agent_id | uniqueidentifier | 16 | 0 |  |  |  |
| agent_type | tinyint | 1 | 0 |  |  |  |
| session_id | int | 4 | 0 |  |  |  |
| database_name | sysname | 256 | 1 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| log_time | datetime | 8 | 0 |  |  |  |
| log_time_utc | datetime | 8 | 0 |  |  |  |
| message | nvarchar | 8000 | 0 |  |  |  |
| source | nvarchar | 8000 | 0 |  |  |  |
| help_url | nvarchar | 8000 | 0 |  |  |  |

