# dbo.CLNDR_LVL_TYPE

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 | YES |  |  |
| CLNDR_LVL_DESC | nvarchar | 510 | 0 |  |  |  |
| CLNDR_LVL_SEQ | T_INTEGER | 2 | 0 |  |  |  |
| TIME_SPAN | T_LONG_INTEGER | 4 | 0 |  |  |  |
| CLNDR_LVL_TYPE_IDNTY | T_INTEGER | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.get_clndr_chld_lbl_$sp](../../StoredProcedures/esell/dbo.get_clndr_chld_lbl_$sp.md)

