# dbo.FNDTN_SL_OBJCT

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OBJCT_ID | int | 4 | 0 |  |  |  |
| TPC_ID | int | 4 | 0 |  |  |  |
| OBJCT_TYPE | smallint | 2 | 0 |  |  |  |
| CRTD_DATE | smalldatetime | 4 | 0 |  |  |  |
| OWNR_ID | int | 4 | 0 |  |  |  |
| MDFD_DATE | datetime | 8 | 1 |  |  |  |
| MDFD_ID | int | 4 | 1 |  |  |  |
| LAST_USED_DATE | smalldatetime | 4 | 1 |  |  |  |
| LAST_USED_ID | int | 4 | 1 |  |  |  |
| OBJCT_DATA | ntext | 16 | 0 |  |  |  |
| OBJCT_CODE | varchar | 30 | 1 |  |  |  |
| BLT_BY_VRSN | varchar | 23 | 1 |  |  |  |
| OBJCT_VRSN | int | 4 | 1 |  |  |  |
| OBJCT_CNTXT | varchar | 30 | 1 |  |  |  |
