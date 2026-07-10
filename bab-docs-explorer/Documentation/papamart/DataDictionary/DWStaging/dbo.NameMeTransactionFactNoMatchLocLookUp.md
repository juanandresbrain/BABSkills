# dbo.NameMeTransactionFactNoMatchLocLookUp

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Pull_StoreID | int | 4 | 1 |  |  |  |
| NameMeTransactionNumber | int | 4 | 1 |  |  |  |
| AnimalBarcode | varchar | 25 | 1 |  |  |  |
| AnimalName | varchar | 25 | 1 |  |  |  |
| AnimalBirthDate | date | 3 | 1 |  |  |  |
| TransactionStartDate | datetime | 8 | 1 |  |  |  |
| TransactionEndDate | datetime | 8 | 1 |  |  |  |
| Gift | int | 4 | 1 |  |  |  |
| FirstVisit | bit | 1 | 1 |  |  |  |
| RecipBirthDate | datetime | 8 | 1 |  |  |  |
| TransactionSource | varchar | 6 | 1 |  |  |  |
| Gender | varchar | 1 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| SKULookUp | varchar | 5 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
