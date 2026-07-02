# dbo.tmpAllocationsAdjUK

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | varchar | 7 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| UPC | varchar | 12 | 1 |  |  |  |
| location_code | varchar | 6 | 1 |  |  |  |
| Adj_qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputUKAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUKAllocAdj.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)

