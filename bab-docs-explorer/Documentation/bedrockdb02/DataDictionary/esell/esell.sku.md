# esell.sku

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| sku_id | nvarchar | 48 | 0 | YES |  |  |
| sku_price | int | 4 | 1 |  |  |  |
| product_id | nvarchar | 40 | 1 |  |  |  |
| inv_ver_req_cd | nchar | 2 | 1 |  |  |  |
| barcode | nvarchar | 100 | 1 |  |  |  |
| upc | nvarchar | 100 | 1 |  |  |  |
| pick_desc | nvarchar | 160 | 1 |  |  |  |
| sku_avail_date | datetime | 8 | 1 |  |  |  |
| sku_unavail_date | datetime | 8 | 1 |  |  |  |
| search_allowed_cd | nchar | 2 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailMerchVsESStyles](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMerchVsESStyles.md)
- [esell: dbo.spMergeEnterpriseSellingStoreOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingStoreOrderQty.md)
- [esell: dbo.spMergeEnterpriseSellingWebOrderQty](../../StoredProcedures/esell/dbo.spMergeEnterpriseSellingWebOrderQty.md)
- [esell: dbo.spSelectEnterpriseSellingInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805.md)
- [esell: dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719](../../StoredProcedures/esell/dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719.md)

