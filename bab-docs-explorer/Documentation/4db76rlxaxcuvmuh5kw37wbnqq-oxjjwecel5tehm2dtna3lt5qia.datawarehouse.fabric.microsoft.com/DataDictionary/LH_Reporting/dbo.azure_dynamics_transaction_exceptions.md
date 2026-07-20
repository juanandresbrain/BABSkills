# dbo.azure_dynamics_transaction_exceptions

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
| ReasonForException | varchar | 8000 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| LineObjectDescription | varchar | 8000 | 1 |  |  |  |
| Transaction_Id | varchar | 8000 | 1 |  |  |  |
| VarianceValue | decimal | 9 | 1 |  |  |  |
| TransactionTotalAmount | decimal | 17 | 1 |  |  |  |
