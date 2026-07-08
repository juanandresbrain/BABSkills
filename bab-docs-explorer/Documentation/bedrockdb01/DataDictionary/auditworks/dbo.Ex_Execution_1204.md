# dbo.Ex_Execution_1204

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| queue_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| from_serial_no | numeric | 9 | 0 |  |  |  |
| to_serial_no | numeric | 9 | 0 |  |  |  |
| status_code | tinyint | 1 | 1 |  |  |  |
| verified | datetime | 8 | 1 |  |  |  |
