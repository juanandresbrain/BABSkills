# dbo.comp_set_style_color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comp_set_id | bigint | 8 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 0 | YES |  |  |
| primary_flag | bit | 1 | 0 |  |  |  |
| pick_sequence_number | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.filter_forecasting_styles_ma_$sp](../../StoredProcedures/ma_01/dbo.filter_forecasting_styles_ma_$sp.md)

