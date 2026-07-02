# dbo.il_vendor_inventory_temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| il_vendor_inventory_temp_id | decimal | 9 | 0 | YES |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| available_units | int | 4 | 0 |  |  |  |

