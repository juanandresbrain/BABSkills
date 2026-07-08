# dbo.SV_HEAD_OFFICE

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | int | 4 | 0 |  |  |  |
| ORG_CHN_NAME | varchar | 50 | 0 |  |  |  |
| ORG_CHN_SHRT_NAME | varchar | 25 | 0 |  |  |  |
| ORG_CHN_TYPE_CODE | varchar | 4 | 0 |  |  |  |
| PRMRY_LANG | varchar | 255 | 1 |  |  |  |
| PRMRY_LANG_ID | smallint | 2 | 1 |  |  |  |
| PRTY_ID | binary | 16 | 0 |  |  |  |
| AUTO_ACPT | numeric | 5 | 1 |  |  |  |
| GMT_OFST | numeric | 9 | 1 |  |  |  |
| GL_CMPNY_NUM | varchar | 20 | 1 |  |  |  |
| GL_LOC_NUM | varchar | 20 | 1 |  |  |  |
| USE_AS_TMPLT | numeric | 5 | 0 |  |  |  |
| TMPLT_DESC | varchar | 255 | 1 |  |  |  |
| OPEN_DATE | datetime | 8 | 1 |  |  |  |
| CLS_DATE | datetime | 8 | 1 |  |  |  |
| ACTV | numeric | 5 | 0 |  |  |  |
| STLMNT_BLNG_NAME | varchar | 50 | 1 |  |  |  |
| MD_PRMTR_TBL_NUM | smallint | 2 | 1 |  |  |  |
| VCHR_CNFG_TYPE | varchar | 4 | 0 |  |  |  |
| TAX_JRSDCTN_CODE | char | 5 | 1 |  |  |  |
| PRMRY_BANK_ACNT_ID | smallint | 2 | 1 |  |  |  |
| SYS_CODE | varchar | 4 | 0 |  |  |  |
| ORG_CHN_TYPE_SHRT_DESC | varchar | 50 | 0 |  |  |  |
