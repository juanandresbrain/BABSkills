# dbo.vldtn_prcs_instnc_dtl_miss_key

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 1 |  |  |  |
| HASH_KEY_DATA_SET_CD | varchar | 8000 | 1 |  |  |  |
| HSH_KEY_COL_NM | varchar | 8000 | 1 |  |  |  |
| HSH_KEY_TXT | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
