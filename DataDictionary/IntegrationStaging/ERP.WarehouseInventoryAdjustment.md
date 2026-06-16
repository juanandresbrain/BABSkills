# ERP.WarehouseInventoryAdjustment

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| WarehouseID | varchar | 5 | 1 |  |  |  |
| Style | varchar | 6 | 1 |  |  |  |
| ItemID | varchar | 7 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| Description | varchar | 52 | 1 |  |  |  |
| AdjustmentDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeWarehouseInventoryAdjustment_BAK20230911](../../StoredProcedures/IntegrationStaging/ERP.spMergeWarehouseInventoryAdjustment_BAK20230911.md)

