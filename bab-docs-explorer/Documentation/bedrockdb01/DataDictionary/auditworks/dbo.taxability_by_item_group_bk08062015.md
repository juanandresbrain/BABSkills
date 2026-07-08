# dbo.taxability_by_item_group_bk08062015

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_item_group_id | numeric | 9 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_until_date | smalldatetime | 4 | 1 |  |  |  |
