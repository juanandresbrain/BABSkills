# dbo.GST_SUM_FACT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNSD_GST_ID | int | 4 | 0 |  |  |  |
| CLNSD_ADDR_ID | int | 4 | 0 |  |  |  |
| FRST_STR_VST_DT_ID | int | 4 | 0 |  |  |  |
| SCND_STR_VST_DT_ID | int | 4 | 0 |  |  |  |
| THRD_STR_VST_DT_ID | int | 4 | 0 |  |  |  |
| LAST_STR_VST_DT_ID | int | 4 | 0 |  |  |  |
| GST_SUM_FACT_UPDT_DT_ID | int | 4 | 0 |  |  |  |
| DY_INTVL_FRST_SCND_VST_CNT | int | 4 | 1 |  |  |  |
| DY_INTVL_SCND_THRD_VST_CNT | int | 4 | 1 |  |  |  |
| NEW_VS_RPT_CD | char | 1 | 1 |  |  |  |
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
| CLNSD_GST_AGE_NBR | varchar | 20 | 1 |  |  |  |
| GNDR_CD | varchar | 20 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
