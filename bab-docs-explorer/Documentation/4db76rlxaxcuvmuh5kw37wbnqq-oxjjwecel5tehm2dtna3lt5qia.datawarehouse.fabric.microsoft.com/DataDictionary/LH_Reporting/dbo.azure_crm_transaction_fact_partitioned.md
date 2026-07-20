# dbo.azure_crm_transaction_fact_partitioned

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POSTransactionID | int | 4 | 1 |  |  |  |
| CRMTransactionID | int | 4 | 1 |  |  |  |
| StoreKey | varchar | 8000 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| CRMTransactionType | varchar | 8000 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| StoreID | varchar | 8000 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| LifetimeTransactionNumber | int | 4 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| inMonth1 | int | 4 | 1 |  |  |  |
| inMonth3 | int | 4 | 1 |  |  |  |
| inMonth6 | int | 4 | 1 |  |  |  |
| inMonth12 | int | 4 | 1 |  |  |  |
| inMonth18 | int | 4 | 1 |  |  |  |
| inMonth24 | int | 4 | 1 |  |  |  |
| inMonth36 | int | 4 | 1 |  |  |  |
