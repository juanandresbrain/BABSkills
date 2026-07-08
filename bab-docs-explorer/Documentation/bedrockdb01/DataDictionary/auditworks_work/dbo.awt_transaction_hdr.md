# dbo.awt_transaction_hdr

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| deposit_declaration_flag | tinyint | 1 | 1 |  |  |  |
| tax_jurisdiction_store | int | 4 | 1 |  |  |  |
| pos_tax_jurisdiction | char | 5 | 1 |  |  |  |
| trans_void_flag | smallint | 2 | 1 |  |  |  |
| pos_tender_total | money | 8 | 1 |  |  |  |
| pos_tender_total_sign | smallint | 2 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| closeout_flag | tinyint | 1 | 1 |  |  |  |
| tax_override_flag | tinyint | 1 | 1 |  |  |  |
| transaction_remark | varchar | 255 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| media_count_flag | tinyint | 1 | 1 |  |  |  |
| if_rejection_flag | tinyint | 1 | 1 |  |  |  |
| tender_total | money | 8 | 1 |  |  |  |
