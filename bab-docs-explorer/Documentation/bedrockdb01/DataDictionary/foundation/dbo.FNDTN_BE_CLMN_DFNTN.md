# dbo.FNDTN_BE_CLMN_DFNTN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DFNTN_ID | T_ID | 16 | 0 |  |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| PRPRTY_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| DBMS_CLMN_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| DTST_CLMN_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| PRMRY_KEY | T_BOOLEAN | 1 | 0 |  |  |  |
| IN_LANG_TBL | T_BOOLEAN | 1 | 0 |  |  |  |
| IDNTY_CLMN | T_BOOLEAN | 1 | 1 |  |  |  |
| IDNTY_SEQ_NAME | T_LONG_DATA | 255 | 1 |  |  |  |
| TBL_KEY_RSRC_TKN_INDX | T_INTEGER | 2 | 1 |  |  |  |
