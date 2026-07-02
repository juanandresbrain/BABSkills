# dbo.ib_on_order

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_on_order_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| on_order_valuation_retail | decimal | 9 | 0 |  |  |  |
| on_order_selling_retail | decimal | 9 | 0 |  |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |
| actual_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| received_quantity | int | 4 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| po_shipment_id | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.ins_ib_on_order_post_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_on_order_post_pc_$sp.md)
- [me_01: dbo.insert_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.insert_ib_on_order_$sp.md)
- [me_01: dbo.on_order_cancel_$sp](../../StoredProcedures/me_01/dbo.on_order_cancel_$sp.md)
- [me_01: dbo.on_order_insert_work_data_$sp](../../StoredProcedures/me_01/dbo.on_order_insert_work_data_$sp.md)
- [me_01: dbo.on_order_pack_create_modify_$sp](../../StoredProcedures/me_01/dbo.on_order_pack_create_modify_$sp.md)
- [me_01: dbo.on_order_reduction_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_$sp.md)
- [me_01: dbo.on_order_reduction_pseudo_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pseudo_$sp.md)
- [me_01: dbo.on_order_reinstate_$sp](../../StoredProcedures/me_01/dbo.on_order_reinstate_$sp.md)
- [me_01: dbo.on_order_update_$sp](../../StoredProcedures/me_01/dbo.on_order_update_$sp.md)
- [me_01: dbo.oo_cleanup_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_cleanup_notax_retails_$sp.md)
- [me_01: dbo.oo_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_populate_notax_retails_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [me_01: dbo.spMerchandisingReportStoreSkinReview](../../StoredProcedures/me_01/dbo.spMerchandisingReportStoreSkinReview.md)
- [me_01: dbo.startup_discrepancy_ib_oo_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_oo_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)

