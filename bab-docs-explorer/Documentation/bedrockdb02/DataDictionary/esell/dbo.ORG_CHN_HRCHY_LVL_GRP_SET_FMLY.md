# dbo.ORG_CHN_HRCHY_LVL_GRP_SET_FMLY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_SET_FMLY_ID | int | 4 | 0 | YES |  |  |
| SET_LIST_PREFIX | varchar | 850 | 0 |  |  |  |
| IS_SET_LIST_PREFIX_CMPLT | bit | 1 | 0 |  |  |  |
| MBR_COUNT | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_GET_SET_FMLY_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_SET_FMLY_ID_$SP.md)
- [esell: dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP](../../StoredProcedures/esell/dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP.md)

