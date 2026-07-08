# dbo.work_adt_trl

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| entry_id | binary | 16 | 0 |  |  |  |
| entry_date | datetime | 8 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| sales_date | smalldatetime | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| processing_status | smallint | 2 | 1 |  |  |  |
