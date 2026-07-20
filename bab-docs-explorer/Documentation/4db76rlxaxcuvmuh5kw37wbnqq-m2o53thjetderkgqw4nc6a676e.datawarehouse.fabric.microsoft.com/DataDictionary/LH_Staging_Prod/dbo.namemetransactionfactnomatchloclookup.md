# dbo.namemetransactionfactnomatchloclookup

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Pull_StoreID | int | 4 | 1 |  |  |  |
| NameMeTransactionNumber | int | 4 | 1 |  |  |  |
| AnimalBarcode | varchar | 8000 | 1 |  |  |  |
| AnimalName | varchar | 8000 | 1 |  |  |  |
| AnimalBirthDate | date | 3 | 1 |  |  |  |
| TransactionStartDate | datetime2 | 8 | 1 |  |  |  |
| TransactionEndDate | datetime2 | 8 | 1 |  |  |  |
| Gift | int | 4 | 1 |  |  |  |
| FirstVisit | bit | 1 | 1 |  |  |  |
| RecipBirthDate | datetime2 | 8 | 1 |  |  |  |
| TransactionSource | varchar | 8000 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| LocationCode | varchar | 8000 | 1 |  |  |  |
| SKULookUp | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
