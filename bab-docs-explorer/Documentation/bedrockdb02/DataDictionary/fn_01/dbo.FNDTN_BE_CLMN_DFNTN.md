# dbo.FNDTN_BE_CLMN_DFNTN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DFNTN_ID | T_ID | 16 | 0 | YES |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 | YES |  |  |
| PRPRTY_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| DBMS_CLMN_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| DTST_CLMN_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| PRMRY_KEY | T_BOOLEAN | 5 | 0 |  |  |  |
| IN_LANG_TBL | T_BOOLEAN | 5 | 0 |  |  |  |
| IDNTY_CLMN | T_BOOLEAN | 5 | 1 |  |  |  |
| IDNTY_SEQ_NAME | T_LONG_DATA | 255 | 1 |  |  |  |
| TBL_KEY_RSRC_TKN_INDX | T_INTEGER | 2 | 1 |  |  |  |

