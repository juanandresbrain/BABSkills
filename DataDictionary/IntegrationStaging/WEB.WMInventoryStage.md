# WEB.WMInventoryStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeInventoryFactFromWM](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWM.md)
- [IntegrationStaging: WEB.spMergeInventoryFactFromWMbackup20191208](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWMbackup20191208.md)

