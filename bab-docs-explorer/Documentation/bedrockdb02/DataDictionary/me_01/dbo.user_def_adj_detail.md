# dbo.user_def_adj_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_def_adj_detail_id | decimal | 9 | 0 | YES |  |  |
| user_defined_adjustment_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| cost_to_adjust | decimal | 9 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| total_retail_to_adjust | decimal | 9 | 1 |  |  |  |
| total_cost_to_adjust | decimal | 9 | 1 |  |  |  |
| to_location_id | smallint | 2 | 1 |  |  |  |
| total_val_retail_to_adjust | decimal | 9 | 1 |  |  |  |
| cost_to_adjust_loc | decimal | 9 | 1 |  |  |  |
| total_cost_to_adjust_loc | decimal | 9 | 1 |  |  |  |
| total_retail_to_adjust_loc | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_udt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_udt_documents_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.spMerchandisingEmailCostcoShipmentUDA](../../StoredProcedures/me_01/dbo.spMerchandisingEmailCostcoShipmentUDA.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)

