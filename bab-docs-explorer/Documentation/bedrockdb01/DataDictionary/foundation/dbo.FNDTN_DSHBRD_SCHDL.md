# dbo.FNDTN_DSHBRD_SCHDL

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SCHDL_ID | binary | 16 | 0 |  |  |  |
| TRGT_ID | binary | 16 | 0 |  |  |  |
| TRGT_TYPE | tinyint | 1 | 0 |  |  |  |
| INTRVL_TYPE | tinyint | 1 | 0 |  |  |  |
| NUM_OF_INTRVL_PRDS | int | 4 | 0 |  |  |  |
| START_DATE_TIME | smalldatetime | 4 | 0 |  |  |  |
| END_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| FRQNCY | int | 4 | 0 |  |  |  |
| IS_SCHDLD_ON_SUN | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_MON | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_TUES | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_WED | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_THURS | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_FRI | bit | 1 | 0 |  |  |  |
| IS_SCHDLD_ON_SAT | bit | 1 | 0 |  |  |  |
| ACTV | bit | 1 | 0 |  |  |  |
| LAST_SCHDL_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| NEXT_EXEC_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| EXEC_STS | tinyint | 1 | 1 |  |  |  |
| LCID | smallint | 2 | 1 |  |  |  |
| USER_ID | int | 4 | 1 |  |  |  |
