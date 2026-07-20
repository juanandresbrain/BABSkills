# dbo.vldtn_prcs_instnc_dtl_prcs_spfc

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 1 |  |  |  |
| HSH_KEY_DTA_SET_CD | varchar | 8000 | 1 |  |  |  |
| HSH_KEY_COL_NM | varchar | 8000 | 1 |  |  |  |
| HSH_KEY_TXT | varchar | 8000 | 1 |  |  |  |
| VLDTD_TBL_NM | varchar | 8000 | 1 |  |  |  |
| VLDTD_COL_NM | varchar | 8000 | 1 |  |  |  |
| VLDTD_COL_VAL_AMT | decimal | 9 | 1 |  |  |  |
| VLDTD_COL_VAL_TXT | varchar | 8000 | 1 |  |  |  |
| VLDTD_COL_VAL_DT | datetime2 | 8 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
