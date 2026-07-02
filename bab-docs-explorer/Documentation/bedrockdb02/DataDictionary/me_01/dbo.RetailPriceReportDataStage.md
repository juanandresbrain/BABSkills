# dbo.RetailPriceReportDataStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| custom_property_value | nvarchar | 60 | 1 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| start_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| selling_retail_price | numeric | 9 | 1 |  |  |  |
| current_selling_retail | numeric | 9 | 1 |  |  |  |
| original_selling_retail | numeric | 9 | 1 |  |  |  |
| current_cost | numeric | 9 | 1 |  |  |  |
| hGroup | nvarchar | 40 | 1 |  |  |  |
| Retail | numeric | 13 | 1 |  |  |  |

