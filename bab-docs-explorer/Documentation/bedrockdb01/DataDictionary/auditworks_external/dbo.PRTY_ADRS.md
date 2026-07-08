# dbo.PRTY_ADRS

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRTY_ADRS_ID | T_ID | 16 | 0 |  |  |  |
| PRTY_ID | T_ID | 16 | 0 |  |  |  |
| ADRS_ID | T_ID | 16 | 0 |  |  |  |
| PRTY_ADRS_SEQ | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| EFCTV_STRT_DATE | T_DATE | 8 | 0 |  |  |  |
| EFCTV_END_DATE | T_DATE | 8 | 1 |  |  |  |
| ADRS_EXPRTN_RSN_ID | T_ID | 16 | 1 |  |  |  |
| PRTY_ADRS_DESC | nvarchar | 510 | 0 |  |  |  |
| ADRS_FNCTN_CODE | nvarchar | 8 | 0 |  |  |  |
