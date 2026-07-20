# dbo.tmpcrmtrans

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| TransacionMonth | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | varchar | 8000 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
