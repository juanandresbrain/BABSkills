# WMS.DynamicsWMSNonWhseInventory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| SKUDescription | varchar | 100 | 1 |  |  |  |
| Qty | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDynamicsWMSNonWhseInventory](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsWMSNonWhseInventory.md)

