# dbo.imp_user_def_adj_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_user_def_adj_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_user_def_adj_id | decimal | 9 | 1 |  |  |  |
| action | nchar | 2 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |
| cost_to_adjust | decimal | 9 | 1 |  |  |  |
| record_type | nchar | 2 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| cost_to_adjust_loc | decimal | 9 | 1 |  |  |  |
| total_unit_adjust | int | 4 | 1 |  |  |  |
| total_retail_adjust | decimal | 9 | 1 |  |  |  |
| total_cost_adjust | decimal | 9 | 1 |  |  |  |
| total_unit_adjust_sending_loc | int | 4 | 1 |  |  |  |
| total_retail_adjust_sending_loc | decimal | 9 | 1 |  |  |  |
| total_cost_adjust_sending_loc | decimal | 9 | 1 |  |  |  |
| sending_location | nvarchar | 40 | 1 |  |  |  |
| receiving_location | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailImportUDAerrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailImportUDAerrors.md)

