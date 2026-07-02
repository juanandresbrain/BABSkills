# dbo.Whse_ERD

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| truck_980 | int | 4 | 1 |  |  |  |
| truck_960 | int | 4 | 1 |  |  |  |
| ground_980 | int | 4 | 1 |  |  |  |
| ground_960 | int | 4 | 1 |  |  |  |
| intnl_econ_980 | int | 4 | 1 |  |  |  |
| intnl_econ_960 | int | 4 | 1 |  |  |  |
| supplySecond_980 | int | 4 | 1 |  |  |  |
| supplySecond_960 | int | 4 | 1 |  |  |  |
| supplyThird_980 | int | 4 | 1 |  |  |  |
| supplyThird_960 | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailWarehouseShipmentInformation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailWarehouseShipmentInformation.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)

