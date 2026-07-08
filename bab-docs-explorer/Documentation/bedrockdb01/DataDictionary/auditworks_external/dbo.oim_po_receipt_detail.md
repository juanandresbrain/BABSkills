# dbo.oim_po_receipt_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_po_receipt_detail_id | numeric | 9 | 0 | YES |  |  |
| oim_po_receipt_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_received | int | 4 | 0 |  |  |  |
| units_damaged | int | 4 | 0 |  |  |  |
| total_retail | numeric | 9 | 1 |  |  |  |
| total_cost | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
