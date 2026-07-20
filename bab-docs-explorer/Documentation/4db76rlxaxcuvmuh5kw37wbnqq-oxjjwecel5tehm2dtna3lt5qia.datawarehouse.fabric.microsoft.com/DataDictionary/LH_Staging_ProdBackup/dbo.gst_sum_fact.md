# dbo.gst_sum_fact

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNSD_GST_ID | int | 4 | 1 |  |  |  |
| CLNSD_ADDR_ID | int | 4 | 1 |  |  |  |
| FRST_STR_VST_DT_ID | int | 4 | 1 |  |  |  |
| SCND_STR_VST_DT_ID | int | 4 | 1 |  |  |  |
| THRD_STR_VST_DT_ID | int | 4 | 1 |  |  |  |
| LAST_STR_VST_DT_ID | int | 4 | 1 |  |  |  |
| GST_SUM_FACT_UPDT_DT_ID | int | 4 | 1 |  |  |  |
| DY_INTVL_FRST_SCND_VST_CNT | int | 4 | 1 |  |  |  |
| DY_INTVL_SCND_THRD_VST_CNT | int | 4 | 1 |  |  |  |
| NEW_VS_RPT_CD | varchar | 8000 | 1 |  |  |  |
| TTL_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_RCNCY_CNT | int | 4 | 1 |  |  |  |
| MNTH_01_03_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_04_06_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_07_09_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_10_12_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_13_15_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_16_18_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_19_21_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_22_24_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_25_36_VST_CNT | int | 4 | 1 |  |  |  |
| MNTH_25_PLUS_VST_CNT | int | 4 | 1 |  |  |  |
| CLNSD_GST_AGE_NBR | varchar | 8000 | 1 |  |  |  |
| GNDR_CD | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
