# dbo.work_media_counts

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_type | tinyint | 1 | 0 |  |  |  |
| media_category | tinyint | 1 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| media_amount | money | 8 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| transaction_qty | unit_datatype | 9 | 0 |  |  |  |
| transaction_qty_for_avg | unit_datatype | 9 | 0 |  |  |  |
