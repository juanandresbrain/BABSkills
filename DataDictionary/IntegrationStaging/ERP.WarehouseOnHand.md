# ERP.WarehouseOnHand

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaID | varchar | 50 | 1 |  |  |  |
| ItemNumber | varchar | 50 | 1 |  |  |  |
| ProductColorId | varchar | 50 | 1 |  |  |  |
| ProductConfigurationId | varchar | 50 | 1 |  |  |  |
| ProductSizeId | varchar | 50 | 1 |  |  |  |
| ProductStyleId | varchar | 50 | 1 |  |  |  |
| InventorySiteId | varchar | 50 | 1 |  |  |  |
| InventoryWarehouseId | varchar | 50 | 1 |  |  |  |
| AvailableOrderedQuantity | decimal | 9 | 1 |  |  |  |
| OnHandQuantity | decimal | 9 | 1 |  |  |  |
| AvailableOnHandQuantity | decimal | 9 | 1 |  |  |  |
| OnOrderQuantity | decimal | 9 | 1 |  |  |  |
| TotalAvailableQuantity | decimal | 9 | 1 |  |  |  |
| OrderedQuantity | decimal | 9 | 1 |  |  |  |
| AreWarehouseManagementProcessesUsed | bit | 1 | 1 |  |  |  |
| ReservedOrderedQuantity | decimal | 9 | 1 |  |  |  |
| ProductName | varchar | 255 | 1 |  |  |  |
| ReservedOnHandQuantity | decimal | 9 | 1 |  |  |  |
| MerchYearPeriod | varchar | 6 | 1 |  |  |  |
| AreWarehouseManagementProcessesUsed | nvarchar | 510 | 1 |  |  |  |
| AvailableOnHandQuantity | float | 8 | 1 |  |  |  |
| AvailableOrderedQuantity | float | 8 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| InventorySiteId | nvarchar | 8000 | 1 |  |  |  |
| InventoryWarehouseId | nvarchar | 8000 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| OnHandQuantity | float | 8 | 1 |  |  |  |
| OnOrderQuantity | float | 8 | 1 |  |  |  |
| OrderedQuantity | float | 8 | 1 |  |  |  |
| ProductColorId | nvarchar | 8000 | 1 |  |  |  |
| ProductConfigurationId | nvarchar | 8000 | 1 |  |  |  |
| ProductName | nvarchar | 8000 | 1 |  |  |  |
| ProductSizeId | nvarchar | 8000 | 1 |  |  |  |
| ProductStyleId | nvarchar | 8000 | 1 |  |  |  |
| ReservedOnHandQuantity | float | 8 | 1 |  |  |  |
| ReservedOrderedQuantity | float | 8 | 1 |  |  |  |
| TotalAvailableQuantity | float | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP](../../StoredProcedures/IntegrationStaging/ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP.md)

