# dbo.FNDTN_DSHBRD_PRMTR_TYPE

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRMTR_TYPE_ID | int | 4 | 0 | YES |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| INTRFC_NAME | varchar | 255 | 1 |  |  |  |
| MAX_HRCHY_DPTH | tinyint | 1 | 1 |  |  |  |
| DFLT_VAL | nvarchar | 510 | 1 |  |  |  |
| DFLT_DSPLY_VAL | nvarchar | 510 | 1 |  |  |  |
| FLD_ID | binary | 16 | 1 |  | YES |  |
| QRY_STRNG_PRMTR_NAME | varchar | 255 | 1 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| SRCH_TYPE | tinyint | 1 | 0 |  |  |  |
| BI_DIM_ID | smallint | 2 | 1 |  |  |  |
| PRCTV_CACHE_CNFGRTN | varchar | 255 | 1 |  |  |  |

