# dbo.CLNDR_MNTH_LANG

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LANG_ID | T_INTEGER | 2 | 0 | YES | YES |  |
| MNTH_NUM | T_SMALL_INTEGER | 1 | 0 | YES |  |  |
| MNTH_LBL | nvarchar | 100 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.get_clndr_chld_lbl_$sp](../../StoredProcedures/esell/dbo.get_clndr_chld_lbl_$sp.md)

