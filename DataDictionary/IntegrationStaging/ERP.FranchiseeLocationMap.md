# ERP.FranchiseeLocationMap

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| FranchiseeName | varchar | 100 | 1 |  |  |  |
| LocationCode | varchar | 5 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)
- [IntegrationStaging: ERP.spMergeDistributionAddressDim](../../StoredProcedures/IntegrationStaging/ERP.spMergeDistributionAddressDim.md)
- [IntegrationStaging: ERP.spMergeFranchiseeLocationMap](../../StoredProcedures/IntegrationStaging/ERP.spMergeFranchiseeLocationMap.md)

