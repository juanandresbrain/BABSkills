# dbo.ORG_CHN_WRKSTN_CNFG_A

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WRKSTN_ID | T_ID | 16 | 0 |  |  |  |
| WRKSTN_CNFG_CODE | nchar | 8 | 0 |  |  |  |
| EFCTV_DATE | T_DATE | 8 | 0 |  |  |  |
| EXPRTN_DATE | T_DATE | 8 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
