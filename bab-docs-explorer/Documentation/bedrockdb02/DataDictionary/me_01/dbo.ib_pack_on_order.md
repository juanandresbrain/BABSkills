# dbo.ib_pack_on_order

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_pack_on_order_id | decimal | 9 | 0 | YES |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |
| pack_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.on_order_pack_create_modify_$sp](../../StoredProcedures/me_01/dbo.on_order_pack_create_modify_$sp.md)
- [me_01: dbo.on_order_pack_update_$sp](../../StoredProcedures/me_01/dbo.on_order_pack_update_$sp.md)
- [me_01: dbo.on_order_reduction_pack_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pack_$sp.md)
- [me_01: dbo.on_order_reinstate_pack_$sp](../../StoredProcedures/me_01/dbo.on_order_reinstate_pack_$sp.md)

