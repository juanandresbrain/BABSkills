# dbo.ORG_CHN_LOC_HRCHY_LVL_GRP

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | smallint | 2 | 0 | YES |  |  |
| HRCHY_LVL_GRP_DESC | varchar | 255 | 0 |  |  |  |
| GRP_MBR_CHNG | datetime | 8 | 1 |  |  |  |
| HRCHY_LVL_ID | binary | 16 | 0 |  |  |  |
| HRCHY_ID | binary | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_GRP_ID | smallint | 2 | 1 |  |  |  |
