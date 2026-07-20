# dbo.vldtn_trend_fact

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_TREND_FACT_ID | int | 4 | 1 |  |  |  |
| VLDTN_TREND_REPORT_ID | int | 4 | 1 |  |  |  |
| VLDTN_TREND_STAT_ID | int | 4 | 1 |  |  |  |
| DT_ID | int | 4 | 1 |  |  |  |
| TM_ID | int | 4 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| METRIC_VALUE | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
