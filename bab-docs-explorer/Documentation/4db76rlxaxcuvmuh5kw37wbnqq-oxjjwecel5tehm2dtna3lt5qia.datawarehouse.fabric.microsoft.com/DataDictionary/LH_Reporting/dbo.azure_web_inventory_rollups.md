# dbo.azure_web_inventory_rollups

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
| StyleCode | varchar | 8000 | 1 |  |  |  |
| StoreInventoryUS | int | 4 | 1 |  |  |  |
| StoreInventoryUK | int | 4 | 1 |  |  |  |
| WebInventoryUS | int | 4 | 1 |  |  |  |
| WebInventoryUK | int | 4 | 1 |  |  |  |
| WarehouseInventoryUS | int | 4 | 1 |  |  |  |
| WarehouseInventoryUK | int | 4 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
