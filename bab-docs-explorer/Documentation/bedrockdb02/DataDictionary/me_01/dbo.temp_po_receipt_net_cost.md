# dbo.temp_po_receipt_net_cost

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| pack_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| net_final_cost | decimal | 9 | 0 |  |  |  |
| net_final_cost_local | decimal | 9 | 1 |  |  |  |
| shipped_date | smalldatetime | 4 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)

