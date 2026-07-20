# dbo.tmp_franchiseefilesimportselectinventoryinsert_cn

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventoryID | varchar | 8000 | 1 |  |  |  |
| InventoryLineNo | int | 4 | 1 |  |  |  |
| StoreID | varchar | 8000 | 1 |  |  |  |
| InventoryDate | date | 3 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| Cost | decimal | 5 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| Franchisee | varchar | 8000 | 1 |  |  |  |
