# dbo.bville_rdmptn_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BVILLE_RDMPTN_STG_ID | int | 4 | 1 |  |  |  |
| SRC_REC_ID | int | 4 | 1 |  |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| TRN_NBR | int | 4 | 1 |  |  |  |
| RDMPTN_TYP_ID | int | 4 | 1 |  |  |  |
| CRM_LYLTY_NBR | varchar | 8000 | 1 |  |  |  |
| TRN_START_DT | datetime2 | 8 | 1 |  |  |  |
| RDMPTN_DT | datetime2 | 8 | 1 |  |  |  |
| RTL_TRN_TYP_CD | varchar | 8000 | 1 |  |  |  |
| TRN_SUB_TYP_CD | varchar | 8000 | 1 |  |  |  |
| VOID_TRN_IND | varchar | 8000 | 1 |  |  |  |
| VOIDING_TRN_IND | varchar | 8000 | 1 |  |  |  |
| TRAIN_TRN_IND | varchar | 8000 | 1 |  |  |  |
| TRN_TTL_AMT | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
