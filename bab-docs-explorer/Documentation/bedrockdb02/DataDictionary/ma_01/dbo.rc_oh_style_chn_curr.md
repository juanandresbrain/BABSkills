# dbo.rc_oh_style_chn_curr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| on_hand_units | int | 4 | 1 |  |  |  |
| on_hand_retail | decimal | 9 | 1 |  |  |  |
| on_hand_cost | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.reclass_oh_post_adjust_cmp_$sp](../../StoredProcedures/ma_01/dbo.reclass_oh_post_adjust_cmp_$sp.md)

