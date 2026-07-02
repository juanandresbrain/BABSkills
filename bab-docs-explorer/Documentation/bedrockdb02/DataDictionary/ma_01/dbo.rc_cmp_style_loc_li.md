# dbo.rc_cmp_style_loc_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| component_type_code | smallint | 2 | 0 | YES |  |  |
| history_component_id | smallint | 2 | 0 | YES |  |  |
| component_units | int | 4 | 1 |  |  |  |
| component_retail | decimal | 9 | 1 |  |  |  |
| component_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| component_cost | decimal | 9 | 1 |  |  |  |
| component_retail_te | decimal | 9 | 1 |  |  |  |
| component_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| component_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.reclass_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_cmp_$sp.md)

