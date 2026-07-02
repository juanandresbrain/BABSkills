# dbo.rptCurrRetail

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| Department | nvarchar | 16 | 1 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| start_date | smalldatetime | 4 | 1 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| selling_retail_price | decimal | 9 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.spMerchandisingTopStyleStage](../../StoredProcedures/ma_01/dbo.spMerchandisingTopStyleStage.md)

