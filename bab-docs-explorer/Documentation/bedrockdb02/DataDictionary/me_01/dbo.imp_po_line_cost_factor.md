# dbo.imp_po_line_cost_factor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_po_line_cost_factor_id | decimal | 9 | 0 |  |  |  |
| imp_po_id | decimal | 9 | 0 |  |  |  |
| action_type | nchar | 2 | 1 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| cost_factor_code | nvarchar | 30 | 0 |  |  |  |
| currency_indicator | smallint | 2 | 0 |  |  |  |
| factor_amount | float | 8 | 0 |  |  |  |
| line_number | smallint | 2 | 0 |  |  |  |

