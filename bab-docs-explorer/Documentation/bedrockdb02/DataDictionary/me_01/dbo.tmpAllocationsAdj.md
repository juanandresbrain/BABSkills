# dbo.tmpAllocationsAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_no | varchar | 12 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| upc | varchar | 12 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| adj_qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWCAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWCAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414.md)

