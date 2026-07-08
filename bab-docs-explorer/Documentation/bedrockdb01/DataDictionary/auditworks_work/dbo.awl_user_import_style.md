# dbo.awl_user_import_style

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| style_long_description | nvarchar | 240 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| cost | money | 8 | 0 |  |  |  |
| subclass_code | smallint | 2 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| style_short_description | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
