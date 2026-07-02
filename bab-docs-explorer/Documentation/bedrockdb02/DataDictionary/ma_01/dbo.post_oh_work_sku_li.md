# dbo.post_oh_work_sku_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_sku_$sp.md)
- [ma_01: dbo.post_oh_work_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_sku_$sp.md)

