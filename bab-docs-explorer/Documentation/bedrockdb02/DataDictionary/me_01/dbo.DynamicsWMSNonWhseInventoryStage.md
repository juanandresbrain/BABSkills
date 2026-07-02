# dbo.DynamicsWMSNonWhseInventoryStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| Qty | bigint | 8 | 1 |  |  |  |
| LoadDate | datetime | 8 | 1 |  |  |  |
| SKUDescription | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMergeDynamicsWMSNonWhseInventory](../../StoredProcedures/me_01/dbo.spMergeDynamicsWMSNonWhseInventory.md)

