# dbo.WebToESInventoryUpdateLog

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| outlet_id | nvarchar | 40 | 1 |  |  |  |
| sku_id | nvarchar | 48 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| BeforeQty | int | 4 | 1 |  |  |  |
| WebOrderQty | int | 4 | 1 |  |  |  |
| AfterQty | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.spMergeEnterpriseSellingStoreOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingStoreOrderQty.md)
- [esell: dbo.spMergeEnterpriseSellingWebOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingWebOrderQty.md)

