# dbo.oim_rtv_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_rtv_detail_id | numeric | 9 | 0 | YES |  |  |
| oim_rtv_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| from_stock_status_code | nvarchar | 6 | 1 |  |  |  |
| units_sent | int | 4 | 0 |  |  |  |
| unit_cost | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
