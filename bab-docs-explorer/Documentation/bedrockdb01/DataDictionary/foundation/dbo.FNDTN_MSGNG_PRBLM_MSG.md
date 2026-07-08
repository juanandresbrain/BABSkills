# dbo.FNDTN_MSGNG_PRBLM_MSG

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MSG_ID | T_ID | 16 | 0 |  |  |  |
| MSGNG_IDNTFR | varchar | 24 | 0 |  |  |  |
| QUEUE_CNFGRTN_ID | int | 4 | 0 |  |  |  |
| MSG | ntext | 16 | 0 |  |  |  |
| ERR_MSG | nvarchar | 2000 | 0 |  |  |  |
| ERR_STCK_TRC | ntext | 16 | 0 |  |  |  |
| ENTRY_DATE_TIME | datetime | 8 | 0 |  |  |  |
| RDY_TO_RSBMT | bit | 1 | 0 |  |  |  |
