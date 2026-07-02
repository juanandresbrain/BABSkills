# dbo.ORG_CHN_HRCHY_LVL_GRP_LANG

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | T_ID | 16 | 0 | YES |  |  |
| LANG_ID | T_INTEGER | 2 | 0 | YES |  |  |
| HRCHY_LVL_GRP_DESC | nvarchar | 510 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_GRPS_IN_SET_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_GRPS_IN_SET_$SP.md)

