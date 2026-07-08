# dbo.tax_subtotal_line_object

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 1 |  |  |  |
| taxed_line_object | smallint | 2 | 1 |  |  |  |
| tax_line_object | smallint | 2 | 0 |  |  |  |
