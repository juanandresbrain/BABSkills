# dbo.post_flsh_group_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_retail | decimal | 9 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| transaction_retail_te | decimal | 9 | 1 |  |  |  |
| transaction_selling_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_reclass_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_reclass_hist_flsh_$sp.md)

