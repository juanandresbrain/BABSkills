# dbo.import_taxability_by_style

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| entry_subtype | nchar | 2 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| item_id | nvarchar | 40 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 1 |  |  |  |
| item_no | item_no_datatype | 9 | 1 |  |  |  |
| effective_from_date | smalldatetime | 4 | 1 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
