# dbo.work_cust_detail_in

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| discount_line_object | smallint | 2 | 1 |  |  |  |
| amount_outstanding_in | money | 8 | 0 |  |  |  |
| units_outstanding_in | unit_datatype | 9 | 0 |  |  |  |
| units_2_in | unit_datatype | 9 | 0 |  |  |  |
| units_3_in | unit_datatype | 9 | 0 |  |  |  |
| units_4_in | unit_datatype | 9 | 0 |  |  |  |
| units_5_in | unit_datatype | 9 | 0 |  |  |  |
