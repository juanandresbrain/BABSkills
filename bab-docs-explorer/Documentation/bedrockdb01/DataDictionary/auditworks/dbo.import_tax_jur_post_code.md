# dbo.import_tax_jur_post_code

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| from_post_code | nvarchar | 40 | 0 |  |  |  |
| to_post_code | nvarchar | 40 | 0 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
