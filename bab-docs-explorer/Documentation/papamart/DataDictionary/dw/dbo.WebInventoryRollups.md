# dbo.WebInventoryRollups

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 6 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| StoreInventoryUS | int | 4 | 1 |  |  |  |
| StoreInventoryUK | int | 4 | 1 |  |  |  |
| WebInventoryUS | int | 4 | 1 |  |  |  |
| WebInventoryUK | int | 4 | 1 |  |  |  |
| WarehouseInventoryUS | int | 4 | 1 |  |  |  |
| WarehouseInventoryUK | int | 4 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
