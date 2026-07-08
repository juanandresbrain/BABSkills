# dbo.oim_inv_count_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_inv_count_detail_id | numeric | 9 | 0 | YES |  |  |
| oim_inv_count_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| zone_label | nvarchar | 30 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| cost | numeric | 9 | 1 |  |  |  |
| total_retail | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
