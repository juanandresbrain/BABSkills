# dbo.CLNDR_PRD

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_PRD_ID | T_ID | 16 | 0 |  |  |  |
| CLNDR_PRD_NUM | T_INTEGER | 2 | 0 |  |  |  |
| CLNDR_PRD_NAME | nvarchar | 510 | 0 |  |  |  |
| STRT_DATE_TIME | T_DATETIME | 8 | 0 |  |  |  |
| END_DATE_TIME | T_DATETIME | 8 | 0 |  |  |  |
| CLNDR_ID | T_ID | 16 | 0 |  |  |  |
| CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| ROOT_TMPLT_ID | T_ID | 16 | 1 |  |  |  |
