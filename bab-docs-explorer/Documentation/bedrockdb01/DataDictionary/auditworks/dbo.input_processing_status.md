# dbo.input_processing_status

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 | YES |  |  |
| process_start_datetime | datetime | 8 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| processing_message | nvarchar | 510 | 1 |  |  |  |
| status | smallint | 2 | 0 |  |  |  |
| instance_id | smallint | 2 | 1 |  |  |  |
| to_instance_id | smallint | 2 | 1 |  |  |  |
| request_date | datetime | 8 | 1 |  |  |  |
| request_id | numeric | 9 | 1 |  |  |  |
