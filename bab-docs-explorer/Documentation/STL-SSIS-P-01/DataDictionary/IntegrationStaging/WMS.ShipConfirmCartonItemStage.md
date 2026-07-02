# WMS.ShipConfirmCartonItemStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _JSON | nvarchar | -1 | 1 |  |  |  |
| _RowIndex | int | 4 | 1 |  |  |  |
| _ParentKeyField | int | 4 | 1 |  |  |  |
| aptosDistributionDocLineNumber | float | 8 | 1 |  |  |  |
| aptosDistributionNumber | bigint | 8 | 1 |  |  |  |
| containerUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| containerUnitsShipped | float | 8 | 1 |  |  |  |
| itemNumber | nvarchar | 200 | 1 |  |  |  |
| orderedQuantity | float | 8 | 1 |  |  |  |
| orderedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| orderNumber | nvarchar | 200 | 1 |  |  |  |
| shippedQuantity | float | 8 | 1 |  |  |  |
| shippedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| toLocation | nvarchar | 200 | 1 |  |  |  |

