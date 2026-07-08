# dbo.EMPLY_HRCHY_LVL

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_ID | binary | 16 | 0 |  |  |  |
| HRCHY_LVL_DESC | varchar | 255 | 0 |  |  |  |
| SEQ_NUM | numeric | 9 | 0 |  |  |  |
| AFLTN_PRMTD | numeric | 5 | 0 |  |  |  |
| HRCHY_ID | binary | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_ID | binary | 16 | 1 |  |  |  |
