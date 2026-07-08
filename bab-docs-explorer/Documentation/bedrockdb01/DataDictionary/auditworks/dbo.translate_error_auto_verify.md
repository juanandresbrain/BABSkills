# dbo.translate_error_auto_verify

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transl_reject_reason | smallint | 2 | 0 |  |  |  |
| output_file_code | nchar | 2 | 0 |  |  |  |
| output_file_column | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| effective_from_date_time | datetime | 8 | 0 |  |  |  |
| effective_until_date_time | datetime | 8 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
