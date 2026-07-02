# dbo.post_oh_work_styleclr_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| merch_year | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 1 |  |  |  |
| on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_oh_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_styleclr_$sp.md)
- [ma_01: dbo.post_oh_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_styleclr_$sp.md)

