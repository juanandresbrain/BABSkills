# dbo.reservation_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reservation_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| quantity | int | 4 | 0 |  |  |  |
| quantity_done | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.update_reservation_details_$sp](../../StoredProcedures/me_01/dbo.update_reservation_details_$sp.md)

