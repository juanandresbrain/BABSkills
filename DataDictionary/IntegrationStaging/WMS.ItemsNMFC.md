# WMS.ItemsNMFC

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DefaultHandlingType | nvarchar | 8000 | 1 |  |  |  |
| LTLClass | nvarchar | 8000 | 1 |  |  |  |
| Name | nvarchar | 8000 | 1 |  |  |  |
| NMFCCode | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeItemsNMFC](../../StoredProcedures/IntegrationStaging/WMS.spMergeItemsNMFC.md)

