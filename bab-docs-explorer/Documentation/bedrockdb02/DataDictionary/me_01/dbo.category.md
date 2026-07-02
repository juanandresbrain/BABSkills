# dbo.category

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| category_id | decimal | 9 | 0 | YES |  |  |
| category_code | nvarchar | 40 | 0 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| category_description | nvarchar | 120 | 0 |  |  |  |
| price_change_type | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| override_flag | bit | 1 | 0 |  |  |  |
| override_price_status_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [USICOAL: dbo.DC_CHK_ITM_REF_INTGR](../../StoredProcedures/USICOAL/dbo.DC_CHK_ITM_REF_INTGR.md)
- [USICOAL: dbo.DC_INS_ITEM](../../StoredProcedures/USICOAL/dbo.DC_INS_ITEM.md)
- [USICOAL: dbo.DC_RPL_ITEM](../../StoredProcedures/USICOAL/dbo.DC_RPL_ITEM.md)
- [USICOAL: dbo.DC_RPL_PLU](../../StoredProcedures/USICOAL/dbo.DC_RPL_PLU.md)
- [USICOAL: dbo.DC_UPD_ITEM](../../StoredProcedures/USICOAL/dbo.DC_UPD_ITEM.md)

