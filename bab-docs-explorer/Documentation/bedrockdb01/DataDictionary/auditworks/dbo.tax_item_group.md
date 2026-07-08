# dbo.tax_item_group

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_item_group_id | numeric | 9 | 0 |  |  |  |
| tax_item_group_code | nvarchar | 20 | 0 |  |  |  |
| tax_item_group_description | nvarchar | 100 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| auto_gen_datetime | datetime | 8 | 1 |  |  |  |
| auto_gen_source | nvarchar | 100 | 1 |  |  |  |
