# WMS.DynamicsContainer

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABStoreNumber | varchar | 4 | 1 |  |  |  |
| ContainerId | varchar | 50 | 1 |  |  |  |
| dataAreaId | varchar | 4 | 1 |  |  |  |
| DeliveryName | nvarchar | 8000 | 1 |  |  |  |
| Height | float | 8 | 1 |  |  |  |
| ItemId | varchar | 6 | 1 |  |  |  |
| Length | float | 8 | 1 |  |  |  |
| LicensePlateId | nvarchar | 200 | 1 |  |  |  |
| Qty | float | 8 | 1 |  |  |  |
| ShipmentId | nvarchar | 100 | 1 |  |  |  |
| Weight | float | 8 | 1 |  |  |  |
| WHSShipmentTable_Address | nvarchar | 8000 | 1 |  |  |  |
| WHSShipmentTable_ShipConfirmUTCDateTime | datetime | 8 | 1 |  |  |  |
| WHSShipmentTable_WaveId | nvarchar | 100 | 1 |  |  |  |
| Width | float | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDynamicsContainer](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsContainer.md)

