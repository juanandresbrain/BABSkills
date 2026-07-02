# dbo.discount

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| discount_id | smallint | 2 | 0 | YES |  |  |
| discount_code | nvarchar | 16 | 0 |  |  |  |
| discount_description | nvarchar | 60 | 0 |  |  |  |
| reflect_in_net_cost_flag | bit | 1 | 0 |  |  |  |
| use_percent_for_discount_flag | bit | 1 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 0 |  |  |  |
| reflect_discount_in_cost_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.rpt_get_po_discounts_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_discounts_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [ma_01: dbo.import_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_group_$sp.md)
- [ma_01: dbo.import_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_style_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)

