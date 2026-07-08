# dbo.user_style_0411

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| style_long_description | varchar | 120 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| cost | money | 8 | 1 |  |  |  |
| subclass_code | tinyint | 1 | 0 |  |  |  |
| style_short_description | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
