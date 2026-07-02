# dbo.FNDTN_DSHBRD_CLNDR_OPTN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_OPTN_ID | binary | 16 | 0 | YES |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| CLNDR_TYPE_ID | tinyint | 1 | 0 |  | YES |  |
| PRD_TYPE_ID | tinyint | 1 | 0 |  | YES |  |
| FRMT_STRNG | varchar | 60 | 1 |  |  |  |
| SEQ_NUM | smallint | 2 | 0 |  |  |  |
| MDX | nvarchar | 4000 | 1 |  |  |  |
| TMPLT_ID | binary | 16 | 0 |  | YES |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| IS_SYS | bit | 1 | 0 |  |  |  |
| DATA_TYPE_FULL_NAME | varchar | 255 | 1 |  |  |  |
| TKN_1_LBL_RES_NAME | varchar | 255 | 1 |  |  |  |

