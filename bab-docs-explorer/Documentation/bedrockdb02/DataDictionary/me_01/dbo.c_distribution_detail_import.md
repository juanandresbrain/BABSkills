# dbo.c_distribution_detail_import

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | numeric | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| location_id | numeric | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingImportDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingImportDistributions.md)
- [me_01: dbo.spMerchandisingSelectDistroPipelineErrors](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDistroPipelineErrors.md)

