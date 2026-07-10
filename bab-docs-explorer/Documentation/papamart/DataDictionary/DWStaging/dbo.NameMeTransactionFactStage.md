# dbo.NameMeTransactionFactStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| NameMeTransactionNumber | varchar | 20 | 1 |  |  |  |
| AnimalBarCode | varchar | 25 | 1 |  |  |  |
| AnimalName | varchar | 50 | 1 |  |  |  |
| AnimalBirthDate | date | 3 | 1 |  |  |  |
| TransactionStartDate | datetime | 8 | 1 |  |  |  |
| TransactionEndDate | datetime | 8 | 1 |  |  |  |
| TransactionDuration | int | 4 | 1 |  |  |  |
| Gift | bit | 1 | 1 |  |  |  |
| FirstVisit | bit | 1 | 1 |  |  |  |
| TransactionSource | varchar | 6 | 1 |  |  |  |
| Gender | char | 1 | 1 |  |  |  |
| RecipBirthDate | datetime | 8 | 1 |  |  |  |
| InsertedDate | datetime | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| POSTransactionID | int | 4 | 1 |  |  |  |
