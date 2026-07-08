# dbo.oim_out_xfer_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_out_xfer_detail_id | numeric | 9 | 0 | YES |  |  |
| oim_out_xfer_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| reason_code | nvarchar | 10 | 1 |  |  |  |
| units_sent | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
