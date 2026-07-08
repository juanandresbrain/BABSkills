# dbo.store_balance_group_heading

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_balance_group | tinyint | 1 | 0 |  |  |  |
| store_balance_section | tinyint | 1 | 0 |  |  |  |
| store_balance_group_descr | nvarchar | 100 | 0 |  |  |  |
| column1_heading | nvarchar | 100 | 0 |  |  |  |
| column2_heading | nvarchar | 100 | 0 |  |  |  |
| column3_heading | nvarchar | 100 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| column1_resource_id | numeric | 9 | 1 |  |  |  |
| column2_resource_id | numeric | 9 | 1 |  |  |  |
| column3_resource_id | numeric | 9 | 1 |  |  |  |
