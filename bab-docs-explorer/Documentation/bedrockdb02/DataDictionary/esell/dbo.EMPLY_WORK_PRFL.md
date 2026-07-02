# dbo.EMPLY_WORK_PRFL

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRFL_ID | T_ID | 16 | 0 | YES |  |  |
| PRFL_DESC | nvarchar | 510 | 0 |  |  |  |
| PRFL_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| MIN_TIME_PER_WEEK | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| MAX_TIME_PER_WEEK | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| MIN_TIME_PER_SHFT | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| MAX_TIME_PER_SHFT | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| MAX_SHFTS_PER_DAY | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| MAX_TIME_PER_DAY | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| OVRTM_FCTR_FRST_THRSHLD | T_CONVERSION_FACTOR | 9 | 1 |  |  |  |
| OVRTM_FCTR_SCND_THRSHLD | T_CONVERSION_FACTOR | 9 | 1 |  |  |  |
| DAY_OVRTM_FRST_THRSHLD | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| DAY_OVRTM_SCND_THRSHLD | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| WEEK_OVRTM_FRST_THRSHLD | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |
| WEEK_OVRTM_SCND_THRSHLD | T_QUANTITY_INTEGER | 9 | 1 |  |  |  |

