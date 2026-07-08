# dbo.EMPLY_CMSN_PLAN

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CMSN_PLAN_CODE | nchar | 8 | 0 |  |  |  |
| CMSN_PLAN_DESC | nvarchar | 510 | 0 |  |  |  |
| CMSN_PLAN_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| CMSN_PRCNT | T_CONVERSION_FACTOR | 9 | 0 |  |  |  |
| GRP_ID | T_ID | 16 | 1 |  |  |  |
| THRSHLD_LWR_LMT | T_MONEY | 9 | 1 |  |  |  |
| THRSHLD_UPR_LMT | T_MONEY | 9 | 1 |  |  |  |
