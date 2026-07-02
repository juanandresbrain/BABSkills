# WEB.UKWebstoreProductBalance

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventoryDate | date | 3 | 1 |  |  |  |
| StyleCode | varchar | 50 | 1 |  |  |  |
| ARRQuantity | int | 4 | 1 |  |  |  |
| AVLQuantity | int | 4 | 1 |  |  |  |
| TRAQuantity | int | 4 | 1 |  |  |  |
| ORDQuantity | int | 4 | 1 |  |  |  |
| PCKQuantity | int | 4 | 1 |  |  |  |
| AWPQuantity | int | 4 | 1 |  |  |  |
| ALLQuantity | int | 4 | 1 |  |  |  |
| ADVQuantity | int | 4 | 1 |  |  |  |
| HLDQuantity | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| UpdatedByFileName | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeInventoryFactFromWM](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWM.md)
- [IntegrationStaging: WEB.spMergeUKWebProductBalance](../../StoredProcedures/IntegrationStaging/WEB.spMergeUKWebProductBalance.md)
- [IntegrationStaging: WEB.spMergeUKWebProductBalance_BAK20230822](../../StoredProcedures/IntegrationStaging/WEB.spMergeUKWebProductBalance_BAK20230822.md)

