# dbo.imp_cd_rim_oh_group_local

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| merch_year_pd | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| rim_on_hand_retail | decimal | 9 | 1 |  |  |  |
| rim_on_hand_cost | decimal | 9 | 1 |  |  |  |
| rim_on_hand_retail_local | decimal | 9 | 0 |  |  |  |
| rim_on_hand_cost_local | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hist_currency_exchange_rate_pd_$sp](../../StoredProcedures/ma_01/dbo.hist_currency_exchange_rate_pd_$sp.md)

