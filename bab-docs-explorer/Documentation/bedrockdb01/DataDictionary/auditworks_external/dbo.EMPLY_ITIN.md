# dbo.EMPLY_ITIN

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| CNTRY_CODE_ISO3 | nchar | 6 | 0 |  |  |  |
| ITIN | nvarchar | 50 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
