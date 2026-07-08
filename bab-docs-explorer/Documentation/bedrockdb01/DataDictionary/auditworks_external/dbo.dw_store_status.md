# dbo.dw_store_status

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| store_status | tinyint | 1 | 0 |  |  |  |
| instance_id | smallint | 2 | 0 |  |  |  |
| source_media_rec_recovery_id | smallint | 2 | 1 |  |  |  |
| subledger_copied_flag | tinyint | 1 | 0 |  |  |  |
