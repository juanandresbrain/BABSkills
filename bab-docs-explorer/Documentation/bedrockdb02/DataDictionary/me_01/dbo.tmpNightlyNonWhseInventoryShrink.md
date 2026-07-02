# dbo.tmpNightlyNonWhseInventoryShrink

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| MerchQty | int | 4 | 1 |  |  |  |
| DynQty | int | 4 | 1 |  |  |  |
| shrinkqty | int | 4 | 1 |  |  |  |
| style_type | varchar | 5 | 0 |  |  |  |
| shrinkqty_distribution_multiple | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputnNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingOutputnNonWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched](../../StoredProcedures/me_01/dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched.md)
- [me_01: dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched_bak](../../StoredProcedures/me_01/dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched_bak.md)
- [me_01: dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatchedByLocationCode](../../StoredProcedures/me_01/dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatchedByLocationCode.md)
- [me_01: dbo.spMerchandisingOutputnNonWhseInventoryShrinkByLocationCode](../../StoredProcedures/me_01/dbo.spMerchandisingOutputnNonWhseInventoryShrinkByLocationCode.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829.md)

