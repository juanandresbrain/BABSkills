# dbo.CRNCY

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRNCY_ID | numeric | 9 | 0 |  |  |  |
| CRNCY_CODE | nchar | 6 | 0 |  |  |  |
| CRNCY_DESC | nvarchar | 510 | 0 |  |  |  |
| CRNCY_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| ACTV | bit | 1 | 0 |  |  |  |
| RSRC_ID | numeric | 9 | 1 |  |  |  |
| DSPL_MASK | nvarchar | 40 | 1 |  |  |  |
| CRNCY_SMBL | nvarchar | 50 | 1 |  |  |  |
