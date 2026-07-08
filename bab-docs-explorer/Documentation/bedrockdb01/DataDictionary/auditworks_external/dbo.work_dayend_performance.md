# dbo.work_dayend_performance

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | int | 4 | 0 |  |  |  |
| stream_no | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| duration | numeric | 9 | 0 |  |  |  |
| transaction_count | int | 4 | 0 |  |  |  |
| store_count | int | 4 | 0 |  |  |  |
| transactions_per_hour | numeric | 9 | 0 |  |  |  |
