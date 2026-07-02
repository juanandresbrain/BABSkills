# dbo.temp_po_receipt_activity_date

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| state_no | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_complete_$sp](../../StoredProcedures/me_01/dbo.import_asn_complete_$sp.md)
- [me_01: dbo.import_asn_fifth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_fifth_step_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)

