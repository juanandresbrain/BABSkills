# dbo.EMPLY_WORK_PRFL

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRFL_ID | binary | 16 | 0 |  |  |  |
| PRFL_DESC | varchar | 255 | 0 |  |  |  |
| PRFL_SHRT_DESC | varchar | 50 | 0 |  |  |  |
| MIN_TIME_PER_WEEK | decimal | 9 | 1 |  |  |  |
| MAX_TIME_PER_WEEK | decimal | 9 | 1 |  |  |  |
| MIN_TIME_PER_SHFT | decimal | 9 | 1 |  |  |  |
| MAX_TIME_PER_SHFT | decimal | 9 | 1 |  |  |  |
| MAX_SHFTS_PER_DAY | decimal | 9 | 1 |  |  |  |
| MAX_TIME_PER_DAY | decimal | 9 | 1 |  |  |  |
| OVRTM_FCTR_FRST_THRSHLD | numeric | 9 | 1 |  |  |  |
| OVRTM_FCTR_SCND_THRSHLD | numeric | 9 | 1 |  |  |  |
| DAY_OVRTM_FRST_THRSHLD | decimal | 9 | 1 |  |  |  |
| DAY_OVRTM_SCND_THRSHLD | decimal | 9 | 1 |  |  |  |
| WEEK_OVRTM_FRST_THRSHLD | decimal | 9 | 1 |  |  |  |
| WEEK_OVRTM_SCND_THRSHLD | decimal | 9 | 1 |  |  |  |
