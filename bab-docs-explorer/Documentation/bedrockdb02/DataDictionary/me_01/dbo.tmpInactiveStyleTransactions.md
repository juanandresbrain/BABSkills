# dbo.tmpInactiveStyleTransactions

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| transaction_date | varchar | 30 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| transaction_type | nvarchar | 512 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailInactiveStyleTransactions](../../StoredProcedures/me_01/dbo.spMerchandisingEmailInactiveStyleTransactions.md)

