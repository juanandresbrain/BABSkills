# dbo.if_tax_override_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_category | smallint | 2 | 0 |  |  |  |
| taxable | tinyint | 1 | 1 |  |  |  |
| exception_tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| tax_exempt_no | nvarchar | 40 | 1 |  |  |  |
