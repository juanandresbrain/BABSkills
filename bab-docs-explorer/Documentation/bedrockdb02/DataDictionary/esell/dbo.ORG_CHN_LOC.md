# dbo.ORG_CHN_LOC

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LOC_ID | T_ID | 16 | 0 | YES |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  | YES |  |
| LOC_DESC | nvarchar | 510 | 0 |  |  |  |
| PHYSCL_CYCL_CNT_IN_PRGRS | T_BOOLEAN | 5 | 0 |  |  |  |
| SLNG_AREA | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| NON_SLNG_AREA | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| AREA_SIZE | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| LNR_SIZE | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| VLM_SIZE | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| SCRTY_CLS_CODE | nchar | 8 | 1 |  |  |  |
| LNR_MSR_CODE | nchar | 8 | 1 |  |  |  |
| AREA_MSR_CODE | nchar | 8 | 1 |  |  |  |
| VLM_MSR_CODE | nchar | 8 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

