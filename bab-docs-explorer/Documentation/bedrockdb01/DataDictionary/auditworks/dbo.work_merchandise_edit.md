# dbo.work_merchandise_edit

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| subclass_code | smallint | 2 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| price_override | tinyint | 1 | 0 |  |  |  |
| pos_iplu_missing | tinyint | 1 | 0 |  |  |  |
| pos_deptclass | int | 4 | 0 |  |  |  |
| gross_line_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| net_line_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| merchandise_category | smallint | 2 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| upc_on_file_flag | tinyint | 1 | 0 |  |  |  |
| salesperson_on_file | int | 4 | 1 |  |  |  |
| salesperson2_on_file | tinyint | 1 | 1 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| non_void_flag | smallint | 2 | 0 |  |  |  |
| scanned | tinyint | 1 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| original_upc_no | numeric | 9 | 1 |  |  |  |
| upc_replaced_flag | numeric | 5 | 0 |  |  |  |
| plu_amount | line_amount_18_4 | 9 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| line_object_changed_flag | tinyint | 1 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| attachment_type | smallint | 2 | 1 |  |  |  |
| source_store_no | int | 4 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| cost | line_amount_18_4 | 9 | 1 |  |  |  |
