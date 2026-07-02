# dbo.ERP_InventoryAdjustmentLog

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AdjustmentID | int | 4 | 0 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| Style | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| Description | varchar | 52 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingImportCNInvAdj](../../StoredProcedures/me_01/dbo.spMerchandisingImportCNInvAdj.md)
- [me_01: dbo.spMerchandisingImportCNInvAdj_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingImportCNInvAdj_Bak20210614.md)
- [me_01: dbo.spMerchandisingProcessWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWcStockAdj.md)
- [me_01: dbo.spUKStockAdjustment](../../StoredProcedures/me_01/dbo.spUKStockAdjustment.md)

