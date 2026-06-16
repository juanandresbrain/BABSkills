# WEB.PreOrderBackOrderInventory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SKU | varchar | 6 | 1 |  |  |  |
| NonInstockQty | int | 4 | 1 |  |  |  |
| InstockDate | datetime | 8 | 1 |  |  |  |
| InventoryType | varchar | 52 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergePreOrderBackOrderInventory](../../StoredProcedures/IntegrationStaging/WEB.spMergePreOrderBackOrderInventory.md)

