# dbo.FranchiseePurchaseOrderIMPORT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderID | varchar | 20 | 0 |  |  |  |
| WarehouseID | varchar | 10 | 1 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| Units | int | 4 | 0 |  |  |  |
| LinePrice | numeric | 5 | 0 |  |  |  |
| DueDate | date | 3 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| Franchisee | varchar | 2 | 0 |  |  |  |
