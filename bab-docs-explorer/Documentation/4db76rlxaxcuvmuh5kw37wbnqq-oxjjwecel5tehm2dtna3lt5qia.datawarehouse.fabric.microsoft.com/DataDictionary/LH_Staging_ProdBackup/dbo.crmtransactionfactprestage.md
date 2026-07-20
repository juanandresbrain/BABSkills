# dbo.crmtransactionfactprestage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| CRMTransactionID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionPostedDate | date | 3 | 1 |  |  |  |
| CRMTransactionType | varchar | 8000 | 1 |  |  |  |
| POSTransactionNumber | varchar | 8000 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| PointsEarned | bit | 1 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| TransactionIDTF | varchar | 8000 | 1 |  |  |  |
