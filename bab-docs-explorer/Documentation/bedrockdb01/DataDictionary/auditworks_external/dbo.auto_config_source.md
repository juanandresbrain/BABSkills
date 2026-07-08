# dbo.auto_config_source

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| config_type | tinyint | 1 | 0 |  |  |  |
| item_type | smallint | 2 | 0 |  |  |  |
| item_code | smallint | 2 | 0 |  |  |  |
| attachment_type | smallint | 2 | 1 |  |  |  |
| attachment_subtype | numeric | 9 | 1 |  |  |  |
| desc_update_flag | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
