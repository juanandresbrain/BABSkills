# dbo.tmpUnshippedItemsWithLWunitsSales

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PickupStore | varchar | 100 | 1 |  |  |  |
| ItemNumber | varchar | 50 | 0 |  |  |  |
| ItemQty | int | 4 | 0 |  |  |  |
| DistroDay | nvarchar | 100 | 1 |  |  |  |
| DCsource | nvarchar | 100 | 1 |  |  |  |
| StyleDescription | varchar | 100 | 1 |  |  |  |
| consumer group | varchar | 50 | 1 |  |  |  |
| department | varchar | 50 | 1 |  |  |  |
| class | varchar | 50 | 1 |  |  |  |
| deptcode | varchar | 50 | 1 |  |  |  |
| subclasscode | varchar | 50 | 1 |  |  |  |
| StyleCode | varchar | 50 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| Allocated | int | 4 | 1 |  |  |  |
| InTransit | int | 4 | 1 |  |  |  |
| DateKey | date | 3 | 0 |  |  |  |
| ProductKey | int | 4 | 0 |  |  |  |
| StoreKey | int | 4 | 0 |  |  |  |
| PreviousFiscalWeek | nvarchar | 100 | 1 |  |  |  |
| LWunitsSold | int | 4 | 1 |  |  |  |
| keyStory | nvarchar | 100 | 1 |  |  |  |
| mstat | nvarchar | 100 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 0 |  |  |  |
| StoreInventoryBuffer | int | 4 | 0 |  |  |  |
| totalQuantity | int | 4 | 0 |  |  |  |
| StoreName | nvarchar | 510 | 1 |  |  |  |
| StoreConcept | nvarchar | 100 | 1 |  |  |  |
| StoreInTransit | int | 4 | 1 |  |  |  |
| storeAllocated | int | 4 | 1 |  |  |  |
