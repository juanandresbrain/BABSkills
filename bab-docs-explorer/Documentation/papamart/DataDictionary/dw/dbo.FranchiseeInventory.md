# dbo.FranchiseeInventory

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventoryID | varchar | 25 | 0 |  |  |  |
| InventoryLineNo | int | 4 | 0 |  |  |  |
| Franchisee | varchar | 2 | 0 |  |  |  |
| StoreID | varchar | 10 | 1 |  |  |  |
| InventoryDate | date | 3 | 0 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| OnHand | int | 4 | 0 |  |  |  |
| Cost | numeric | 5 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| BatchID | varchar | 52 | 0 |  |  |  |
