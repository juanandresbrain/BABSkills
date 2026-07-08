# dbo.ORG_CHN_HRCHY_LVL_GRP

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_LVL_GRP_IDNTY | T_INTEGER | 2 | 0 | YES |  |  |
| HRCHY_LVL_GRP_DESC | nvarchar | 510 | 0 |  |  |  |
| HRCHY_LVL_GRP_CODE | nvarchar | 40 | 1 |  |  |  |
| GRP_MBR_CHNG | T_DATE | 8 | 1 |  |  |  |
| HRCHY_LVL_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_GRP_ID | T_ID | 16 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| ALTNT_GRP_CODE | nvarchar | 100 | 1 |  |  |  |
| HRCHY_LVL_GRP_SHRT_DESC | nvarchar | 100 | 1 |  |  |  |
