# dbo.integrationstaging_web_ukwebstoreproductbalance

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventoryDate | date | 3 | 1 |  |  |  |
| StyleCode | varchar | 8000 | 1 |  |  |  |
| ARRQuantity | int | 4 | 1 |  |  |  |
| AVLQuantity | int | 4 | 1 |  |  |  |
| TRAQuantity | int | 4 | 1 |  |  |  |
| ORDQuantity | int | 4 | 1 |  |  |  |
| PCKQuantity | int | 4 | 1 |  |  |  |
| AWPQuantity | int | 4 | 1 |  |  |  |
| ALLQuantity | int | 4 | 1 |  |  |  |
| ADVQuantity | int | 4 | 1 |  |  |  |
| HLDQuantity | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedByFileName | varchar | 8000 | 1 |  |  |  |
