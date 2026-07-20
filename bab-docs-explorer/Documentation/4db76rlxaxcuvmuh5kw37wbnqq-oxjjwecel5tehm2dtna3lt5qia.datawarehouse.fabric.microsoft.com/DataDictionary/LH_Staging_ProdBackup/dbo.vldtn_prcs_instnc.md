# dbo.vldtn_prcs_instnc

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_ID | int | 4 | 1 |  |  |  |
| EXEC_STRT_DTTM | datetime2 | 8 | 1 |  |  |  |
| EXEC_END_DTTM | datetime2 | 8 | 1 |  |  |  |
| PASS_REC_CNT | int | 4 | 1 |  |  |  |
| FAIL_REC_CNT | int | 4 | 1 |  |  |  |
| THRSHLD_QTY | decimal | 9 | 1 |  |  |  |
| PASS_IND | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
