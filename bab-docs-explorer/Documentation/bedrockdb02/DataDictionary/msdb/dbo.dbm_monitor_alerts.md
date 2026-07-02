# dbo.dbm_monitor_alerts

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| database_id | smallint | 2 | 1 |  |  |  |
| retention_period | int | 4 | 1 |  |  |  |
| time_behind | int | 4 | 1 |  |  |  |
| enable_time_behind | bit | 1 | 1 |  |  |  |
| send_queue | int | 4 | 1 |  |  |  |
| enable_send_queue | bit | 1 | 1 |  |  |  |
| redo_queue | int | 4 | 1 |  |  |  |
| enable_redo_queue | bit | 1 | 1 |  |  |  |
| average_delay | int | 4 | 1 |  |  |  |
| enable_average_delay | bit | 1 | 1 |  |  |  |

