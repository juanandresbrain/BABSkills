# dbo.if_special_order_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| units | real | 4 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| merchandise_description | nvarchar | 64 | 1 |  |  |  |
| expecting_delivery_on | nvarchar | 64 | 1 |  |  |  |
| color_description | nvarchar | 64 | 1 |  |  |  |
| size_description | nvarchar | 64 | 1 |  |  |  |
| width_description | nvarchar | 64 | 1 |  |  |  |
| vendor_name | nvarchar | 64 | 1 |  |  |  |
| vendor_style_description | nvarchar | 64 | 1 |  |  |  |
| spo_class_description | nvarchar | 64 | 1 |  |  |  |
| vendor_no | nchar | 12 | 1 |  |  |  |
