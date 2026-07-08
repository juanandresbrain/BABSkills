# dbo.oim_inv_count

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_inv_count_id | numeric | 9 | 0 |  |  |  |
| inventory_control_no | nvarchar | 40 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
