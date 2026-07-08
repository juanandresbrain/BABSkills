# dbo.ORG_CHN

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| PRTY_ID | T_ID | 16 | 0 |  |  |  |
| ORG_CHN_TYPE_CODE | nvarchar | 8 | 0 |  |  |  |
| ORG_CHN_NAME | nvarchar | 120 | 1 |  |  |  |
| ORG_CHN_SHRT_NAME | nvarchar | 50 | 0 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| GMT_OFST | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| STLMNT_BLNG_NAME | nvarchar | 100 | 1 |  |  |  |
| PLAN_START_DATE | T_DATE | 8 | 1 |  |  |  |
| PLAN_END_DATE | T_DATE | 8 | 1 |  |  |  |
| AUTO_ACPT | T_FLAG | 5 | 1 |  |  |  |
| USE_OFLN_INVNTRY_MNGMNT | T_BOOLEAN | 5 | 0 |  |  |  |
| NTWRK_TYPE | nvarchar | 8 | 1 |  |  |  |
| GL_CMPNY_NUM | nvarchar | 40 | 1 |  |  |  |
| GL_LOC_NUM | nvarchar | 40 | 1 |  |  |  |
| COMP_DATE | T_DATE | 8 | 1 |  |  |  |
| RQR_ITEM_INFO | T_BOOLEAN | 5 | 0 |  |  |  |
| SHIP_HOLD_DATE | T_DATE | 8 | 1 |  |  |  |
| OPEN_TO_RCV_DATE | T_DATE | 8 | 1 |  |  |  |
| CSTMR_PCKP | T_BOOLEAN | 5 | 0 |  |  |  |
| OCPNCY_COST_FXD | T_MONEY | 9 | 1 |  |  |  |
| OCPNCY_COST_VRBL | T_MONEY | 9 | 1 |  |  |  |
| OCPNCY_COST_VRBL_THRSHLD | T_MONEY | 9 | 1 |  |  |  |
| CSTMR_SHPMNT | T_BOOLEAN | 5 | 0 |  |  |  |
| SHRNKG_FCTR | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| CLS_DATE | T_DATE | 8 | 1 |  |  |  |
| OPEN_DATE | T_DATE | 8 | 1 |  |  |  |
| RPLNSHBL | T_BOOLEAN | 5 | 0 |  |  |  |
| TRNSFR_CPBLTY | T_BOOLEAN | 5 | 0 |  |  |  |
| DFLT_ADRS_SEQ | T_SEQUENCE_NUMBER | 9 | 1 |  |  |  |
| DFLT_CRNCY_CODE | nchar | 6 | 1 |  |  |  |
| OPRT_HOUR_ID | T_ID | 16 | 1 |  |  |  |
| OPEN_HOUR_ID | T_ID | 16 | 1 |  |  |  |
| TAX_JRSDCTN_CODE | nchar | 10 | 1 |  |  |  |
| MD_PRMTR_TBL_NUM | T_INTEGER | 2 | 1 |  |  |  |
| VCHR_CNFG_TYPE | nvarchar | 8 | 0 |  |  |  |
| PRMRY_BANK_ACNT_ID | T_INTEGER | 2 | 1 |  |  |  |
| PRMRY_LANG_ID | T_INTEGER | 2 | 1 |  |  |  |
| USE_AS_TMPLT | T_BOOLEAN | 5 | 0 |  |  |  |
| TMPLT_DESC | nvarchar | 510 | 1 |  |  |  |
| PRMRY_EML_ADRS_ID | T_ID | 16 | 1 |  |  |  |
| EXTRNL_RFRNC_NUM | T_LONG_INTEGER | 4 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
| TIME_ZONE_ID | int | 4 | 1 |  |  |  |
| LOC_CTGRY_CODE | nvarchar | 8 | 1 |  |  |  |
| SLNG_FLAG | T_BOOLEAN | 5 | 1 |  |  |  |
| ORG_CHN_STS | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| REOPEN_DATE | T_DATE | 8 | 1 |  |  |  |
| WH_SYSTM | T_BOOLEAN | 5 | 1 |  |  |  |
| ALLW_CSTM_ODR | T_BOOLEAN | 5 | 1 |  |  |  |
| SND_INV_MVMNT_TO_OMS | T_BOOLEAN | 5 | 1 |  |  |  |
| ALLW_CSTM_PKP_ODR | T_BOOLEAN | 5 | 1 |  |  |  |
| SLNG_SPC | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| NON_SLNG_SPC | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| TRGT_SALES | T_MONEY | 9 | 1 |  |  |  |
| RTNG_PRRTY | T_LONG_INTEGER | 4 | 1 |  |  |  |
| CLS_RSN | nvarchar | 510 | 1 |  |  |  |
