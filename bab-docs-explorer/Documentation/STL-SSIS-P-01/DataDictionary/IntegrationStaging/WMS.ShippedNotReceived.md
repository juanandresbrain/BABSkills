# WMS.ShippedNotReceived

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | nvarchar | 200 | 1 |  |  |  |
| OrderStatus | nvarchar | 200 | 1 |  |  |  |
| FromWarehouse | nvarchar | 200 | 1 |  |  |  |
| ToWarehouse | nvarchar | 200 | 1 |  |  |  |
| Receipt Date | date | 3 | 1 |  |  |  |
| ModeOfDelivery | nvarchar | 200 | 1 |  |  |  |
| AptosShipmentNumber | nvarchar | 200 | 1 |  |  |  |
| QuantityShipped | float | 8 | 1 |  |  |  |
| QuantityReceived | float | 8 | 1 |  |  |  |
| QuantityNotReceived | float | 8 | 1 |  |  |  |
| DistrictName | nvarchar | 200 | 1 |  |  |  |
| DistrictManager | nvarchar | 200 | 1 |  |  |  |
| DmId | int | 4 | 1 |  |  |  |
| DMfirstName | nvarchar | 200 | 1 |  |  |  |
| DMlastName | nvarchar | 200 | 1 |  |  |  |
| TMfirstName | nvarchar | 200 | 1 |  |  |  |
| TMlastName | nvarchar | 200 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spShippedNotReceivedReport](../../StoredProcedures/IntegrationStaging/WMS.spShippedNotReceivedReport.md)
- [IntegrationStaging: WMS.spShippedNotReceivedReportPrep](../../StoredProcedures/IntegrationStaging/WMS.spShippedNotReceivedReportPrep.md)

