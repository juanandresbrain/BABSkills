# dbo.MSG_EVNT_FLD_VAL

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MSG_ID | int | 4 | 0 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| EVNT_FLD_ID | int | 4 | 0 |  |  |  |
| GRP_SEQ | smallint | 2 | 0 |  |  |  |
| EVNT_FLD_DATA_TYPE | tinyint | 1 | 0 |  |  |  |
| FLD_LNGTH | smallint | 2 | 1 |  |  |  |
| DATA_SRC | int | 4 | 0 |  |  |  |
| FLD_ID | int | 4 | 1 |  |  |  |
| INTRNL_TYPE | int | 4 | 1 |  |  |  |
| CNSTNT_VAL | nvarchar | 200 | 1 |  |  |  |
| LAST_MDFD | datetime | 8 | 0 |  |  |  |
| ROW_ID | int | 4 | 0 | YES |  |  |
