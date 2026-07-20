# dbo.crm_pos_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_POS_STG_ID | int | 4 | 1 |  |  |  |
| CRM_GST_NBR | varchar | 8000 | 1 |  |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| POS_TRN_DT | datetime2 | 8 | 1 |  |  |  |
| POS_TRN_NBR | varchar | 8000 | 1 |  |  |  |
| SRC_TRN_REC_ID | int | 4 | 1 |  |  |  |
| RGSTR_NBR | varchar | 8000 | 1 |  |  |  |
| POS_TRN_PSTD_DT | datetime2 | 8 | 1 |  |  |  |
| CRM_LYLTY_NBR | varchar | 8000 | 1 |  |  |  |
| CRM_MBRSHP_DT | datetime2 | 8 | 1 |  |  |  |
| SFS_TRN_TYP_CD | varchar | 8000 | 1 |  |  |  |
| SLS_MDULE_TRN_NBR | varchar | 8000 | 1 |  |  |  |
| TTL_NET_RTL_AMT | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
