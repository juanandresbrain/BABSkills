# dbo.franchiseepurchaseorder

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderID | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderLineID | int | 4 | 1 |  |  |  |
| WarehouseID | varchar | 8000 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| LinePrice | decimal | 5 | 1 |  |  |  |
| DueDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
