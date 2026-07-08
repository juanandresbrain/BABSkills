# dbo.ORG_CHN_HRCHY_LVL

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_LVL_DESC | nvarchar | 510 | 0 |  |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| AFLTN_PRMTD | T_BOOLEAN | 5 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_ID | T_ID | 16 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| GRP_CODE_MSK | nvarchar | 40 | 1 |  |  |  |
