# dbo.webstore_inventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STYLE | varchar | 10 | 1 |  |  |  |
| SKU_DESC | varchar | 35 | 1 |  |  |  |
| AVAILABLE | decimal | 17 | 1 |  |  |  |
| load_date | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportWebstoreInventory](../../StoredProcedures/me_01/dbo.spMerchandisingReportWebstoreInventory.md)

