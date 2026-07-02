# dbo.FDS_FILE_LOG

**Database:** FDS  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FILE_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| FILE_NAME | char | 255 | 1 |  |  |  |
| FILE_TIME | datetime | 8 | 1 |  |  |  |
| PICKUP_LOC | char | 255 | 1 |  |  |  |
| FILE_ACTION | char | 25 | 1 |  |  |  |
| STATUS | char | 25 | 1 |  |  |  |
| FILE_SIZE | int | 4 | 1 |  |  |  |
| CRC | int | 4 | 1 |  |  |  |

