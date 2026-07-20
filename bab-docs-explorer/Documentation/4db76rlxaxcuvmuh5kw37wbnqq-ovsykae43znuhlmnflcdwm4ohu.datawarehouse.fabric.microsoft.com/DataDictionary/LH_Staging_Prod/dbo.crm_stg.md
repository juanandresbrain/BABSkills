# dbo.crm_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_STG_ID | int | 4 | 1 |  |  |  |
| SRC_REC_CRTE_DT | datetime2 | 8 | 1 |  |  |  |
| STR_NBR | varchar | 8000 | 1 |  |  |  |
| CRM_GST_NBR | varchar | 8000 | 1 |  |  |  |
| CRM_LYLTY_NBR | varchar | 8000 | 1 |  |  |  |
| CRM_HSHLD_NBR | varchar | 8000 | 1 |  |  |  |
| CRM_ADDR_NBR | int | 4 | 1 |  |  |  |
| FRST_NM | varchar | 8000 | 1 |  |  |  |
| LAST_NM | varchar | 8000 | 1 |  |  |  |
| GNDR_CD | varchar | 8000 | 1 |  |  |  |
| BRTH_DT | datetime2 | 8 | 1 |  |  |  |
| ADDR_LN_1_TXT | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_2_TXT | varchar | 8000 | 1 |  |  |  |
| CTY_NM | varchar | 8000 | 1 |  |  |  |
| ST_PRVNC_TXT | varchar | 8000 | 1 |  |  |  |
| PSTL_CD | varchar | 8000 | 1 |  |  |  |
| CNTRY_ABBRV | varchar | 8000 | 1 |  |  |  |
| PHN_NBR | varchar | 8000 | 1 |  |  |  |
| PHN_EXTNS_NBR | varchar | 8000 | 1 |  |  |  |
| EMAIL_ADDR_TXT | varchar | 8000 | 1 |  |  |  |
| SND_MAIL_CD | varchar | 8000 | 1 |  |  |  |
| SND_EMAIL_CD | varchar | 8000 | 1 |  |  |  |
| EMAIL_OPT_IN_CD | varchar | 8000 | 1 |  |  |  |
| LANG_CD | varchar | 8000 | 1 |  |  |  |
| SRC_REC_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| CRM_MBRSHP_DT | datetime2 | 8 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| GST_CHKSUM | int | 4 | 1 |  |  |  |
| ADDR_CHKSUM | int | 4 | 1 |  |  |  |
| MAIL_OPT_IN_CD | varchar | 8000 | 1 |  |  |  |
| MOBILE_TXT_NBR | varchar | 8000 | 1 |  |  |  |
| MOBILE_TXT_STAT_CD | varchar | 8000 | 1 |  |  |  |
| MOBILE_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| MAIL_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| EMAIL_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| DM_ATTR_STAT_CD | varchar | 8000 | 1 |  |  |  |
| EMAIL_ATTR_STAT_CD | varchar | 8000 | 1 |  |  |  |
| EMAILCERT_STAT_CD | varchar | 8000 | 1 |  |  |  |
| EMAILCERT_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| SFSPOINTS_STAT_CD | varchar | 8000 | 1 |  |  |  |
| SFSPOINTS_UPDT_DT | datetime2 | 8 | 1 |  |  |  |
