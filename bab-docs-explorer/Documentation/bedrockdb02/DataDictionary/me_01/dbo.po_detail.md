# dbo.po_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_detail_id | int | 4 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| po_location_id | smallint | 2 | 0 |  |  |  |
| total_ordered_pseudo_cost | decimal | 9 | 1 |  |  |  |
| total_ordered_pseudo_retail | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  | YES |  |
| pack_id | decimal | 9 | 1 |  | YES |  |
| ordered_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.get_po_detail_retail_rep_$sp](../../StoredProcedures/me_01/dbo.get_po_detail_retail_rep_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.pom_check_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_check_released_units_$sp.md)
- [me_01: dbo.rpt_get_pending_send_edi_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pending_send_edi_pos_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_01042018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_01042018.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_BAK_02272018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_BAK_02272018.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

