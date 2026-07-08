# dbo.FNDTN_DSHBRD_MTDT_FLD_PRPRTY

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLD_PRPRTY_ID | binary | 16 | 0 |  |  |  |
| FLD_ID | binary | 16 | 0 |  |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 512 | 1 |  |  |  |
| HRZNTL_ALGNMNT | tinyint | 1 | 1 |  |  |  |
| FRMT_STRNG | varchar | 60 | 1 |  |  |  |
| DATA_TYPE_FULL_NAME | varchar | 255 | 1 |  |  |  |
| MDX_FRGMNT | nvarchar | 4000 | 1 |  |  |  |
| FLD_GRP_CTGRY_ID | smallint | 2 | 0 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| IS_SYS | bit | 1 | 0 |  |  |  |
| TMPLT_ID | binary | 16 | 0 |  |  |  |
