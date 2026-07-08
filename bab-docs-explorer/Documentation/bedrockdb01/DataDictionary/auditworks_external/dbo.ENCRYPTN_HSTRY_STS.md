# dbo.ENCRYPTN_HSTRY_STS

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TBL_NAME | nvarchar | 60 | 0 |  |  |  |
| CLMN_NAME | nvarchar | 60 | 0 |  |  |  |
| KEY_CLMN | nvarchar | 60 | 1 |  |  |  |
| LAST_KEY_ID | numeric | 17 | 1 |  |  |  |
| COMPLETED | smallint | 2 | 0 |  |  |  |
