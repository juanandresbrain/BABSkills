# dbo.FNDTN_BLNCNG_CHCK

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BLNCNG_CHCK_ID | binary | 16 | 0 |  |  |  |
| BLNCNG_GRP_ID | binary | 16 | 0 |  |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| ACTV_FLG | bit | 1 | 0 |  |  |  |
| FRST_STMNT | ntext | 16 | 0 |  |  |  |
| SCND_STMNT | ntext | 16 | 0 |  |  |  |
| IS_SUB_CHCK | bit | 1 | 0 |  |  |  |
| TLRNC_VAL | money | 8 | 1 |  |  |  |
| TLRNC_TYPE | char | 3 | 1 |  |  |  |
