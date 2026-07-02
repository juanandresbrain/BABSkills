# dbo.wholesale_inventory_pack

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_code | nvarchar | 40 | 0 | YES |  |  |
| pack_code | nvarchar | 40 | 0 |  |  |  |
| pack_id | decimal | 9 | 0 | YES |  |  |
| available_on_hand | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.update_wholesale_inventory_$sp](../../StoredProcedures/me_01/dbo.update_wholesale_inventory_$sp.md)

