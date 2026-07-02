# dbo.qty_convert

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style | varchar | 6 | 1 |  |  |  |
| description | varchar | 52 | 1 |  |  |  |
| orig_qty | int | 4 | 1 |  |  |  |
| converted_qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWcStockAdj.md)
- [me_01: dbo.spMerchandisingSelectWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWcStockAdj.md)
- [me_01: dbo.spUKStockAdjustment](../../StoredProcedures/me_01/dbo.spUKStockAdjustment.md)
- [me_01: dbo.spUKStockAdjustment_FileExport](../../StoredProcedures/me_01/dbo.spUKStockAdjustment_FileExport.md)

