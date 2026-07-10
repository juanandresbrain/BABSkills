# dbo.VLDTN_TREND_FACT

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_TREND_FACT_ID | int | 4 | 0 | YES |  |  |
| VLDTN_TREND_REPORT_ID | int | 4 | 0 |  |  |  |
| VLDTN_TREND_STAT_ID | int | 4 | 0 |  |  |  |
| DT_ID | int | 4 | 0 |  |  |  |
| TM_ID | int | 4 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| METRIC_VALUE | int | 4 | 0 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
