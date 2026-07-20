# dbo.ksk_regis_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| KSK_REGIS_STG_ID | int | 4 | 1 |  |  |  |
| SRC_REC_ID | int | 4 | 1 |  |  |  |
| SRC_EXTRCT_DT | datetime2 | 8 | 1 |  |  |  |
| KSK_NBR | int | 4 | 1 |  |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| SNDR_FRST_NM | varchar | 8000 | 1 |  |  |  |
| SNDR_LAST_NM | varchar | 8000 | 1 |  |  |  |
| SNDR_ALIAS_NM | varchar | 8000 | 1 |  |  |  |
| SNDR_BRTH_DT | datetime2 | 8 | 1 |  |  |  |
| SNDR_GNDR_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_EMAIL_ADDR_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_ADDR_LN_1_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_ADDR_LN_2_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_APT_UNIT_NBR | varchar | 8000 | 1 |  |  |  |
| SNDR_CTY_NM | varchar | 8000 | 1 |  |  |  |
| SNDR_PSTL_CD | varchar | 8000 | 1 |  |  |  |
| SNDR_ST_PRVNC_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_CNTRY_TXT | varchar | 8000 | 1 |  |  |  |
| SNDR_SND_MAIL_CD | varchar | 8000 | 1 |  |  |  |
| SNDR_SND_EMAIL_CD | varchar | 8000 | 1 |  |  |  |
| RCPNT_TYP_CD | varchar | 8000 | 1 |  |  |  |
| RCPNT_FRST_NM | varchar | 8000 | 1 |  |  |  |
| RCPNT_LAST_NM | varchar | 8000 | 1 |  |  |  |
| RCPNT_BRTH_DT | datetime2 | 8 | 1 |  |  |  |
| RCPNT_GNDR_TXT | varchar | 8000 | 1 |  |  |  |
| RCPNT_EMAIL_ADDR_TXT | varchar | 8000 | 1 |  |  |  |
| RCPNT_ADDR_LN_1_TXT | varchar | 8000 | 1 |  |  |  |
| RCPNT_ADDR_LN_2_TXT | varchar | 8000 | 1 |  |  |  |
| RCPNT_APT_UNIT_NBR | varchar | 8000 | 1 |  |  |  |
| RCPNT_CTY_NM | varchar | 8000 | 1 |  |  |  |
| RCPNT_PSTL_CD | varchar | 8000 | 1 |  |  |  |
| RCPNT_ST_PRVNC_TXT | varchar | 8000 | 1 |  |  |  |
| RCPNT_CNTRY_TXT | varchar | 8000 | 1 |  |  |  |
| ANML_BARCD_NBR | varchar | 8000 | 1 |  |  |  |
| ANML_NBR | varchar | 8000 | 1 |  |  |  |
| ANML_NM | varchar | 8000 | 1 |  |  |  |
| ANML_TYP_CD | varchar | 8000 | 1 |  |  |  |
| ANML_BRTH_DT_TXT | varchar | 8000 | 1 |  |  |  |
| VTRL_WRLD_ANML_PIN_NBR | varchar | 8000 | 1 |  |  |  |
| PRTY_TRN_CD | varchar | 8000 | 1 |  |  |  |
| TRN_LANG_CD | varchar | 8000 | 1 |  |  |  |
| TRN_START_DT | datetime2 | 8 | 1 |  |  |  |
| TRN_END_DT | datetime2 | 8 | 1 |  |  |  |
| PARNT_CNSNT_CD | varchar | 8000 | 1 |  |  |  |
| PARNT_NM | varchar | 8000 | 1 |  |  |  |
| UNDR_AGE_13_CD | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| RCPNT_CHKSUM | int | 4 | 1 |  |  |  |
| GST_CHKSUM | int | 4 | 1 |  |  |  |
| ADDR_CHKSUM | int | 4 | 1 |  |  |  |
