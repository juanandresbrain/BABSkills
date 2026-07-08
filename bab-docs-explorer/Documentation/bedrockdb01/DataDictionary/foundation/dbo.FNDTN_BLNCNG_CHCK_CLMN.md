# dbo.FNDTN_BLNCNG_CHCK_CLMN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CHCK_CLMN_ID | binary | 16 | 0 |  |  |  |
| BLNCNG_CHCK_ID | binary | 16 | 0 |  |  |  |
| CLMN_INDEX | smallint | 2 | 0 |  |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| IS_KEY | bit | 1 | 0 |  |  |  |
| IS_ID | bit | 1 | 0 |  |  |  |
| OLAP_TYPE | tinyint | 1 | 1 |  |  |  |
| OLAP_INDX | smallint | 2 | 1 |  |  |  |
| TLRNC_VAL | money | 8 | 1 |  |  |  |
| TLRNC_TYPE | char | 3 | 1 |  |  |  |
