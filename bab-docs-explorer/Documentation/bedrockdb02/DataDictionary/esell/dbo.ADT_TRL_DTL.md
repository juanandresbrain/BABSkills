# dbo.ADT_TRL_DTL

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTRY_ID | T_ID | 16 | 0 | YES |  |  |
| SEQ_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| TBL_NAME | nvarchar | 510 | 0 |  |  |  |
| TBL_KEY | nvarchar | 510 | 0 |  |  |  |
| TBL_KEY_RSRC_NAME | nvarchar | 510 | 0 |  |  |  |
| TBL_KEY_RSRC_PRMS | nvarchar | 510 | 0 |  |  |  |
| ACTN_CODE | nvarchar | 8 | 0 |  |  |  |
| CLMN_NAME | nvarchar | 4000 | 1 |  |  |  |
| OLD_VAL | nvarchar | 3000 | 1 |  |  |  |
| NEW_VAL | nvarchar | 3000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

