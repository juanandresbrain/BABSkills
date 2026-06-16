# POS.ZebraLabelProductInfo

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| cost | varchar | 14 | 1 |  |  |  |
| local_desc | nvarchar | 80 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 0 |  |  |  |
| in_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: POS.spMergeZebraLabelPricing](../../StoredProcedures/IntegrationStaging/POS.spMergeZebraLabelPricing.md)

