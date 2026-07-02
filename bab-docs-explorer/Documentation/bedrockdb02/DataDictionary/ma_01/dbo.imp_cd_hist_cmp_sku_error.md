# dbo.imp_cd_hist_cmp_sku_error

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| error_id | smallint | 2 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| price_status_code | nvarchar | 6 | 1 |  |  |  |
| transaction_reason_code | nvarchar | 30 | 1 |  |  |  |
| row_text | nvarchar | 1000 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_sku_$sp.md)

