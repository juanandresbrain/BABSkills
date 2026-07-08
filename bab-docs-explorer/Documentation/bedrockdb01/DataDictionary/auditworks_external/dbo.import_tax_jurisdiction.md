# dbo.import_tax_jurisdiction

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| remit_to_location_type | tinyint | 1 | 0 |  |  |  |
| remit_to_location_code | nchar | 6 | 0 |  |  |  |
| jurisdiction_name | nchar | 100 | 0 |  |  |  |
| pos_tax_jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
