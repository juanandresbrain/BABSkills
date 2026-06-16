# WMS.DynamicsAverageCost

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 8 | 1 |  |  |  |
| InventSiteId | nvarchar | 8 | 1 |  |  |  |
| InventLocationId | nvarchar | 8 | 1 |  |  |  |
| ItemId | nvarchar | 8000 | 1 |  |  |  |
| ItemName | nvarchar | 8000 | 1 |  |  |  |
| ItemPropertyId | nvarchar | 8000 | 1 |  |  |  |
| PostedQty | numeric | 17 | 1 |  |  |  |
| PostedValue | numeric | 17 | 1 |  |  |  |
| AverageCost | numeric | 17 | 1 |  |  |  |
| AverageCostRounded | numeric | 17 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.WMS.[spMergeDynamicsAverageCost](../../StoredProcedures/IntegrationStaging/dbo_WMS._spMergeDynamicsAverageCost.md)
- [IntegrationStaging: WMS.spMergeDynamicsAverageCost](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsAverageCost.md)

