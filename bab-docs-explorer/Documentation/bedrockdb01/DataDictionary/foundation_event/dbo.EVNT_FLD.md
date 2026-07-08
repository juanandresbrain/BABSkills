# dbo.EVNT_FLD

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_FLD_ID | T_INTEGER | 2 | 0 | YES |  |  |
| EVNT_FLD_NAME_RSRC | T_LONG_DATA | 255 | 1 |  |  |  |
| EVNT_FLD_DSCRPTN_RSRC | T_LONG_DATA | 255 | 0 |  |  |  |
| EVNT_FLD_DATA_TYPE | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| DATA_NMRC_UNIT_RSRC | T_LONG_DATA | 255 | 1 |  |  |  |
| DATA_FRMT | T_ALPHANUMERIC_TOKEN | 30 | 1 |  |  |  |
| FLD_LNGTH | T_INTEGER | 2 | 1 |  |  |  |
| IS_VAL_LIST | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| VLDTN_VAL_LIST | nvarchar | 510 | 1 |  |  |  |
| DSPLY_SQL_STMNT | T_LONG_DATA | 255 | 1 |  |  |  |
| ENCRPTN_INFO | T_LONG_DATA | 255 | 1 |  |  |  |
