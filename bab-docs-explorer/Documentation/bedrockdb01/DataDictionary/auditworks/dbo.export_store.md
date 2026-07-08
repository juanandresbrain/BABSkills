# dbo.export_store

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| tax_jurisdiction | char | 5 | 0 |  |  |  |
| tax_strip_table_no | tinyint | 1 | 0 |  |  |  |
| media_parameter_table_no | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| deposit_balancing_method | smallint | 2 | 0 |  |  |  |
| petty_cash_line_object | smallint | 2 | 1 |  |  |  |
| multiple_mediacounts_added | tinyint | 1 | 0 |  |  |  |
| autoaccept_flag | tinyint | 1 | 0 |  |  |  |
| tax_strip_flag | tinyint | 1 | 0 |  |  |  |
| outlet_store_flag | tinyint | 1 | 0 |  |  |  |
| settlement_billing_name | varchar | 20 | 1 |  |  |  |
| store_deposit_destination | smallint | 2 | 0 |  |  |  |
| interstore_export_region | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| gl_store | varchar | 20 | 0 |  |  |  |
| country_id | numeric | 9 | 1 |  |  |  |
| timezone_offset_hours | numeric | 5 | 1 |  |  |  |
| city | varchar | 20 | 1 |  |  |  |
| state_code | varchar | 2 | 1 |  |  |  |
| zip_code | varchar | 20 | 1 |  |  |  |
| comp_date | smalldatetime | 4 | 1 |  |  |  |
| store_export_code | varchar | 3 | 0 |  |  |  |
| open_date | smalldatetime | 4 | 1 |  |  |  |
| log_tax_override | tinyint | 1 | 1 |  |  |  |
| currency_id | numeric | 9 | 1 |  |  |  |
| email_address | varchar | 255 | 1 |  |  |  |
