# dbo.az_namemetransactionfact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | bigint | 8 | 1 |  |  |  |
| NameMeTransactionNumber | varchar | 8000 | 1 |  |  |  |
| AnimalBarCode | varchar | 8000 | 1 |  |  |  |
| AnimalName | varchar | 8000 | 1 |  |  |  |
| AnimalBirthDate | date | 3 | 1 |  |  |  |
| TransactionStartDate | datetime2 | 8 | 1 |  |  |  |
| TransactionEndDate | datetime2 | 8 | 1 |  |  |  |
| TransactionDuration | int | 4 | 1 |  |  |  |
| Gift | int | 4 | 1 |  |  |  |
| FirstVisit | int | 4 | 1 |  |  |  |
| TransactionSource | varchar | 8000 | 1 |  |  |  |
| Age | decimal | 5 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedDate | datetime2 | 8 | 1 |  |  |  |
| InsertedBy | varchar | 8000 | 1 |  |  |  |
| UpdatedBy | varchar | 8000 | 1 |  |  |  |
| POSTransactionID | varchar | 4080 | 1 |  |  |  |
