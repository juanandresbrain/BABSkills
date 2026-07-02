# dbo.tmp960LockTransfers

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style | varchar | 6 | 1 |  |  |  |
| description | varchar | 52 | 1 |  |  |  |
| orig_qty | int | 4 | 1 |  |  |  |
| abs_qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWcStockAdj.md)
- [me_01: dbo.spMerchandisingSelect960LockTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingSelect960LockTransfers.md)

