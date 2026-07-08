# dbo.valid_line_object_type_action

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| default_db_cr_none | smallint | 2 | 0 |  |  |  |
| default_merchandise_category | smallint | 2 | 1 |  |  |  |
| default_reference_type | smallint | 2 | 0 |  |  |  |
| default_discountable_group | smallint | 2 | 1 |  |  |  |
| basic_db_cr_type | tinyint | 1 | 0 |  |  |  |
| store_balance_group | tinyint | 1 | 1 |  |  |  |
| store_balance_column | tinyint | 1 | 1 |  |  |  |
| auto_config_flag | tinyint | 1 | 0 |  |  |  |
| default_transaction_category | tinyint | 1 | 0 |  |  |  |
| default_media_category | tinyint | 1 | 0 |  |  |  |
