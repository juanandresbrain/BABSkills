# dbo.CRMTransactionFact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| CRMTransactionID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionPostedDate | date | 3 | 1 |  |  |  |
| CRMTransactionType | varchar | 6 | 1 |  |  |  |
| POSTransactionNumber | varchar | 20 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 0 |  |  |  |
| PointsEarned | bit | 1 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| InsertedDate | datetime | 8 | 1 |  |  |  |
| UpdatedDate | datetime | 8 | 1 |  |  |  |
| InsertedBy | varchar | 50 | 1 |  |  |  |
| UpdatedBy | varchar | 50 | 1 |  |  |  |
| MNTH_01_12_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_01_24_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_01_36_VST_CNT | int | 4 | 1 |  |  |  |
| daysSinceLastVisit | int | 4 | 1 |  |  |  |
| numTransToday | int | 4 | 1 |  |  |  |
| lifetimeVisitNumber | int | 4 | 1 |  |  |  |
| GaapSales | numeric | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| LifetimeTransactionSequence | int | 4 | 1 |  |  |  |
| LifetimeVisitSequence | int | 4 | 1 |  |  |  |
| POS | varchar | 10 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
