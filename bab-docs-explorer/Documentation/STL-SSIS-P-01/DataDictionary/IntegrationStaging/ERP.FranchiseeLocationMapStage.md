# ERP.FranchiseeLocationMapStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| FranchiseeName | varchar | 100 | 1 |  |  |  |
| LocationCode | varchar | 5 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeFranchiseeLocationMap](../../StoredProcedures/IntegrationStaging/ERP.spMergeFranchiseeLocationMap.md)

