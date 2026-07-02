# dbo.DATA_VERSION

**Database:** REPL_MAN  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VERSION_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| DATABASE_NAME | varchar | 30 | 0 |  |  |  |
| DATA_VERSION_NO | int | 4 | 0 |  |  |  |
| CREATION_DATETIME | datetime | 8 | 1 |  |  |  |
| STATUS | char | 4 | 1 |  |  |  |
| LAST_LEASE_DATETIME | datetime | 8 | 1 |  |  |  |

