# dbo.work_auto_complete_trans_line

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| row_id | numeric | 13 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| item_line_id | numeric | 5 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| originating_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| originating_line_id | numeric | 5 | 0 |  |  |  |
| originating_units | unit_datatype | 9 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| price_override | tinyint | 1 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| originating_date | smalldatetime | 4 | 0 |  |  |  |
| current_flag | tinyint | 1 | 0 |  |  |  |
| order_line_object | smallint | 2 | 0 |  |  |  |
| pmt_line_object | smallint | 2 | 0 |  |  |  |
| originating_tender_line_id | numeric | 5 | 0 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| originating_line_id2 | numeric | 5 | 1 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| reference_no_length | tinyint | 1 | 1 |  |  |  |
| auto_complete_transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| source_store_no | int | 4 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| serial_no | nvarchar | 160 | 1 |  |  |  |
