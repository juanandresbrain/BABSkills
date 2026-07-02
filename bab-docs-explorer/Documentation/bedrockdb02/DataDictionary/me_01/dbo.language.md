# dbo.language

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| language_id | int | 4 | 0 | YES |  |  |
| parameter_system_id | tinyint | 1 | 0 |  |  |  |
| locale_identifier | smallint | 2 | 0 |  |  |  |
| locale_description | nvarchar | 60 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| default_desc_language_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.plu_crs_temp_output_$sp](../../StoredProcedures/me_01/dbo.plu_crs_temp_output_$sp.md)
- [me_01: dbo.plu_desc_$sp](../../StoredProcedures/me_01/dbo.plu_desc_$sp.md)
- [USICOAL: dbo.DC_INS_EQUAL_TAX_ZONE_LANG](../../StoredProcedures/USICOAL/dbo.DC_INS_EQUAL_TAX_ZONE_LANG.md)
- [USICOAL: dbo.DC_INS_TAX_AUTHORITY_LANG](../../StoredProcedures/USICOAL/dbo.DC_INS_TAX_AUTHORITY_LANG.md)
- [USICOAL: dbo.DC_INS_TAX_RULE_LANG](../../StoredProcedures/USICOAL/dbo.DC_INS_TAX_RULE_LANG.md)
- [USICOAL: dbo.DC_INS_TAXABLE_ITEM_GRP_LANG](../../StoredProcedures/USICOAL/dbo.DC_INS_TAXABLE_ITEM_GRP_LANG.md)
- [USICOAL: dbo.DC_INS_VALUE_ADDED_TAX_LANG](../../StoredProcedures/USICOAL/dbo.DC_INS_VALUE_ADDED_TAX_LANG.md)
- [USICOAL: dbo.DC_INSUPD_EQUAL_TAX_ZONE_LANG](../../StoredProcedures/USICOAL/dbo.DC_INSUPD_EQUAL_TAX_ZONE_LANG.md)
- [USICOAL: dbo.DC_INSUPD_TAX_AUTHORITY_LANG](../../StoredProcedures/USICOAL/dbo.DC_INSUPD_TAX_AUTHORITY_LANG.md)
- [USICOAL: dbo.DC_INSUPD_TAX_RULE_LANG](../../StoredProcedures/USICOAL/dbo.DC_INSUPD_TAX_RULE_LANG.md)
- [USICOAL: dbo.DC_INSUPD_TAXABLE_ITEM_GRP_LANG](../../StoredProcedures/USICOAL/dbo.DC_INSUPD_TAXABLE_ITEM_GRP_LANG.md)
- [USICOAL: dbo.DC_INSUPD_VALUE_ADDED_TAX_LANG](../../StoredProcedures/USICOAL/dbo.DC_INSUPD_VALUE_ADDED_TAX_LANG.md)
- [USICOAL: dbo.DC_RPL_EQUAL_TAX_ZONE_LANG](../../StoredProcedures/USICOAL/dbo.DC_RPL_EQUAL_TAX_ZONE_LANG.md)
- [USICOAL: dbo.DC_RPL_TAX_AUTHORITY_LANG](../../StoredProcedures/USICOAL/dbo.DC_RPL_TAX_AUTHORITY_LANG.md)
- [USICOAL: dbo.DC_RPL_TAX_RULE_LANG](../../StoredProcedures/USICOAL/dbo.DC_RPL_TAX_RULE_LANG.md)
- [USICOAL: dbo.DC_RPL_TAXABLE_ITEM_GRP_LANG](../../StoredProcedures/USICOAL/dbo.DC_RPL_TAXABLE_ITEM_GRP_LANG.md)
- [USICOAL: dbo.DC_RPL_VALUE_ADDED_TAX_LANG](../../StoredProcedures/USICOAL/dbo.DC_RPL_VALUE_ADDED_TAX_LANG.md)
- [USICOAL: dbo.DC_UPD_EQUAL_TAX_ZONE_LANG](../../StoredProcedures/USICOAL/dbo.DC_UPD_EQUAL_TAX_ZONE_LANG.md)
- [USICOAL: dbo.DC_UPD_TAX_AUTHORITY_LANG](../../StoredProcedures/USICOAL/dbo.DC_UPD_TAX_AUTHORITY_LANG.md)
- [USICOAL: dbo.DC_UPD_TAX_RULE_LANG](../../StoredProcedures/USICOAL/dbo.DC_UPD_TAX_RULE_LANG.md)
- [USICOAL: dbo.DC_UPD_TAXABLE_ITEM_GRP_LANG](../../StoredProcedures/USICOAL/dbo.DC_UPD_TAXABLE_ITEM_GRP_LANG.md)
- [USICOAL: dbo.DC_UPD_VALUE_ADDED_TAX_LANG](../../StoredProcedures/USICOAL/dbo.DC_UPD_VALUE_ADDED_TAX_LANG.md)

