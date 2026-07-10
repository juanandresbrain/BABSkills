# dbo.VLDTN_TREND_STAT_DIM_new

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_TREND_STAT_ID | int | 4 | 0 | YES |  |  |
| VLDTN_TREND_REPORT_ID | int | 4 | 0 |  |  |  |
| NM | varchar | 50 | 0 |  |  |  |
| DESCR | varchar | 100 | 1 |  |  |  |
| DSPLY_SEQ | int | 4 | 1 |  |  |  |
| CAT1 | varchar | 30 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
