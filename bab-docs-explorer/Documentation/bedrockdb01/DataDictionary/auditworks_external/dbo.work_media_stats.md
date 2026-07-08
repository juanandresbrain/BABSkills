# dbo.work_media_stats

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| media_category | tinyint | 1 | 0 |  |  |  |
| media_amount | money | 8 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
