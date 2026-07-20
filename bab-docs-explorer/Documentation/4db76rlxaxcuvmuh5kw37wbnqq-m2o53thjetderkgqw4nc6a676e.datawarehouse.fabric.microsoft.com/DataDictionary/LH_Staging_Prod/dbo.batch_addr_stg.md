# dbo.batch_addr_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STG_ID | int | 4 | 1 |  |  |  |
| STG_DTA_SET_CD | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_1_TXT | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_2_TXT | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_3_TXT | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_4_TXT | varchar | 8000 | 1 |  |  |  |
| ADDR_LN_5_TXT | varchar | 8000 | 1 |  |  |  |
| APT_UNIT_NBR | varchar | 8000 | 1 |  |  |  |
| CTY_NM | varchar | 8000 | 1 |  |  |  |
| VNTY_CTY_NM | varchar | 8000 | 1 |  |  |  |
| CNTY_NM | varchar | 8000 | 1 |  |  |  |
| ST_PRVNC_ABBRV | varchar | 8000 | 1 |  |  |  |
| ST_PRVNC_NM | varchar | 8000 | 1 |  |  |  |
| PSTL_CD | varchar | 8000 | 1 |  |  |  |
| PSTL_PLS_4_CD | varchar | 8000 | 1 |  |  |  |
| CNTRY_ABBRV | varchar | 8000 | 1 |  |  |  |
| CNTRY_NM | varchar | 8000 | 1 |  |  |  |
| CARI_RTE_CD | varchar | 8000 | 1 |  |  |  |
| LAT_NBR | varchar | 8000 | 1 |  |  |  |
| LONG_NBR | varchar | 8000 | 1 |  |  |  |
| APT_UNIT_IND | varchar | 8000 | 1 |  |  |  |
| SND_MAIL_IND | varchar | 8000 | 1 |  |  |  |
| ADDR_TYP_CD | varchar | 8000 | 1 |  |  |  |
| ADDR_TYP_DESCR | varchar | 8000 | 1 |  |  |  |
| ADDR_ACTV_STAT_CD | varchar | 8000 | 1 |  |  |  |
| QAS_RTRN_CD | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
