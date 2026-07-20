# dbo.crmtransactionfact

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| CRMTransactionID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionPostedDate | date | 3 | 1 |  |  |  |
| CRMTransactionType | varchar | 8000 | 1 |  |  |  |
| POSTransactionNumber | varchar | 8000 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| PointsEarned | bit | 1 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedDate | datetime2 | 8 | 1 |  |  |  |
| InsertedBy | varchar | 8000 | 1 |  |  |  |
| UpdatedBy | varchar | 8000 | 1 |  |  |  |
| MNTH_01_12_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_01_24_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_01_36_VST_CNT | int | 4 | 1 |  |  |  |
| daysSinceLastVisit | int | 4 | 1 |  |  |  |
| numTransToday | int | 4 | 1 |  |  |  |
| lifetimeVisitNumber | int | 4 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| LifetimeTransactionSequence | int | 4 | 1 |  |  |  |
| LifetimeVisitSequence | int | 4 | 1 |  |  |  |
| POS | varchar | 8000 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
