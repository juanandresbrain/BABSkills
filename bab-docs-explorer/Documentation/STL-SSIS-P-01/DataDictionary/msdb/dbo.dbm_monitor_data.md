# dbo.dbm_monitor_data

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| database_id | smallint | 2 | 1 |  |  |  |
| role | bit | 1 | 1 |  |  |  |
| status | tinyint | 1 | 1 |  |  |  |
| witness_status | tinyint | 1 | 1 |  |  |  |
| log_flush_rate | bigint | 8 | 1 |  |  |  |
| send_queue_size | bigint | 8 | 1 |  |  |  |
| send_rate | bigint | 8 | 1 |  |  |  |
| redo_queue_size | bigint | 8 | 1 |  |  |  |
| redo_rate | bigint | 8 | 1 |  |  |  |
| transaction_delay | bigint | 8 | 1 |  |  |  |
| transactions_per_sec | bigint | 8 | 1 |  |  |  |
| time | datetime | 8 | 1 |  |  |  |
| end_of_log_lsn | numeric | 13 | 1 |  |  |  |
| failover_lsn | numeric | 13 | 1 |  |  |  |
| local_time | datetime | 8 | 1 |  |  |  |

