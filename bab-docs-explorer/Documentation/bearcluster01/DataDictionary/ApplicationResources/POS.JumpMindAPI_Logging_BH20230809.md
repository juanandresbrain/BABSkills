# POS.JumpMindAPI_Logging_BH20230809

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
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

