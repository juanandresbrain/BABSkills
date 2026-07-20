# dbo.namemetransactionfactstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| NameMeTransactionNumber | varchar | 8000 | 1 |  |  |  |
| AnimalBarCode | varchar | 8000 | 1 |  |  |  |
| AnimalName | varchar | 8000 | 1 |  |  |  |
| AnimalBirthDate | date | 3 | 1 |  |  |  |
| TransactionStartDate | datetime2 | 8 | 1 |  |  |  |
| TransactionEndDate | datetime2 | 8 | 1 |  |  |  |
| TransactionDuration | int | 4 | 1 |  |  |  |
| Gift | bit | 1 | 1 |  |  |  |
| FirstVisit | bit | 1 | 1 |  |  |  |
| TransactionSource | varchar | 8000 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| RecipBirthDate | datetime2 | 8 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| POSTransactionID | int | 4 | 1 |  |  |  |
