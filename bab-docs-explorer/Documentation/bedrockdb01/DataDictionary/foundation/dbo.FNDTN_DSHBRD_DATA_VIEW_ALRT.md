# dbo.FNDTN_DSHBRD_DATA_VIEW_ALRT

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRT_ID | binary | 16 | 0 |  |  |  |
| USER_ID | int | 4 | 0 |  |  |  |
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  |  |  |
| TRGT_CLMN_ID | binary | 16 | 1 |  |  |  |
| ALRT_ACTN | tinyint | 1 | 0 |  |  |  |
| ALRT_CLR_SCHM | tinyint | 1 | 0 |  |  |  |
| TOOL_TIP_TEXT | nvarchar | 510 | 1 |  |  |  |
| EXPRSN_STRNG | nvarchar | 4000 | 1 |  |  |  |
| EXPRSN_OPTNS | nvarchar | 510 | 1 |  |  |  |
| APLY_ON_CLMN_FNCTN | bit | 1 | 0 |  |  |  |
| CRTN_DATE | datetime | 8 | 0 |  |  |  |
