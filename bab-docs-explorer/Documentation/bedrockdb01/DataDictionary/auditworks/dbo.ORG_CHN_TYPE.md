# dbo.ORG_CHN_TYPE

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_TYPE_CODE | nvarchar | 8 | 0 |  |  |  |
| ORG_CHN_TYPE_DESC | nvarchar | 510 | 0 |  |  |  |
| ORG_CHN_TYPE_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| SYS_CODE | nvarchar | 8 | 0 |  |  |  |
| LOC_CTGRY_CODE | nvarchar | 8 | 1 |  |  |  |
| SYSTM_DFND | T_BOOLEAN | 5 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 1 |  |  |  |
