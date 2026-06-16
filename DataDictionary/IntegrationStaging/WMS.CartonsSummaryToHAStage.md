# WMS.CartonsSummaryToHAStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipmentId | nvarchar | 200 | 1 |  |  |  |
| deliveryName | nvarchar | 200 | 1 |  |  |  |
| street | nvarchar | 400 | 1 |  |  |  |
| city | nvarchar | 200 | 1 |  |  |  |
| state | nvarchar | 200 | 1 |  |  |  |
| zip | nvarchar | 200 | 1 |  |  |  |
| country | nvarchar | 200 | 1 |  |  |  |
| shipCarrier | nvarchar | 200 | 1 |  |  |  |
| modeOfDelivery | nvarchar | 200 | 1 |  |  |  |
| waveId | nvarchar | 200 | 1 |  |  |  |
| containerId | nvarchar | 200 | 1 |  |  |  |
| grossWeight | float | 8 | 1 |  |  |  |
| length | float | 8 | 1 |  |  |  |
| width | float | 8 | 1 |  |  |  |
| height | float | 8 | 1 |  |  |  |
| shipTo | nvarchar | 200 | 1 |  |  |  |
| warehouse | nvarchar | 200 | 1 |  |  |  |
| description | nvarchar | 200 | 1 |  |  |  |
| deliveryDescription | nvarchar | 200 | 1 |  |  |  |
| totalQuantityContainer | nvarchar | 510 | 1 |  |  |  |
| itemNumber | nvarchar | 200 | 1 |  |  |  |
| totalQuantity | nvarchar | 510 | 1 |  |  |  |
| OrderNumber | nvarchar | 50 | 1 |  |  |  |
| CustomerAccount | nvarchar | 50 | 1 |  |  |  |
| MessageDateUTC | datetime | 8 | 1 |  |  |  |
| AptosDistroNumber | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeCartonsSummaryToHA](../../StoredProcedures/IntegrationStaging/WMS.spMergeCartonsSummaryToHA.md)

