# POS.JumpMindAPI_Logging

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| storeNo | varchar | 5 | 1 |  |  |  |
| registerNo | varchar | 5 | 1 |  |  |  |
| transactionNo | varchar | 10 | 1 |  |  |  |
| jsonDateTime | datetime | 8 | 1 |  |  |  |
| apiDateTime | datetime | 8 | 1 |  |  |  |
| rawFileName | varchar | 30 | 1 |  |  |  |
| rawFileContents | varchar | -1 | 1 |  |  |  |
| transactionType | varchar | 20 | 1 |  |  |  |
| processed | tinyint | 1 | 1 |  |  |  |
| processedTime | datetime | 8 | 1 |  |  |  |
| isControlTransaction | tinyint | 1 | 1 |  |  |  |
| controlTransactionProcessed | tinyint | 1 | 1 |  |  |  |
| controlTransactionNo | int | 4 | 1 |  |  |  |
| xpollFolder | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.spDeleteJumpmindJsonRecords](../../StoredProcedures/ApplicationResources/dbo.spDeleteJumpmindJsonRecords.md)

