# ERP.DistributionHeader

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PICKLISTID | varchar | 20 | 1 |  |  |  |
| CustAccount | varchar | 50 | 1 |  |  |  |
| CUSTOMERREQUISITIONID | varchar | 50 | 1 |  |  |  |
| DELIVERYTERM | varchar | 200 | 1 |  |  |  |
| FROMWAREHOUSE | varchar | 5 | 1 |  |  |  |
| MODEOFDELIVERY | varchar | 10 | 1 |  |  |  |
| ORDERID | varchar | 20 | 1 |  |  |  |
| ORDERTYPE | varchar | 20 | 1 |  |  |  |
| SHIPTONAME | varchar | 100 | 1 |  |  |  |
| TOWAREHOUSE | varchar | 5 | 1 |  |  |  |
| TRANSACTIONDATETIME | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ReleaseDate | datetime | 8 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| OrderCreateSource | varchar | 10 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)

