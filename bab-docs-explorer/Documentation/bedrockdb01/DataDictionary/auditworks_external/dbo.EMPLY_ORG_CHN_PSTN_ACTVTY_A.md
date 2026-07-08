# dbo.EMPLY_ORG_CHN_PSTN_ACTVTY_A

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| PSTN_CODE | nchar | 8 | 0 |  |  |  |
| ACTVTY_CODE | nchar | 8 | 0 |  |  |  |
| GRP_ID | T_ID | 16 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
