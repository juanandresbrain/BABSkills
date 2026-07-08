# dbo.EMPLY_CMSN_PLAN

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CMSN_PLAN_CODE | char | 4 | 0 |  |  |  |
| CMSN_PLAN_DESC | varchar | 255 | 0 |  |  |  |
| CMSN_PLAN_SHRT_DESC | varchar | 50 | 0 |  |  |  |
| CMSN_PRCNT | numeric | 9 | 0 |  |  |  |
| GRP_ID | binary | 16 | 1 |  |  |  |
| THRSHLD_LWR_LMT | numeric | 9 | 1 |  |  |  |
| THRSHLD_UPR_LMT | numeric | 9 | 1 |  |  |  |
