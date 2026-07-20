# dbo.vldtn_prcs_instnc_dtl_ref_intgrty

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 1 |  |  |  |
| PARNT_TBL_NM | varchar | 8000 | 1 |  |  |  |
| CHILD_TBL_NM | varchar | 8000 | 1 |  |  |  |
| CHILD_COL_NM | varchar | 8000 | 1 |  |  |  |
| MISS_CHILD_ID | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
