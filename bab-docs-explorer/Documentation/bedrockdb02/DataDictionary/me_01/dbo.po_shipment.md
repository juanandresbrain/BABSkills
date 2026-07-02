# dbo.po_shipment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| estimated_shipment_percent | decimal | 5 | 1 |  |  |  |
| sourcing_line_ship_id | int | 4 | 1 |  |  |  |
| sourcing_line_number | int | 4 | 1 |  |  |  |
| storepack_defn_released_flag | bit | 1 | 0 |  |  |  |
| country_id | decimal | 9 | 1 |  | YES |  |
| carrier_id | smallint | 2 | 1 |  | YES |  |
| ship_via_id | smallint | 2 | 1 |  | YES |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_po_detail_retail_rep_$sp](../../StoredProcedures/me_01/dbo.get_po_detail_retail_rep_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.on_order_reduction_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_$sp.md)
- [me_01: dbo.on_order_reduction_pack_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pack_$sp.md)
- [me_01: dbo.on_order_reduction_pseudo_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pseudo_$sp.md)
- [me_01: dbo.rpt_get_po_shipments_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_shipments_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.set_delivery_dates_$sp](../../StoredProcedures/me_01/dbo.set_delivery_dates_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)

