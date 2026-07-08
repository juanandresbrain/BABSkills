# dbo.ORG_CHN_HRCHY

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| HRCHY_DESC | nvarchar | 510 | 0 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| DFLT_GRP_ID | T_ID | 16 | 1 |  |  |  |
| SCRTY_USER_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| MTLY_EXCLSV | T_BOOLEAN | 5 | 0 |  |  |  |
| MNDTRY_ASGNMNT | T_BOOLEAN | 5 | 0 |  |  |  |
