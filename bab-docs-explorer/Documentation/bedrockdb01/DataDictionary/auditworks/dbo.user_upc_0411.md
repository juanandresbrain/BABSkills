# dbo.user_upc_0411

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| pos_identifier | varchar | 20 | 0 |  |  |  |
| pos_identifier_type | tinyint | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| prim_size_label | varchar | 8 | 1 |  |  |  |
| sec_size_label | varchar | 8 | 1 |  |  |  |
| size_master_id | numeric | 9 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
