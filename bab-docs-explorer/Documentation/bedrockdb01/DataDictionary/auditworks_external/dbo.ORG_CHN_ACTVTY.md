# dbo.ORG_CHN_ACTVTY

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ACTVTY_CODE | nchar | 8 | 0 |  |  |  |
| ACTVTY_DESC | nvarchar | 510 | 0 |  |  |  |
| ACTVTY_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| SCRTY_CNFG | T_BOOLEAN | 5 | 0 |  |  |  |
| ASGN_SLS_GOAL | T_BOOLEAN | 5 | 0 |  |  |  |
| APRVL_ACTVTY_CODE | nchar | 8 | 1 |  |  |  |
| SYS_CODE | nvarchar | 8 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
