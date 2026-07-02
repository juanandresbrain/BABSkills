# dbo.currency

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_id | decimal | 9 | 0 | YES |  |  |
| currency_code | nvarchar | 6 | 0 |  |  |  |
| currency_description | nvarchar | 100 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| currency_symbol | nvarchar | 6 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pocost_valid_styles_$sp](../../StoredProcedures/me_01/dbo.pocost_valid_styles_$sp.md)
- [me_01: dbo.rpt_get_fob_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_fob_BABW_$sp.md)
- [me_01: dbo.rpt_get_lookup_home_currency_$sp](../../StoredProcedures/me_01/dbo.rpt_get_lookup_home_currency_$sp.md)
- [me_01: dbo.rpt_get_lookup_jurisdiction_currency_$sp](../../StoredProcedures/me_01/dbo.rpt_get_lookup_jurisdiction_currency_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.sales_balancing_c$sp](../../StoredProcedures/me_01/dbo.sales_balancing_c$sp.md)
- [me_01: dbo.sales_balancing_l$sp](../../StoredProcedures/me_01/dbo.sales_balancing_l$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spBABW_GoogleGetValidLocationList](../../StoredProcedures/me_01/dbo.spBABW_GoogleGetValidLocationList.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor_BAK_20180305](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor_BAK_20180305.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor_BAK_20180710](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor_BAK_20180710.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingOutputUpdateCNYStyleVendor](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUpdateCNYStyleVendor.md)
- [me_01: dbo.upd_pc_generate_tickets_$sp](../../StoredProcedures/me_01/dbo.upd_pc_generate_tickets_$sp.md)
- [me_01: dbo.validate_pc_generate_tickets_details_$sp](../../StoredProcedures/me_01/dbo.validate_pc_generate_tickets_details_$sp.md)

