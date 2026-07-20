# dbo.namemetransactionfact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NameMeTransactionKey | int | 4 | 1 |  |  |  |
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
| Age | decimal | 5 | 1 |  |  |  |
| TransactionSource | varchar | 8000 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedDate | datetime2 | 8 | 1 |  |  |  |
| InsertedBy | varchar | 8000 | 1 |  |  |  |
| UpdatedBy | varchar | 8000 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| POSTransactionID | int | 4 | 1 |  |  |  |
