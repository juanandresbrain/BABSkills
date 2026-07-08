# dbo.shap_if_merchandise_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| merchandise_category | smallint | 2 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| subclass_code | tinyint | 1 | 0 |  |  |  |
| price_override | tinyint | 1 | 0 |  |  |  |
| pos_iplu_missing | tinyint | 1 | 0 |  |  |  |
| upc_on_file_flag | tinyint | 1 | 0 |  |  |  |
| pos_deptclass | int | 4 | 0 |  |  |  |
| ticket_price | line_amount | 9 | 0 |  |  |  |
| sold_at_price | line_amount | 9 | 0 |  |  |  |
| scanned | tinyint | 1 | 1 |  |  |  |
| pos_identifier | varchar | 20 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| plu_price | line_amount | 9 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
