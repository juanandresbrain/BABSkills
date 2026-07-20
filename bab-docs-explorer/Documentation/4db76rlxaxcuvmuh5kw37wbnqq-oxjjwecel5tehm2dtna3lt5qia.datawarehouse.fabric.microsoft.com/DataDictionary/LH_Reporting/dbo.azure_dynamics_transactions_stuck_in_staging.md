# dbo.azure_dynamics_transactions_stuck_in_staging

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| TransactionNumber | int | 4 | 1 |  |  |  |
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| TransTotal | decimal | 13 | 1 |  |  |  |
