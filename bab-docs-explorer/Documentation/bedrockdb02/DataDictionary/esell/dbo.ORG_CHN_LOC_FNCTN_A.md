# dbo.ORG_CHN_LOC_FNCTN_A

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LOC_ID | T_ID | 16 | 0 | YES | YES |  |
| FNCTN_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| PRMRY_LOC_FNCTN_A | T_BOOLEAN | 5 | 0 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

