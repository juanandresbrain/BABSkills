# dbo.NightlyNonWhseInventoryShrink

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| MerchQty | int | 4 | 1 |  |  |  |
| Whseqty | int | 4 | 1 |  |  |  |
| shrinkqty | int | 4 | 1 |  |  |  |
| style_type | varchar | 5 | 0 |  |  |  |
| shrinkqty_distribution_multiple | int | 4 | 1 |  |  |  |
| sync_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829.md)

