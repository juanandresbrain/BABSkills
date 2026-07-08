# dbo.oim_store_ship_rcpt_dtl

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_store_ship_rcpt_dtl_id | numeric | 9 | 0 | YES |  |  |
| oim_store_ship_rcpt_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_received | int | 4 | 0 |  |  |  |
| force_flag | tinyint | 1 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
