# dbo.imp_id_hist_cmp_sku

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| component_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_sku_$sp.md)

