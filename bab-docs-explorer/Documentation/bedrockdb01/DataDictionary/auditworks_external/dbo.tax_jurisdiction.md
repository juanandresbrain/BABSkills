# dbo.tax_jurisdiction

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_jurisdiction_id | numeric | 9 | 0 | YES |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| jurisdiction_name | nvarchar | 100 | 0 |  |  |  |
| gl_replacement_value | nvarchar | 40 | 1 |  |  |  |
| pos_tax_jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
