# dbo.GST_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GST_STG_ID | int | 4 | 0 | YES |  |  |
| STG_ID | int | 4 | 0 |  |  |  |
| STG_DTA_SET_CD | varchar | 20 | 0 |  |  |  |
| CLNSD_ADDR_ID | int | 4 | 0 |  |  |  |
| CRM_GST_NBR | varchar | 20 | 1 |  |  |  |
| LYLTY_GST_NBR | varchar | 20 | 1 |  |  |  |
| FRST_NM | varchar | 60 | 1 |  |  |  |
| LAST_NM | varchar | 60 | 1 |  |  |  |
| NCK_NM | varchar | 60 | 1 |  |  |  |
| DRVD_GNDR_CD | varchar | 1 | 1 |  |  |  |
| BRTH_DT | datetime | 8 | 1 |  |  |  |
| PHN_NBR | varchar | 20 | 1 |  |  |  |
| PHN_EXTNS_NBR | varchar | 20 | 1 |  |  |  |
| EMAIL_ADDR_TXT | varchar | 100 | 1 |  |  |  |
| DRVD_UNDR_AGE_13_IND | char | 1 | 1 |  |  |  |
| DRVD_PARNT_CNSNT_IND | char | 1 | 1 |  |  |  |
| PARNT_NM | varchar | 50 | 1 |  |  |  |
| LANG_CD | varchar | 5 | 1 |  |  |  |
| DTA_SET_CD | varchar | 20 | 1 |  |  |  |
| REC_ID | int | 4 | 1 |  |  |  |
| SCR_NBR | int | 4 | 1 |  |  |  |
| OVRLP_DTA_SET_CD | varchar | 20 | 1 |  |  |  |
| OVRLP_REC_ID | int | 4 | 1 |  |  |  |
| OVRLP_SCR_NBR | int | 4 | 1 |  |  |  |
| SRC_REC_UPDT_DT | datetime | 8 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| CRM_MBRSHP_DT | datetime | 8 | 1 |  |  |  |
| CRM_REGIS_STR_ID | int | 4 | 1 |  |  |  |
| MOBILE_TXT_NBR | varchar | 20 | 1 |  |  |  |
