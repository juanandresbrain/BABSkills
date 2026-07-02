# dbo.SCRTY_ACS_HRCHY_LVL_GRP_SET

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ACS_ID | numeric | 9 | 0 | YES |  |  |
| ACS_ID_TYPE | tinyint | 1 | 0 | YES |  |  |
| HRCHY_LVL_GRP_SET_ID | int | 4 | 0 | YES | YES |  |
| ACTV | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_USER_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_USER_SET_ID_$SP.md)

