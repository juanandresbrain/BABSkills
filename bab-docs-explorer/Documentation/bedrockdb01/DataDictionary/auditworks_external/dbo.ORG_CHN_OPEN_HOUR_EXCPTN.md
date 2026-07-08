# dbo.ORG_CHN_OPEN_HOUR_EXCPTN

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| EXCPTN_DATE | T_DATE | 8 | 0 |  |  |  |
| START_TIME | T_TIME | 8 | 0 |  |  |  |
| END_TIME | T_TIME | 8 | 0 |  |  |  |
| CLSD | T_BOOLEAN | 5 | 0 |  |  |  |
| RSN_ID | T_ID | 16 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
