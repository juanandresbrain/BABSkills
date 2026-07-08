# dbo.stock_control_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| upc_on_file_flag | tinyint | 1 | 0 |  |  |  |
| store_on_file_flag | tinyint | 1 | 0 |  |  |  |
| merchandise_key | numeric | 9 | 1 |  |  |  |
| initiated_by_host | tinyint | 1 | 0 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| other_store_no | int | 4 | 1 |  |  |  |
| location_no | int | 4 | 1 |  |  |  |
| vendor_no | nvarchar | 3000 | 1 |  |  |  |
| count_date | datetime | 8 | 1 |  |  |  |
| pos_identifier | nvarchar | 3000 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| reason | nvarchar | 3000 | 1 |  |  |  |
| imrd | nvarchar | 3000 | 1 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
