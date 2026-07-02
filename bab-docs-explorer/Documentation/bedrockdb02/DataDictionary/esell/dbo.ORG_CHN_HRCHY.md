# dbo.ORG_CHN_HRCHY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_ID | T_ID | 16 | 0 | YES |  |  |
| HRCHY_DESC | nvarchar | 510 | 0 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| DFLT_GRP_ID | T_ID | 16 | 1 |  |  |  |
| SCRTY_USER_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| MTLY_EXCLSV | T_BOOLEAN | 5 | 0 |  |  |  |
| MNDTRY_ASGNMNT | T_BOOLEAN | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_GRPS_IN_SET_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_GRPS_IN_SET_$SP.md)

