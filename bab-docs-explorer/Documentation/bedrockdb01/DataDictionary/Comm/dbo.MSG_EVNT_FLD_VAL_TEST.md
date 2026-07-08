# dbo.MSG_EVNT_FLD_VAL_TEST

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MSG_ID | int | 4 | 0 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| EVNT_FLD_ID | int | 4 | 0 |  |  |  |
| GRP_SEQ | smallint | 2 | 0 |  |  |  |
| TEST_SEQ | int | 4 | 0 |  |  |  |
| DATA_SRC | int | 4 | 0 |  |  |  |
| FLD_ID | int | 4 | 1 |  |  |  |
| INTRNL_TYPE | int | 4 | 1 |  |  |  |
| OPRTR | varchar | 2 | 0 |  |  |  |
| FLD_VAL | nvarchar | 50 | 0 |  |  |  |
| EXPRSN_OPRTR | varchar | 3 | 1 |  |  |  |
| LAST_MDFD | datetime | 8 | 0 |  |  |  |
| ROW_ID | int | 4 | 0 | YES |  |  |
