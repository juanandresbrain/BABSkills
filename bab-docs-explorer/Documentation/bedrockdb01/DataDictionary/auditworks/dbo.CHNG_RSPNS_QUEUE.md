# dbo.CHNG_RSPNS_QUEUE

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTY_TYPE | nvarchar | 100 | 1 |  |  |  |
| ENTY_ID | T_ID | 16 | 1 |  |  |  |
| ENTY_NUM | T_LONG_INTEGER | 4 | 1 |  |  |  |
| ENTY_CODE | nchar | 12 | 1 |  |  |  |
| STS | nchar | 8 | 1 |  |  |  |
| LCKD | T_BOOLEAN | 5 | 1 |  |  |  |
| CHNG_DATE_TIME | T_DATETIME | 8 | 1 |  |  |  |
