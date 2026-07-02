# dbo.po_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_discount_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| discount_id | smallint | 2 | 0 |  | YES |  |
| pct_amt | smallint | 2 | 0 |  |  |  |
| discount_value | float | 8 | 0 |  |  |  |
| calculate_on | smallint | 2 | 0 |  |  |  |
| reflect_in_discount_cost_flag | bit | 1 | 0 |  |  |  |
| subject_to_terms_flag | bit | 1 | 0 |  |  |  |
| sequence | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.rpt_get_po_discounts_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_discounts_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)

