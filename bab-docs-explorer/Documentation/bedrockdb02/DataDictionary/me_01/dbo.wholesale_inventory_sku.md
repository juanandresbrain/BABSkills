# dbo.wholesale_inventory_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_code | nvarchar | 40 | 0 | YES |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| size_code | nvarchar | 34 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| available_on_hand | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.update_wholesale_inventory_$sp](../../StoredProcedures/me_01/dbo.update_wholesale_inventory_$sp.md)

