# dbo.FirstLogic_v_QAS_QAS_Data_Cleansed

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STG_ID | int | 4 | 0 |  |  |  |
| STG_DTA_SET_CD | varchar | 20 | 0 |  |  |  |
| ADDR_LN_1_TXT | varchar | 60 | 1 |  |  |  |
| ADDR_LN_2_TXT | varchar | 60 | 1 |  |  |  |
| ADDR_LN_3_TXT | varchar | 60 | 1 |  |  |  |
| ADDR_LN_4_TXT | varchar | 60 | 1 |  |  |  |
| ADDR_LN_5_TXT | varchar | 60 | 1 |  |  |  |
| APT_UNIT_NBR | varchar | 60 | 1 |  |  |  |
| CTY_NM | varchar | 60 | 1 |  |  |  |
| VNTY_CTY_NM | varchar | 60 | 1 |  |  |  |
| CNTY_NM | varchar | 60 | 1 |  |  |  |
| ST_PRVNC_ABBRV | varchar | 5 | 1 |  |  |  |
| ST_PRVNC_NM | varchar | 60 | 1 |  |  |  |
| PSTL_CD | varchar | 10 | 1 |  |  |  |
| PSTL_PLS_4_CD | varchar | 5 | 1 |  |  |  |
| CNTRY_ABBRV | varchar | 5 | 1 |  |  |  |
| CNTRY_NM | varchar | 60 | 1 |  |  |  |
| LAT_NBR | varchar | 20 | 1 |  |  |  |
| LONG_NBR | varchar | 20 | 1 |  |  |  |
| APT_UNIT_IND | char | 1 | 1 |  |  |  |
| SND_MAIL_IND | char | 1 | 1 |  |  |  |
| ADDR_TYP_CD | varchar | 10 | 1 |  |  |  |
| ADDR_TYP_DESCR | varchar | 50 | 1 |  |  |  |
| ADDR_ACTV_STAT_CD | varchar | 10 | 1 |  |  |  |
| QAS_RTRN_CD | varchar | 30 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| CARI_RTE_CD | varchar | 20 | 1 |  |  |  |
