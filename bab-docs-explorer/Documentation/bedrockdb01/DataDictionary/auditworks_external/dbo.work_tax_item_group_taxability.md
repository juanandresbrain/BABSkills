# dbo.work_tax_item_group_taxability

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| tax_item_group_id | numeric | 9 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_until_date | smalldatetime | 4 | 1 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| source_code | nvarchar | 20 | 1 |  |  |  |
| posting_datetime | datetime | 8 | 1 |  |  |  |
