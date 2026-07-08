# dbo.work_media_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| denominator | money | 8 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| avoid_zero | tinyint | 1 | 0 |  |  |  |
