# WMS.ItemCasePackStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseId | varchar | 10 | 1 |  |  |  |
| StyleCode | varchar | 10 | 1 |  |  |  |
| ItemDesc | varchar | 150 | 1 |  |  |  |
| OrderMultiple | int | 4 | 1 |  |  |  |
| DistribMultiple | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeItemCasePack](../../StoredProcedures/IntegrationStaging/WMS.spMergeItemCasePack.md)

