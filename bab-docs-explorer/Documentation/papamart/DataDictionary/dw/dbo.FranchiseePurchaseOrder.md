# dbo.FranchiseePurchaseOrder

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 2 | 0 |  |  |  |
| PurchaseOrderID | varchar | 20 | 0 |  |  |  |
| PurchaseOrderLineID | int | 4 | 0 |  |  |  |
| WarehouseID | varchar | 10 | 1 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| Units | int | 4 | 0 |  |  |  |
| LinePrice | numeric | 5 | 0 |  |  |  |
| DueDate | date | 3 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| BatchID | varchar | 52 | 0 |  |  |  |
