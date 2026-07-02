# dbo.FDS_CONNECTION

**Database:** FDS  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CONNECTION_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| START_TIME | datetime | 8 | 1 |  |  |  |
| FINISH_TIME | datetime | 8 | 1 |  |  |  |
| REMOTE_ID | char | 37 | 1 |  |  |  |
| FILE_ID | char | 255 | 1 |  |  |  |
| CONN_ACTION | char | 25 | 1 |  |  |  |
| PORT | int | 4 | 1 |  |  |  |
| STATUS | char | 25 | 1 |  |  |  |
| RETURNCODE | int | 4 | 1 |  |  |  |

