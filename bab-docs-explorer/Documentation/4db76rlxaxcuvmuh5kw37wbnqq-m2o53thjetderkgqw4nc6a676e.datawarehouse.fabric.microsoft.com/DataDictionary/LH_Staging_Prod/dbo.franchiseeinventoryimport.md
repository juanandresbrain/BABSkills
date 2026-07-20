# dbo.franchiseeinventoryimport

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | varchar | 8000 | 1 |  |  |  |
| InventoryDate | date | 3 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| Cost | decimal | 5 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| Franchisee | varchar | 8000 | 1 |  |  |  |
