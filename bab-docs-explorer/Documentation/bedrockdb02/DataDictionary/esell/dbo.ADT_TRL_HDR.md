# dbo.ADT_TRL_HDR

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTRY_ID | T_ID | 16 | 0 | YES |  |  |
| ENTRY_DATE_TIME | T_DATETIME | 8 | 0 |  |  |  |
| USER_NAME | nvarchar | 100 | 1 |  |  |  |
| USER_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| APP_ID | T_INTEGER | 2 | 0 |  |  |  |
| ROOT_TBL_NAME | nvarchar | 510 | 0 |  |  |  |
| ROOT_TBL_KEY | nvarchar | 510 | 1 |  |  |  |
| ROOT_TBL_KEY_RSRC_NAME | nvarchar | 510 | 1 |  |  |  |
| ROOT_TBL_KEY_RSRC_PRMS | nvarchar | 510 | 1 |  |  |  |
| FNCTN_NUM | T_INTEGER | 2 | 1 |  |  |  |
| ADT_CMNT | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

