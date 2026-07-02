# dbo.FNDTN_BLNCNG_CHCK_EXEC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BLCNG_CHCK_EXEC_ID | binary | 16 | 0 | YES |  |  |
| JOB_EXEC_ID | bigint | 8 | 0 |  | YES |  |
| BLNCNG_CHCK_ID | binary | 16 | 0 |  | YES |  |
| CHCK_NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| START_DATE_TIME | datetime | 8 | 1 |  |  |  |
| END_DATE_TIME | datetime | 8 | 1 |  |  |  |
| BLNCNG_STATUS | tinyint | 1 | 0 |  | YES |  |
| FIRST_RCRD_COUNT | int | 4 | 1 |  |  |  |
| SCND_RCRD_COUNT | int | 4 | 1 |  |  |  |
| FRST_NAME | nvarchar | 10 | 0 |  |  |  |
| SCND_NAME | nvarchar | 10 | 0 |  |  |  |
| PRNT_CHCK_EXEC_ID | binary | 16 | 1 |  |  |  |
| PRNT_SQNC_NO | int | 4 | 1 |  |  |  |
| TLRNC | varchar | 100 | 1 |  |  |  |

