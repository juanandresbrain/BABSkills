# dbo.franchiseepurchaseorderimport

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderID | varchar | 8000 | 1 |  |  |  |
| WarehouseID | varchar | 8000 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| LinePrice | decimal | 5 | 1 |  |  |  |
| DueDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| Franchisee | varchar | 8000 | 1 |  |  |  |
