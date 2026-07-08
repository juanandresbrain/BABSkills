# dbo.work_upc_trail_edit

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| before_upc_no | numeric | 9 | 0 |  |  |  |
| after_upc_no | numeric | 9 | 0 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 0 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| class_code | int | 4 | 1 |  |  |  |
| subclass_code | smallint | 2 | 1 |  |  |  |
| sku_lookup_flag | smallint | 2 | 1 |  |  |  |
| cost | line_amount | 9 | 1 |  |  |  |
