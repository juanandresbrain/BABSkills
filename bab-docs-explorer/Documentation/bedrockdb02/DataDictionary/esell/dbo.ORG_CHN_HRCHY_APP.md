# dbo.ORG_CHN_HRCHY_APP

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| APP_ID | smallint | 2 | 0 | YES |  |  |
| DVSN_HRCHY_LVL_ID | T_ID | 16 | 1 |  |  |  |
| RPRT_HRCHY_ID | T_ID | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_GRPS_IN_SET_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_GRPS_IN_SET_$SP.md)
- [esell: dbo.SCRTY_GET_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_SET_ID_$SP.md)

