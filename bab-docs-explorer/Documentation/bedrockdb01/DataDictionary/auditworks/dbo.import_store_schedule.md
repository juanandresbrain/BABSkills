# dbo.import_store_schedule

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| schedule_date | smalldatetime | 4 | 0 |  |  |  |
| open_closed_flag | tinyint | 1 | 0 |  |  |  |
| closed_reason_code | tinyint | 1 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
