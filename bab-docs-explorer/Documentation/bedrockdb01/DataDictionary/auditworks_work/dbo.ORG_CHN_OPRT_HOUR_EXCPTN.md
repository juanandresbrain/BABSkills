# dbo.ORG_CHN_OPRT_HOUR_EXCPTN

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | int | 4 | 0 |  |  |  |
| EXCPTN_DATE | datetime | 8 | 0 |  |  |  |
| START_TIME | datetime | 8 | 0 |  |  |  |
| END_TIME | datetime | 8 | 0 |  |  |  |
| CLSD | numeric | 5 | 0 |  |  |  |
| RSN_ID | binary | 16 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
