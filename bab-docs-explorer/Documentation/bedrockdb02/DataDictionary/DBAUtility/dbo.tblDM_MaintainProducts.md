# dbo.tblDM_MaintainProducts

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_code | varchar | 20 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 0 |  |  |  |
| hg_code | varchar | 8 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| sku | bigint | 8 | 1 |  |  |  |
| subclass_code | varchar | 20 | 1 |  |  |  |
| subclass | varchar | 20 | 1 |  |  |  |
| class | varchar | 20 | 1 |  |  |  |
| department | varchar | 20 | 1 |  |  |  |
| department_code | varchar | 20 | 1 |  |  |  |
| division | varchar | 20 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| start_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| selling_retail_price | numeric | 9 | 1 |  |  |  |
| current_selling_retail | numeric | 9 | 1 |  |  |  |
| original_selling_retail | numeric | 9 | 1 |  |  |  |
| ib_price_id | numeric | 9 | 0 |  |  |  |
| style_id | numeric | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)

