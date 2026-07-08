# dbo.PRTY_CNTCT

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRTY_CNTCT_ID | T_ID | 16 | 0 |  |  |  |
| PRTY_ID | T_ID | 16 | 0 |  |  |  |
| CNTCT_TYPE_CODE | nvarchar | 8 | 0 |  |  |  |
| CNTCT_DTLS | nvarchar | 510 | 1 |  |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| CNTCT | nvarchar | 510 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
| PRMRY | T_BOOLEAN | 5 | 1 |  |  |  |
