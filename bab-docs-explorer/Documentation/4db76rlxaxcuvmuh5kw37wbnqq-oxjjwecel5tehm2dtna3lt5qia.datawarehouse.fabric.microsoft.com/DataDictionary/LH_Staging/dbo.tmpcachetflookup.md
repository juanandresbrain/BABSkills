# dbo.tmpcachetflookup

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| POSTransactionNumber | int | 4 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | decimal | 17 | 1 |  |  |  |
