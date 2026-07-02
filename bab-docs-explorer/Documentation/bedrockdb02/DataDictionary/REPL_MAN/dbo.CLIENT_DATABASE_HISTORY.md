# dbo.CLIENT_DATABASE_HISTORY

**Database:** REPL_MAN  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HISTORY_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| CLIENT_ID | uniqueidentifier | 16 | 0 |  |  |  |
| DATABASE_NAME | varchar | 30 | 0 |  |  |  |
| DATA_VERSION_NO | int | 4 | 0 |  |  |  |
| UPDATE_DT | datetime | 8 | 1 |  |  |  |
| UPDATE_STATUS | char | 4 | 1 |  |  |  |
| UPDATE_TYPE | char | 4 | 1 |  |  |  |

