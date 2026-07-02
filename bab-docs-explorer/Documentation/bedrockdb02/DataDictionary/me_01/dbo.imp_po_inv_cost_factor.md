# dbo.imp_po_inv_cost_factor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_number | nvarchar | 40 | 0 | YES |  |  |
| po_line_number | decimal | 9 | 0 | YES |  |  |
| shipment_number | nvarchar | 40 | 0 | YES |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| cost_factor_code | nvarchar | 30 | 0 | YES |  |  |
| total_cost_factor_amount | decimal | 9 | 0 |  |  |  |
| quantity_invoiced | int | 4 | 0 |  |  |  |
| unit_cost | decimal | 9 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)

