# dbo.work_auto_complete_trans_dtl

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| row_id | numeric | 13 | 0 | YES |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reversal_sign | smallint | 2 | 0 |  |  |  |
| item_line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| source_store_no | int | 4 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| originating_transaction_id | numeric | 9 | 1 |  |  |  |
| originating_line_id | numeric | 5 | 1 |  |  |  |
| originating_units | unit_datatype | 9 | 1 |  |  |  |
| merchandise_category | tinyint | 1 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| price_override | tinyint | 1 | 1 |  |  |  |
| pos_iplu_missing | tinyint | 1 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| pos_no_hit_deptclass | int | 4 | 1 |  |  |  |
| ticket_price | numeric | 9 | 1 |  |  |  |
| sold_at_price | numeric | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| scanned | tinyint | 1 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| reference_no_length | tinyint | 1 | 0 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| auto_complete_transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| serial_no | nvarchar | 160 | 1 |  |  |  |
| cost | numeric | 9 | 1 |  |  |  |
