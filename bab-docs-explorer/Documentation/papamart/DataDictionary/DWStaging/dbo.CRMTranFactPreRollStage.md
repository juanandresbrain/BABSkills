# dbo.CRMTranFactPreRollStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| LifetimeTransactionCount | int | 4 | 1 |  |  |  |
| LifetimeRecencyCount | int | 4 | 1 |  |  |  |
| LifetimeSalesTotal | numeric | 17 | 1 |  |  |  |
| FirstTransactionDate | date | 3 | 1 |  |  |  |
| LastTransDate | date | 3 | 1 |  |  |  |
| FirstStoreConcept | nvarchar | 12 | 1 |  |  |  |
| LastTransStore | varchar | 4 | 1 |  |  |  |
