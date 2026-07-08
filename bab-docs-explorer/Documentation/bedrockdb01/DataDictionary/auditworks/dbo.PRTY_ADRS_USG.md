# dbo.PRTY_ADRS_USG

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRTY_ID | T_ID | 16 | 0 |  |  |  |
| PRTY_ADRS_SEQ | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| PRTY_ADRS_DESC | nvarchar | 510 | 0 |  |  |  |
| ADRS_FNCTN_CODE | nvarchar | 8 | 0 |  |  |  |
| CNTCT_PREF_ID | T_ID | 16 | 1 |  |  |  |
