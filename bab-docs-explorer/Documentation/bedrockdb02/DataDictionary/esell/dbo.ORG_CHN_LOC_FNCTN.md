# dbo.ORG_CHN_LOC_FNCTN

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FNCTN_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| FNCTN_DESC | nvarchar | 510 | 0 |  |  |  |
| FNCTN_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| SYS_CODE | nvarchar | 8 | 0 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

