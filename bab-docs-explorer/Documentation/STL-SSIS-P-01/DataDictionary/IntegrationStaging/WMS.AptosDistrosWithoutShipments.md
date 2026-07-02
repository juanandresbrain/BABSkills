# WMS.AptosDistrosWithoutShipments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABAptosShipmentNumber | varchar | 20 | 1 |  |  |  |
| BABAptosDistroNumber | varchar | 20 | 1 |  |  |  |
| BABAptosDistroLineNumber | int | 4 | 1 |  |  |  |
| ToWarehouse | varchar | 4 | 1 |  |  |  |
| ItemNumber | varchar | 7 | 1 |  |  |  |
| APISuccess | int | 4 | 1 |  |  |  |
| DynamicsOrder | varchar | 52 | 1 |  |  |  |
| DynamicsShipmentLogged | varchar | 3 | 1 |  |  |  |
| DistroShipmentStageDate | datetime | 8 | 1 |  |  |  |
| ShipmentStageDate | datetime | 8 | 1 |  |  |  |
| AptosShipmentDistroItemLogged | nvarchar | 6 | 1 |  |  |  |
| AptosShipmentLogged | nvarchar | 6 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailDistrosVsShipmentsValidation](../../StoredProcedures/IntegrationStaging/WMS.spEmailDistrosVsShipmentsValidation.md)

