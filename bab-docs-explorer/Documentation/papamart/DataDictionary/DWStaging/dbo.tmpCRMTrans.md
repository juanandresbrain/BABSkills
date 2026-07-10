# dbo.tmpCRMTrans

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| TransacionMonth | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | nvarchar | 12 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| StoreNumber | varchar | 10 | 1 |  |  |  |
| Country | varchar | 50 | 1 |  |  |  |
| GaapSales | numeric | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
