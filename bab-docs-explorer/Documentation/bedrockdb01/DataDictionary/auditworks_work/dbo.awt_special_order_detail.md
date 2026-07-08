# dbo.awt_special_order_detail

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
| units | real | 4 | 0 |  |  |  |
| units_sign | smallint | 2 | 0 |  |  |  |
| salesperson | int | 4 | 0 |  |  |  |
| merchandise_description | varchar | 32 | 1 |  |  |  |
| expecting_delivery_on | varchar | 32 | 1 |  |  |  |
| color_description | varchar | 32 | 1 |  |  |  |
| size_description | varchar | 32 | 1 |  |  |  |
| width_description | varchar | 32 | 1 |  |  |  |
| vendor_name | varchar | 32 | 1 |  |  |  |
| vendor_style_description | varchar | 32 | 1 |  |  |  |
| spo_class_description | varchar | 32 | 1 |  |  |  |
| vendor_no | varchar | 6 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
