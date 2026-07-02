# dbo.DynamicsWMSNonWhseInventory

**Database:** me_01  
**Server:** bedrockdb02  

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

- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink.md)
- [me_01: dbo.spMergeDynamicsWMSNonWhseInventory](../../StoredProcedures/me_01/dbo.spMergeDynamicsWMSNonWhseInventory.md)
- [me_01: dbo.spSelectStoreInventoryPrepData](../../StoredProcedures/me_01/dbo.spSelectStoreInventoryPrepData.md)

