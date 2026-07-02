# dbo.imp_cd_hist_oh_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| price_status_code | nvarchar | 6 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 1 |  |  |  |
| on_hand_retail_local | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hist_currency_exchange_rate_$sp](../../StoredProcedures/ma_01/dbo.hist_currency_exchange_rate_$sp.md)

