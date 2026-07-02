# dbo.tblNightlyStoreInventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| sku_desc | varchar | 100 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| load_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829.md)

