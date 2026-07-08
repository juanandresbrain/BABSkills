# dbo.upc_sa

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| style_reference_id | numeric | 9 | 0 |  |  |  |
| style_short_description | varchar | 20 | 1 |  |  |  |
| style_long_description | varchar | 120 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| subclass_code | tinyint | 1 | 0 |  |  |  |
| class_description | varchar | 30 | 0 |  |  |  |
| class_short_description | varchar | 12 | 1 |  |  |  |
| department_code | smallint | 2 | 0 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 4 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| prim_size_label | varchar | 8 | 1 |  |  |  |
| sec_size_label | varchar | 8 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
