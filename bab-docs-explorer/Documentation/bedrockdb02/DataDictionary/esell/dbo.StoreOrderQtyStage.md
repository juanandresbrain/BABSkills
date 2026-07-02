# dbo.StoreOrderQtyStage

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OutletID | varchar | 5 | 1 |  |  |  |
| Style | varchar | 50 | 1 |  |  |  |
| OrderQty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.spMergeEnterpriseSellingStoreOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingStoreOrderQty.md)

