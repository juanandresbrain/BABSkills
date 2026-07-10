# dbo.CRM_POS_STG_RJCT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_POS_STG_RJCT_ID | int | 4 | 0 | YES |  |  |
| RJCT_RSN_ID | int | 4 | 0 |  |  |  |
| CRM_GST_NBR | varchar | 20 | 1 |  |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| POS_TRN_DT | datetime | 8 | 1 |  |  |  |
| POS_TRN_NBR | varchar | 20 | 1 |  |  |  |
| SRC_TRN_REC_ID | int | 4 | 1 |  |  |  |
| RGSTR_NBR | varchar | 20 | 1 |  |  |  |
| POS_TRN_PSTD_DT | datetime | 8 | 1 |  |  |  |
| CRM_LYLTY_NBR | varchar | 20 | 1 |  |  |  |
| CRM_MBRSHP_DT | datetime | 8 | 1 |  |  |  |
| SFS_TRN_TYP_CD | varchar | 5 | 1 |  |  |  |
| SLS_MDULE_TRN_NBR | varchar | 20 | 1 |  |  |  |
| TTL_NET_RTL_AMT | decimal | 9 | 1 |  |  |  |
| ETL_ERR_COL_NBR | int | 4 | 1 |  |  |  |
| ETL_ERR_NBR | int | 4 | 1 |  |  |  |
| ETL_ERR_DESCR | varchar | 100 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
