# dbo.ORG_CHN_FCLTY_BIN_LOC

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BIN_LOC_ID | T_ID | 16 | 0 |  |  |  |
| LOC_ID | T_ID | 16 | 0 |  |  |  |
| BIN_LOC_CODE | nvarchar | 40 | 0 |  |  |  |
| BIN_LOC_DESC | nvarchar | 510 | 0 |  |  |  |
| STCK | T_INTEGER | 2 | 1 |  |  |  |
| DPTH | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| WDTH | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| HGHT | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| ACTV | nvarchar | 60 | 0 |  |  |  |
| TRNVR | T_INTEGER | 2 | 0 |  |  |  |
| TMPRY | T_BOOLEAN | 5 | 0 |  |  |  |
| PICK_FRNT | T_BOOLEAN | 5 | 0 |  |  |  |
| FTPRNT | T_INTEGER | 2 | 0 |  |  |  |
| MSR_CODE | nchar | 8 | 1 |  |  |  |
