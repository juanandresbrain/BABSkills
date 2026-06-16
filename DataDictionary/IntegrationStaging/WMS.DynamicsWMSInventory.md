# WMS.DynamicsWMSInventory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| sku_desc | varchar | 100 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDynamicsWMSInventory](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsWMSInventory.md)

