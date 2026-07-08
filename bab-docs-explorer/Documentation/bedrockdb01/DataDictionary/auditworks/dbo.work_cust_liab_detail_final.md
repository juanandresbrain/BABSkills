# dbo.work_cust_liab_detail_final

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
| location_store_no | int | 4 | 1 |  |  |  |
| location_no | int | 4 | 1 |  |  |  |
| amount_outstanding | money | 8 | 0 |  |  |  |
| units_outstanding | unit_datatype | 9 | 0 |  |  |  |
| units_2 | unit_datatype | 9 | 0 |  |  |  |
| units_3 | unit_datatype | 9 | 0 |  |  |  |
| units_4 | unit_datatype | 9 | 0 |  |  |  |
| units_5 | unit_datatype | 9 | 0 |  |  |  |
| existing_detail | tinyint | 1 | 0 |  |  |  |
| discount_line_object | smallint | 2 | 1 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
