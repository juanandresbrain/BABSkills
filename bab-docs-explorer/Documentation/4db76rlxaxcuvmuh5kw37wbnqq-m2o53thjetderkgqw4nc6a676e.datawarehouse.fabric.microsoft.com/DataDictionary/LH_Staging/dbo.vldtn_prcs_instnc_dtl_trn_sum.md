# dbo.vldtn_prcs_instnc_dtl_trn_sum

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 1 |  |  |  |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 1 |  |  |  |
| HASH_KEY_COL_NM | varchar | 8000 | 1 |  |  |  |
| HSH_KEY_TXT | varchar | 8000 | 1 |  |  |  |
| SRC_TBL_NM | varchar | 8000 | 1 |  |  |  |
| SRC_COL_NM | varchar | 8000 | 1 |  |  |  |
| SRC_TRN_SUM_AMT | decimal | 9 | 1 |  |  |  |
| TGT_TBL_NM | varchar | 8000 | 1 |  |  |  |
| TGT_COL_NM | varchar | 8000 | 1 |  |  |  |
| TGT_TRN_SUM_AMT | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
