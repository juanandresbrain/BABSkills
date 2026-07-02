# dbo.dist_min_max_profile

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_min_max_profile_id | bigint | 8 | 0 | YES |  |  |
| dist_detail_id | bigint | 8 | 0 |  |  |  |
| minimum | int | 4 | 1 |  |  |  |
| maximum | int | 4 | 1 |  |  |  |
| presentation_stock | int | 4 | 1 |  |  |  |
| capacity_maximum | int | 4 | 1 |  |  |  |
| order_point | tinyint | 1 | 0 |  |  |  |
| incl_pres_stock_with_ord_pt_fl | bit | 1 | 0 |  |  |  |
| on_hand_units | int | 4 | 1 |  |  |  |
| in_transit_units | int | 4 | 1 |  |  |  |
| allocated_units | int | 4 | 1 |  |  |  |
| on_order_units | int | 4 | 1 |  |  |  |
| original_suggested_quantity | int | 4 | 1 |  |  |  |
| adjusted_quantity | int | 4 | 1 |  |  |  |
| short_shipped_quantity | int | 4 | 1 |  |  |  |
| future_inventory_reserve_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

