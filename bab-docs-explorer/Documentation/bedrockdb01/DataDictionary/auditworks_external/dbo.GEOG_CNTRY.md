# dbo.GEOG_CNTRY

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CNTRY_CODE_ISO3 | nchar | 6 | 0 |  |  |  |
| CNTRY_CODE_ISO2 | nchar | 4 | 1 |  |  |  |
| CNTRY_DESC | nvarchar | 510 | 0 |  |  |  |
| CNTRY_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| TLPHNY_CNTRY_CODE | nchar | 6 | 1 |  |  |  |
| DFLT_CRNCY_CODE | nchar | 6 | 0 |  |  |  |
| TRNSTNL_CRNCY_CODE | nchar | 6 | 1 |  |  |  |
| ITIN_VLDTN_FRMT | nvarchar | 2000 | 1 |  |  |  |
| ITIN_DSPLY_FRMT | nvarchar | 2000 | 1 |  |  |  |
| OPRTNG_CNTRY | T_BOOLEAN | 5 | 1 |  |  |  |
