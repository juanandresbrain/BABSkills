# dbo.work_merchandise_move

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| sku_id | float | 8 | 1 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| class_code | int | 4 | 1 |  |  |  |
| subclass_code | int | 4 | 1 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| price_override | tinyint | 1 | 0 |  |  |  |
| ticket_price | line_amount_18_4 | 9 | 1 |  |  |  |
| sold_at_price | line_amount_18_4 | 9 | 1 |  |  |  |
| plu_price | line_amount_18_4 | 9 | 1 |  |  |  |
| gross_line_amount | line_amount_18_4 | 9 | 1 |  |  |  |
| merchandise_category | smallint | 2 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| upc_on_file_flag | tinyint | 1 | 0 |  |  |  |
| salesperson_on_file | tinyint | 1 | 1 |  |  |  |
| salesperson2_on_file | tinyint | 1 | 1 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| tax_override | tinyint | 1 | 1 |  |  |  |
| merch_stock_flag | tinyint | 1 | 1 |  |  |  |
| attachment_mandatory | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| source_store_no | int | 4 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| cost | line_amount_18_4 | 9 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
