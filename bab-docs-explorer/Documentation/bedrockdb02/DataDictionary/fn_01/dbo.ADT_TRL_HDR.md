# dbo.ADT_TRL_HDR

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTRY_ID | T_ID | 16 | 0 | YES |  |  |
| ENTRY_DATE_TIME | T_DATETIME | 8 | 0 |  |  |  |
| USER_NAME | T_NAME | 50 | 1 |  |  |  |
| USER_ID | numeric | 9 | 1 |  |  |  |
| APP_ID | T_INTEGER | 2 | 0 |  |  |  |
| ROOT_TBL_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| ROOT_TBL_KEY | T_DESCRIPTION | 255 | 1 |  |  |  |
| ROOT_TBL_KEY_RSRC_NAME | T_LONG_DATA | 255 | 1 |  |  |  |
| ROOT_TBL_KEY_RSRC_PRMS | T_DESCRIPTION | 255 | 1 |  |  |  |
| FNCTN_NUM | T_INTEGER | 2 | 1 |  |  |  |
| ADT_CMNT | T_DESCRIPTION | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

