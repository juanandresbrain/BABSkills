# esell.outlet_sku_xref

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| sku_id | nvarchar | 48 | 0 | YES |  |  |
| outlet_id | nvarchar | 40 | 0 | YES |  |  |
| threshold | int | 4 | 0 |  |  |  |
| qty | int | 4 | 0 |  |  |  |
| sku_price | int | 4 | 1 |  |  |  |
| tax_rate | numeric | 5 | 1 |  |  |  |
| sell_thru | numeric | 5 | 1 |  |  |  |
| inv_status_1 | int | 4 | 0 |  |  |  |
| inv_status_2 | int | 4 | 0 |  |  |  |
| inv_status_3 | int | 4 | 0 |  |  |  |
| inv_status_4 | int | 4 | 0 |  |  |  |
| inv_status_5 | int | 4 | 0 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |
| group_id | nvarchar | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.spMergeEnterpriseSellingStoreOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingStoreOrderQty.md)
- [esell: dbo.spMergeEnterpriseSellingWebOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingWebOrderQty.md)
- [esell: dbo.spSelectEnterpriseSellingInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719.md)

