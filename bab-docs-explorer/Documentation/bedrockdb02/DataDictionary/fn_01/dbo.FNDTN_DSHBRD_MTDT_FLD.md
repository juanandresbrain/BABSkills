# dbo.FNDTN_DSHBRD_MTDT_FLD

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLD_ID | binary | 16 | 0 | YES |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 512 | 1 |  |  |  |
| HRZNTL_ALGNMNT | tinyint | 1 | 1 |  |  |  |
| FRMT_STRNG | varchar | 60 | 1 |  |  |  |
| DATA_TYPE_FULL_NAME | varchar | 255 | 1 |  |  |  |
| MDX_FRGMNT | nvarchar | 4000 | 1 |  |  |  |
| FLD_GRP_CTGRY_ID | smallint | 2 | 0 |  | YES |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| IS_SYS | bit | 1 | 0 |  |  |  |
| FLD_TYPE_ID | tinyint | 1 | 0 |  | YES |  |
| MDX_CALC_MODE | tinyint | 1 | 1 |  |  |  |
| TMPLT_ID | binary | 16 | 0 |  | YES |  |
| IS_EDF | bit | 1 | 0 |  |  |  |
| CRNCY_OPTN | tinyint | 1 | 0 |  |  |  |
| ALWD_DATE_DMNSNS | varchar | 15 | 1 |  |  |  |
| AGRGT_FNCTN | varchar | 25 | 1 |  |  |  |
| IS_DFLT_MBR_ALL | bit | 1 | 0 |  |  |  |

