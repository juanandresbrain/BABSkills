# dbo.FNDTN_DSHBRD_DATA_VIEW_CLMN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLMN_ID | binary | 16 | 0 |  |  |  |
| DATA_VIEW_ID | binary | 16 | 0 |  |  |  |
| SEQ_NUM | tinyint | 1 | 0 |  |  |  |
| NAME_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| DESC_RES_NAME | nvarchar | 510 | 1 |  |  |  |
| FLD_TYPE_ID | tinyint | 1 | 0 |  |  |  |
| CNTNT_ID | binary | 16 | 1 |  |  |  |
| TITLE_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| CLMN_NAME | nvarchar | 120 | 0 |  |  |  |
| FRMT_STRNG | varchar | 60 | 1 |  |  |  |
| HRZNTL_ALGNMNT | tinyint | 1 | 1 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| OLAP_INDX | smallint | 2 | 1 |  |  |  |
| CLMN_INDX | smallint | 2 | 0 |  |  |  |
| CNTNT_OPTN_ID | binary | 16 | 1 |  |  |  |
| CLMN_DATA | nvarchar | 4000 | 1 |  |  |  |
| CLMN_WDTH | smallint | 2 | 1 |  |  |  |
| DIM_HRCHY_ID | binary | 16 | 1 |  |  |  |
| SRC_CLMN_ID | binary | 16 | 1 |  |  |  |
| DATA_TYPE_FULL_NAME | varchar | 255 | 1 |  |  |  |
| TOTAL_FUNC | tinyint | 1 | 1 |  |  |  |
| CLMN_FUNC | tinyint | 1 | 1 |  |  |  |
| ROW_FLTR_EXPRSN | nvarchar | 4000 | 1 |  |  |  |
| ROW_FLTR_EXPRSN_INFX | nvarchar | 4000 | 1 |  |  |  |
| CNTNT_FLTR_EXPRSN | nvarchar | 4000 | 1 |  |  |  |
| CNTNT_FLTR_EXPRSN_INFX | nvarchar | 4000 | 1 |  |  |  |
| IS_DYNMC | bit | 1 | 0 |  |  |  |
| TKN_1_VAL | varchar | 50 | 1 |  |  |  |
| CRNCY_SRC | tinyint | 1 | 1 |  |  |  |
| CNTNT_OPTN_DATE_DMNSN_ROLE | smallint | 2 | 1 |  |  |  |
| IS_DATA_HAS_RES | bit | 1 | 0 |  |  |  |
