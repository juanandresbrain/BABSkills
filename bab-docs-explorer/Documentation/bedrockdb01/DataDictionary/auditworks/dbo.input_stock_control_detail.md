# dbo.input_stock_control_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| merchandise_key | numeric | 9 | 1 |  |  |  |
| initiated_by_host | tinyint | 1 | 0 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| other_store_no | int | 4 | 1 |  |  |  |
| location_no | int | 4 | 1 |  |  |  |
| vendor_no | nvarchar | 3000 | 1 |  |  |  |
| count_date | datetime | 8 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| pos_identifier | nvarchar | 3000 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| reason | nvarchar | -1 | 1 |  |  |  |
| imrd | nvarchar | 3000 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 40 | 1 |  |  |  |
| pos_description | nvarchar | 510 | 1 |  |  |  |
| lookup_pos_code_imrd | nvarchar | 40 | 1 |  |  |  |
| pos_description_imrd | nvarchar | 510 | 1 |  |  |  |
| lookup_pos_code_vendor | nvarchar | 40 | 1 |  |  |  |
| pos_description_vendor | nvarchar | 510 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
