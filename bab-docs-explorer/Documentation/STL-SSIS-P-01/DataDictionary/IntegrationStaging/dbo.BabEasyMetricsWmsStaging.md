# dbo.BabEasyMetricsWmsStaging

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AccountNum | nvarchar | 8000 | 1 |  |  |  |
| CreatedDateTimeWorkLine | datetime | 8 | 1 |  |  |  |
| Cube | nvarchar | 8000 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| InventLocationIdFrom | nvarchar | 8000 | 1 |  |  |  |
| InventLocationIdTo | nvarchar | 8000 | 1 |  |  |  |
| InventQtyWork | float | 8 | 1 |  |  |  |
| ItemId | nvarchar | 8000 | 1 |  |  |  |
| Level | nvarchar | 8000 | 1 |  |  |  |
| LineNum | float | 8 | 1 |  |  |  |
| LocProfileId | nvarchar | 8000 | 1 |  |  |  |
| LocType | nvarchar | 8000 | 1 |  |  |  |
| OrderNum | nvarchar | 8000 | 1 |  |  |  |
| ProcessType | nvarchar | 8000 | 1 |  |  |  |
| QtyWork | float | 8 | 1 |  |  |  |
| State | nvarchar | 8000 | 1 |  |  |  |
| UnitId | nvarchar | 8000 | 1 |  |  |  |
| UserId | nvarchar | 8000 | 1 |  |  |  |
| Weight | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_ContainerId | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_InventLocationId | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_InventSiteId | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_TargetLicensePlateId | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_WorkId | nvarchar | 8000 | 1 |  |  |  |
| WHSWorkTable_WorkTransType | nvarchar | 510 | 1 |  |  |  |
| WMSLocationId | nvarchar | 8000 | 1 |  |  |  |
| WorkClassId | nvarchar | 8000 | 1 |  |  |  |
| WorkClosedUTCDateTime | datetime | 8 | 1 |  |  |  |
| WorkId | nvarchar | 8000 | 1 |  |  |  |
| WorkInProcessUTCDateTime | datetime | 8 | 1 |  |  |  |
| WorkManuallyCompletedBy | nvarchar | 8000 | 1 |  |  |  |
| WorkTemplateCode | nvarchar | 8000 | 1 |  |  |  |
| WorkType | nvarchar | 510 | 1 |  |  |  |
| ZoneId | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spEasyMetricsTransform](../../StoredProcedures/IntegrationStaging/dbo.spEasyMetricsTransform.md)
- [IntegrationStaging: dbo.spEasyMetricsTransform_Bak20231212](../../StoredProcedures/IntegrationStaging/dbo.spEasyMetricsTransform_Bak20231212.md)

