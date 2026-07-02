# ERP.InventoryAdjustmentLog_3PL

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AdjustmentID | int | 4 | 0 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| WarehouseID | varchar | 4 | 1 |  |  |  |
| Style | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| Description | varchar | 52 | 1 |  |  |  |
| Entity | nvarchar | 10 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

