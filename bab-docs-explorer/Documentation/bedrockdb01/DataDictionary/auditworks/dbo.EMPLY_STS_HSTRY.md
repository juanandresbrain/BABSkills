# dbo.EMPLY_STS_HSTRY

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| EFCTV_DATE | T_DATE | 8 | 0 |  |  |  |
| EMPLY_STS_CODE | nvarchar | 8 | 0 |  |  |  |
| EXPRTN_DATE | T_DATE | 8 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
