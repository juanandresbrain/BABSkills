# dbo.scaleout_execution

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | smallint | 2 | 0 |  |  |  |
| queue_id | int | 4 | 0 |  |  |  |
| posting_date | smalldatetime | 4 | 0 |  |  |  |
| instance_from_serial_no | numeric | 9 | 0 |  |  |  |
| instance_to_serial_no | numeric | 9 | 1 |  |  |  |
| status_code | tinyint | 1 | 1 |  |  |  |
