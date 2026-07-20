# dbo.azure_unshipped_skus

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PickupStore | varchar | 8000 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| StoreConcept | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| ItemQty | int | 4 | 1 |  |  |  |
| DistroDay | varchar | 8000 | 1 |  |  |  |
| DCsource | varchar | 8000 | 1 |  |  |  |
| StyleDescription | varchar | 8000 | 1 |  |  |  |
| consumer_group | varchar | 8000 | 1 |  |  |  |
| department | varchar | 8000 | 1 |  |  |  |
| class | varchar | 8000 | 1 |  |  |  |
| deptcode | varchar | 8000 | 1 |  |  |  |
| subclasscode | varchar | 8000 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| Allocated | int | 4 | 1 |  |  |  |
| InTransit | int | 4 | 1 |  |  |  |
| DateKey | date | 3 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| PreviousFiscalWeek | varchar | 8000 | 1 |  |  |  |
| LWunitsSold | int | 4 | 1 |  |  |  |
| keyStory | varchar | 8000 | 1 |  |  |  |
| mstat | varchar | 8000 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 1 |  |  |  |
| StoreInventoryBuffer | int | 4 | 1 |  |  |  |
| totalQuantity | int | 4 | 1 |  |  |  |
| StoreInTransit | int | 4 | 1 |  |  |  |
| storeAllocated | int | 4 | 1 |  |  |  |
