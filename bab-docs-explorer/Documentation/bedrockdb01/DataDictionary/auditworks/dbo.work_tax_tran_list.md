# dbo.work_tax_tran_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 1 |  |  |  |
| old_upc_no | numeric | 9 | 1 |  |  |  |
| old_sku_id | numeric | 9 | 1 |  |  |  |
| old_style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| old_class_code | int | 4 | 1 |  |  |  |
| old_subclass_code | smallint | 2 | 1 |  |  |  |
| old_upc_on_file_flag | tinyint | 1 | 1 |  |  |  |
| old_upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| old_cost | line_amount_18_4 | 9 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
