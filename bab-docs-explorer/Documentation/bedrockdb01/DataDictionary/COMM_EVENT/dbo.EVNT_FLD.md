# dbo.EVNT_FLD

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_FLD_ID | smallint | 2 | 0 | YES |  |  |
| EVNT_FLD_NAME_RSRC | nvarchar | 510 | 1 |  |  |  |
| EVNT_FLD_DSCRPTN_RSRC | nvarchar | 510 | 0 |  |  |  |
| EVNT_FLD_DATA_TYPE | tinyint | 1 | 0 |  |  |  |
| DATA_NMRC_UNIT_RSRC | nvarchar | 510 | 1 |  |  |  |
| DATA_FRMT | nvarchar | 60 | 1 |  |  |  |
| FLD_LNGTH | smallint | 2 | 1 |  |  |  |
| IS_VAL_LIST | tinyint | 1 | 0 |  |  |  |
| VLDTN_VAL_LIST | nvarchar | 510 | 1 |  |  |  |
| DSPLY_SQL_STMNT | nvarchar | 510 | 1 |  |  |  |
| ENCRPTN_INFO | nvarchar | 510 | 1 |  |  |  |
