# dbo.rebuild_request_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| request_id | numeric | 9 | 0 |  |  |  |
| rebuild_type | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| request_status | smallint | 2 | 0 |  |  |  |
| process_id | tinyint | 1 | 0 |  |  |  |
| copied_from_request_id | numeric | 9 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
