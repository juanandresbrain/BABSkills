# dbo.FNDTN_SCRTY_ERR_LOG

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| APP_ID | smallint | 2 | 0 |  |  |  |
| CMPNY_ID | smallint | 2 | 0 |  |  |  |
| USER_ID | numeric | 9 | 0 |  |  |  |
| USER_ID_TYPE | tinyint | 1 | 0 |  |  |  |
| INSTNC | tinyint | 1 | 0 |  |  |  |
| TIME_STMP | datetime | 8 | 0 |  |  |  |
| ERR_NUM | int | 4 | 0 |  |  |  |
| SVRTY_LVL | smallint | 2 | 0 |  |  |  |
| ERR_SRC | varchar | 255 | 0 |  |  |  |
| ERR_MSG | text | 16 | 0 |  |  |  |
