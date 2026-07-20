# dbo.az_crmtransactionfact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | varchar | 4080 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionPostedDate | date | 3 | 1 |  |  |  |
| CRMTransactionType | varchar | 8000 | 1 |  |  |  |
| POSTransactionNumber | varchar | 8000 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedDate | datetime2 | 8 | 1 |  |  |  |
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
| matchedByEmail | int | 4 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
