# dbo.awl_special_order_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| units | real | 4 | 0 |  |  |  |
| units_sign | smallint | 2 | 0 |  |  |  |
| salesperson | int | 4 | 0 |  |  |  |
| merchandise_description | nvarchar | 64 | 1 |  |  |  |
| expecting_delivery_on | nvarchar | 64 | 1 |  |  |  |
| color_description | nvarchar | 64 | 1 |  |  |  |
| size_description | nvarchar | 64 | 1 |  |  |  |
| width_description | nvarchar | 64 | 1 |  |  |  |
| vendor_name | nvarchar | 64 | 1 |  |  |  |
| vendor_style_description | nvarchar | 64 | 1 |  |  |  |
| spo_class_description | nvarchar | 64 | 1 |  |  |  |
| vendor_no | nvarchar | 12 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
