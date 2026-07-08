# dbo.awl_user_import_upc

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| color_code | nvarchar | 8 | 1 |  |  |  |
| color_short_description | nvarchar | 16 | 1 |  |  |  |
| prim_size_label | nvarchar | 16 | 1 |  |  |  |
| sec_size_label | nvarchar | 16 | 1 |  |  |  |
| size_master_id | numeric | 9 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
