# dbo.BabEasyMetricsWmsStagingTransformed

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Cube | nvarchar | 8000 | 1 |  |  |  |
| Level | nvarchar | 8000 | 1 |  |  |  |
| StartEndLocationType | nvarchar | 8000 | 1 |  |  |  |
| QuantityUOM | nvarchar | 8000 | 1 |  |  |  |
| Weight | nvarchar | 8000 | 1 |  |  |  |
| ProcessType | nvarchar | 8000 | 1 |  |  |  |
| Site | nvarchar | 8000 | 1 |  |  |  |
| Facility | nvarchar | 8000 | 1 |  |  |  |
| CaseId | nvarchar | 8000 | 1 |  |  |  |
| PalletLpId | nvarchar | 8000 | 1 |  |  |  |
| Directionality | nvarchar | 510 | 1 |  |  |  |
| Employee | nvarchar | 8000 | 1 |  |  |  |
| StartDateTime | datetime | 8 | 1 |  |  |  |
| EndDateTime | datetime | 8 | 1 |  |  |  |
| Units | float | 8 | 1 |  |  |  |
| HandlingMetric | nvarchar | 8000 | 1 |  |  |  |
| Timestamp | datetime | 8 | 1 |  |  |  |
| OrderNumber | nvarchar | 8000 | 1 |  |  |  |
| Sku | nvarchar | 8000 | 1 |  |  |  |
| Quantity | float | 8 | 1 |  |  |  |
| StartLocation | nvarchar | 8000 | 1 |  |  |  |
| EndLocation | nvarchar | 8000 | 1 |  |  |  |
| StartZone | nvarchar | 8000 | 1 |  |  |  |
| EquipmentType | nvarchar | 8000 | 1 |  |  |  |
| TransactionId | nvarchar | 8000 | 1 |  |  |  |
| TransactionSequence | float | 8 | 1 |  |  |  |
| WorklineStatus | varchar | 2 | 0 |  |  |  |
| WorkClass | nvarchar | 8000 | 1 |  |  |  |
| StartLocationProfile | nvarchar | 8000 | 1 |  |  |  |
| EndLocationProfile | nvarchar | 8000 | 1 |  |  |  |
| WorkTemplate | nvarchar | 8000 | 1 |  |  |  |
| EndZone | nvarchar | 8000 | 1 |  |  |  |
| WorkManuallyCompletedBy | nvarchar | 8000 | 1 |  |  |  |
| CustomerAccount | nvarchar | 8000 | 1 |  |  |  |
| OrderDeliveryState | nvarchar | 8000 | 1 |  |  |  |
| FromWarehouse | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spEasyMetricsTransform](../../StoredProcedures/IntegrationStaging/dbo.spEasyMetricsTransform.md)
- [IntegrationStaging: dbo.spEasyMetricsTransform_Bak20231212](../../StoredProcedures/IntegrationStaging/dbo.spEasyMetricsTransform_Bak20231212.md)

