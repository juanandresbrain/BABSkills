# dbo.vldtn_prcs

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_NM | varchar | 8000 | 1 |  |  |  |
| VLDTN_PRCS_DESCR | varchar | 8000 | 1 |  |  |  |
| FREQ_CD | varchar | 8000 | 1 |  |  |  |
| FREQ_DESCR | varchar | 8000 | 1 |  |  |  |
| CLS_CD | varchar | 8000 | 1 |  |  |  |
| CLS_DESCR | varchar | 8000 | 1 |  |  |  |
| ACTV_STRT_DT | datetime2 | 8 | 1 |  |  |  |
| ACTV_END_DT | datetime2 | 8 | 1 |  |  |  |
| ACTV_STAT_CD | varchar | 8000 | 1 |  |  |  |
| INACTV_RSN_TXT | varchar | 8000 | 1 |  |  |  |
| THRSHLD_QTY | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| BEG_EFF_DT | datetime2 | 8 | 1 |  |  |  |
| END_EFF_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
