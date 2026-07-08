# dbo.work_upc_template

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| replace_upc_no | numeric | 9 | 1 |  |  |  |
| replace_upc_flag | tinyint | 1 | 1 |  |  |  |
| stock_merch_flag | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| class_code | int | 4 | 1 |  |  |  |
| subclass_code | smallint | 2 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| interface_id | tinyint | 1 | 1 |  |  |  |
| interface_status_flag | smallint | 2 | 1 |  |  |  |
| all_rejects_fixed | tinyint | 1 | 1 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| ticket_price | line_amount_18_4 | 9 | 1 |  |  |  |
| sold_at_price | line_amount_18_4 | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| cost | line_amount_18_4 | 9 | 1 |  |  |  |
