# WMS.WarehouseOnHand9980

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Arrived | float | 8 | 1 |  |  |  |
| AvailNoWork | int | 4 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| InventLocationId | nvarchar | 8000 | 1 |  |  |  |
| InventSiteId | nvarchar | 8000 | 1 |  |  |  |
| InventStatusId | nvarchar | 8000 | 1 |  |  |  |
| ItemId | nvarchar | 8000 | 1 |  |  |  |
| OnOrder | float | 8 | 1 |  |  |  |
| Ordered | float | 8 | 1 |  |  |  |
| PhysicalInvent | float | 8 | 1 |  |  |  |
| Picked | float | 8 | 1 |  |  |  |
| ReservedNoLocation | int | 4 | 1 |  |  |  |
| ReservOrdered | float | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeWarehouseOnHand9980](../../StoredProcedures/IntegrationStaging/WMS.spMergeWarehouseOnHand9980.md)

