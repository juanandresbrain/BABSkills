# dbo.tax_default_backup

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_jurisdiction | char | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_until_date | smalldatetime | 4 | 1 |  |  |  |
| inserted_by_trigger | tinyint | 1 | 1 |  |  |  |
