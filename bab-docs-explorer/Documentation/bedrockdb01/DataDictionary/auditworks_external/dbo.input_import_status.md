# dbo.input_import_status

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_batch_id | numeric | 9 | 0 | YES |  |  |
| process_start_datetime | datetime | 8 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| processing_message | nvarchar | 510 | 1 |  |  |  |
| status | smallint | 2 | 0 |  |  |  |
