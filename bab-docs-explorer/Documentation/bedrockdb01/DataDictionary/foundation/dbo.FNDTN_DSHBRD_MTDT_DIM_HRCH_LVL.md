# dbo.FNDTN_DSHBRD_MTDT_DIM_HRCH_LVL

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DIM_HRCHY_LVL_ID | binary | 16 | 0 |  |  |  |
| DIM_HRCHY_ID | binary | 16 | 1 |  |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 512 | 1 |  |  |  |
| HRZNTL_ALGNMNT | tinyint | 1 | 1 |  |  |  |
| FRMT_STRNG | varchar | 60 | 1 |  |  |  |
| HRCHY_LVL_NUM | tinyint | 1 | 0 |  |  |  |
| MDX_FRGMNT | nvarchar | 4000 | 1 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| IS_SYS | bit | 1 | 0 |  |  |  |
| DATA_TYPE_FULL_NAME | varchar | 255 | 1 |  |  |  |
