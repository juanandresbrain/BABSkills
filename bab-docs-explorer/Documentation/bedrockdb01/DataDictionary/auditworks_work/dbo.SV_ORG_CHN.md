# dbo.SV_ORG_CHN

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | int | 4 | 0 |  |  |  |
| PRTY_ID | binary | 16 | 0 |  |  |  |
| ORG_CHN_TYPE_CODE | varchar | 4 | 0 |  |  |  |
| ORG_CHN_NAME | varchar | 50 | 0 |  |  |  |
| ORG_CHN_SHRT_NAME | varchar | 25 | 0 |  |  |  |
| ACTV | numeric | 5 | 0 |  |  |  |
| GMT_OFST | numeric | 9 | 1 |  |  |  |
| STLMNT_BLNG_NAME | varchar | 50 | 1 |  |  |  |
| PLAN_START_DATE | datetime | 8 | 1 |  |  |  |
| PLAN_END_DATE | datetime | 8 | 1 |  |  |  |
| AUTO_ACPT | numeric | 5 | 1 |  |  |  |
| USE_OFLN_INVNTRY_MNGMNT | numeric | 5 | 0 |  |  |  |
| NTWRK_TYPE | varchar | 4 | 1 |  |  |  |
| GL_CMPNY_NUM | varchar | 20 | 1 |  |  |  |
| GL_LOC_NUM | varchar | 20 | 1 |  |  |  |
| COMP_DATE | datetime | 8 | 1 |  |  |  |
| RQR_ITEM_INFO | numeric | 5 | 0 |  |  |  |
| SHIP_HOLD_DATE | datetime | 8 | 1 |  |  |  |
| OPEN_TO_RCV_DATE | datetime | 8 | 1 |  |  |  |
| CSTMR_PCKP | numeric | 5 | 0 |  |  |  |
| OCPNCY_COST_FXD | numeric | 9 | 1 |  |  |  |
| OCPNCY_COST_VRBL | numeric | 9 | 1 |  |  |  |
| OCPNCY_COST_VRBL_THRSHLD | numeric | 9 | 1 |  |  |  |
| CSTMR_SHPMNT | numeric | 5 | 0 |  |  |  |
| SHRNKG_FCTR | numeric | 9 | 1 |  |  |  |
| CLS_DATE | datetime | 8 | 1 |  |  |  |
| OPEN_DATE | datetime | 8 | 1 |  |  |  |
| RPLNSHBL | numeric | 5 | 0 |  |  |  |
| TRNSFR_CPBLTY | numeric | 5 | 0 |  |  |  |
| DFLT_ADRS_SEQ | numeric | 9 | 1 |  |  |  |
| DFLT_CRNCY_CODE | char | 3 | 1 |  |  |  |
| OPRT_HOUR_ID | binary | 16 | 1 |  |  |  |
| OPEN_HOUR_ID | binary | 16 | 1 |  |  |  |
| TAX_JRSDCTN_CODE | char | 5 | 1 |  |  |  |
| MD_PRMTR_TBL_NUM | smallint | 2 | 1 |  |  |  |
| VCHR_CNFG_TYPE | varchar | 4 | 0 |  |  |  |
| PRMRY_BANK_ACNT_ID | smallint | 2 | 1 |  |  |  |
| PRMRY_LANG | varchar | 255 | 1 |  |  |  |
| PRMRY_LANG_ID | smallint | 2 | 1 |  |  |  |
| USE_AS_TMPLT | numeric | 5 | 0 |  |  |  |
| TMPLT_DESC | varchar | 255 | 1 |  |  |  |
| PRMRY_EML_ADRS_ID | binary | 16 | 1 |  |  |  |
| EXTRNL_RFRNC_NUM | int | 4 | 1 |  |  |  |
| SYS_CODE | varchar | 4 | 0 |  |  |  |
| ORG_CHN_TYPE_SHRT_DESC | varchar | 50 | 0 |  |  |  |
