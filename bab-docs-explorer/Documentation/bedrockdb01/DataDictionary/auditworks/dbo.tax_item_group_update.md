# dbo.tax_item_group_update

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_name | nvarchar | 60 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| class_code | int | 4 | 1 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 0 |  |  |  |
| last_modified_date_time | datetime | 8 | 0 |  |  |  |
