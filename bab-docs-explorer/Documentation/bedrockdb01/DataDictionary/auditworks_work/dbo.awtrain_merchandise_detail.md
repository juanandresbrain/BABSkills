# dbo.awtrain_merchandise_detail

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
| line_id | numeric | 5 | 0 |  |  |  |
| merchandise_category | tinyint | 1 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| units_sign | smallint | 2 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| price_override | tinyint | 1 | 0 |  |  |  |
| pos_iplu_missing | tinyint | 1 | 0 |  |  |  |
| pos_deptclass | int | 4 | 0 |  |  |  |
| pos_no_hit_deptclass | int | 4 | 0 |  |  |  |
| ticket_price | numeric | 9 | 0 |  |  |  |
| sold_at_price | numeric | 9 | 0 |  |  |  |
| pos_identifier | varchar | 20 | 0 |  |  |  |
| scanned | tinyint | 1 | 0 |  |  |  |
| pos_identifier_type | tinyint | 1 | 0 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
