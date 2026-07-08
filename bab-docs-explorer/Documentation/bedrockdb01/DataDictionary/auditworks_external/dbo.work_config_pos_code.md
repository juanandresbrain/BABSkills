# dbo.work_config_pos_code

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| request_id | binary | 16 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| code_type | tinyint | 1 | 1 |  |  |  |
| code | smallint | 2 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| pos_description | nvarchar | 1000 | 1 |  |  |  |
| disregard_pos_descr_change | tinyint | 1 | 1 |  |  |  |
| card_type | nchar | 2 | 1 |  |  |  |
| foreign_currency_flag | tinyint | 1 | 1 |  |  |  |
| reference_no_length | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| attachment_type | smallint | 2 | 1 |  |  |  |
| note_type | int | 4 | 0 |  |  |  |
| merchandise_category | tinyint | 1 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| new_code_flag | tinyint | 1 | 0 |  |  |  |
| desc_update_flag | tinyint | 1 | 0 |  |  |  |
| entry_date | datetime | 8 | 0 |  |  |  |
| form_name | nvarchar | 510 | 1 |  |  |  |
| issued_flag | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| transaction_line_string | nvarchar | 510 | 1 |  |  |  |
