# dbo.import_tax_rate_compound_level

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
