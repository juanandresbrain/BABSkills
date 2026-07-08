# dbo.taxability_by_style

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_until_date | smalldatetime | 4 | 1 |  |  |  |
