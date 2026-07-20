# dbo.integrationstaging_web_vwstoreinventorybuffer

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GTIN | varchar | 8000 | 1 |  |  |  |
| TotalQuantity | int | 4 | 1 |  |  |  |
| ProtectedQuantity | int | 4 | 1 |  |  |  |
| WarehouseCode | varchar | 8000 | 1 |  |  |  |
| CustomerSKU | varchar | 8000 | 1 |  |  |  |
| ProductCode | varchar | 8000 | 1 |  |  |  |
| Attribute1 | varchar | 8000 | 1 |  |  |  |
| PreBackOrderQuantity | varchar | 8000 | 1 |  |  |  |
| InStockDateUTC | varchar | 8000 | 1 |  |  |  |
| InventoryType | varchar | 8000 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 1 |  |  |  |
| StoreInventoryBuffer | int | 4 | 1 |  |  |  |
