# dbo.ORG_CHN_HRCHY_LVL_GRP_SET

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_SET_ID | int | 4 | 0 | YES |  |  |
| GRP_LIST_PREFIX | varchar | 850 | 0 |  |  |  |
| IS_GRP_LIST_PREFIX_CMPLT | bit | 1 | 0 |  |  |  |
| MBR_COUNT | smallint | 2 | 0 |  |  |  |
| LARGEST_GRP_SET_ID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.SCRTY_CHK_IS_SUBSET_PRPR_$SP](../../StoredProcedures/esell/dbo.SCRTY_CHK_IS_SUBSET_PRPR_$SP.md)
- [esell: dbo.SCRTY_GET_CMPLMNT_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_CMPLMNT_SET_ID_$SP.md)
- [esell: dbo.SCRTY_GET_INTRSCT_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_INTRSCT_SET_ID_$SP.md)
- [esell: dbo.SCRTY_GET_SET_FMLY_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_SET_FMLY_ID_$SP.md)
- [esell: dbo.SCRTY_GET_SET_ID_$SP](../../StoredProcedures/esell/dbo.SCRTY_GET_SET_ID_$SP.md)
- [esell: dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP](../../StoredProcedures/esell/dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP.md)
- [esell: dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP](../../StoredProcedures/esell/dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP.md)
- [esell: dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP](../../StoredProcedures/esell/dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP.md)

