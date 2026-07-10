# dbo.BVILLE_RDMPTN_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BVILLE_RDMPTN_STG_ID | int | 4 | 0 | YES |  |  |
| SRC_REC_ID | int | 4 | 1 |  |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| TRN_NBR | int | 4 | 1 |  |  |  |
| RDMPTN_TYP_ID | int | 4 | 1 |  |  |  |
| CRM_LYLTY_NBR | varchar | 20 | 1 |  |  |  |
| TRN_START_DT | datetime | 8 | 1 |  |  |  |
| RDMPTN_DT | datetime | 8 | 1 |  |  |  |
| RTL_TRN_TYP_CD | varchar | 5 | 1 |  |  |  |
| TRN_SUB_TYP_CD | varchar | 10 | 1 |  |  |  |
| VOID_TRN_IND | char | 1 | 1 |  |  |  |
| VOIDING_TRN_IND | char | 1 | 1 |  |  |  |
| TRAIN_TRN_IND | char | 1 | 1 |  |  |  |
| TRN_TTL_AMT | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
