# dbo.po_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_location_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  | YES |  |
| pricing_exchange_rate | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_po_detail_retail_rep_$sp](../../StoredProcedures/me_01/dbo.get_po_detail_retail_rep_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.pom_check_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_check_released_units_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_01042018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_01042018.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_BAK_02272018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_BAK_02272018.md)
- [me_01: dbo.sp_keith_ib_audit_trail](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail.md)
- [me_01: dbo.sp_keith_ib_audit_trailBACKU20150511](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBACKU20150511.md)
- [me_01: dbo.sp_keith_ib_audit_trailBAK20220801](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBAK20220801.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

