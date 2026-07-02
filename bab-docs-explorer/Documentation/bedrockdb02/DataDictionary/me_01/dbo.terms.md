# dbo.terms

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| terms_id | smallint | 2 | 0 | YES |  |  |
| terms_code | nvarchar | 30 | 0 |  |  |  |
| terms_description | nvarchar | 100 | 0 |  |  |  |
| dating_basis | smallint | 2 | 0 |  |  |  |
| invoice_due_date_months | tinyint | 1 | 0 |  |  |  |
| invoice_due_date_days | smallint | 2 | 0 |  |  |  |
| discount_due_date_months | tinyint | 1 | 0 |  |  |  |
| discount_due_date_days | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.rpt_get_fob_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_fob_BABW_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_terms_$sp](../../StoredProcedures/me_01/dbo.rpt_get_terms_$sp.md)
- [me_01: dbo.rpt_get_unsolicited_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_unsolicited_receipt_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)

