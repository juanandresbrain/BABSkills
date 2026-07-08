# dbo.work_unposted_transactions

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| instance_id | smallint | 2 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_description | nvarchar | 60 | 0 |  |  |  |
| object_id | int | 4 | 1 |  |  |  |
| posted_transaction | numeric | 9 | 0 |  |  |  |
| unposted_transaction | numeric | 9 | 0 |  |  |  |
| min_posted_serial_no | numeric | 9 | 0 |  |  |  |
| max_posted_serial_no | numeric | 9 | 0 |  |  |  |
