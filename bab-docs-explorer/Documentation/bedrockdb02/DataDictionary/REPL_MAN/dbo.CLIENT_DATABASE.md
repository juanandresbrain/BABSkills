# dbo.CLIENT_DATABASE

**Database:** REPL_MAN  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLIENT_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| DATABASE_NAME | varchar | 30 | 0 | YES |  |  |
| CLIENT_STATE | char | 4 | 1 |  |  |  |
| CLIENT_STATE_DT | datetime | 8 | 1 |  |  |  |
| CUR_DATA_VERSION_NO | int | 4 | 1 |  |  |  |
| CUR_DATA_VERSION_DT | datetime | 8 | 1 |  |  |  |
| UPDATE_TYPE | char | 4 | 1 |  |  |  |

