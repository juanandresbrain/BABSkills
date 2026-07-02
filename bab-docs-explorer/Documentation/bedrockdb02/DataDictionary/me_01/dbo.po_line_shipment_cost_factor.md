# dbo.po_line_shipment_cost_factor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_line_shipment_cost_factor_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| po_line_shipment_id | smallint | 2 | 0 |  |  |  |
| cost_factor_id | smallint | 2 | 1 |  | YES |  |
| currency_indicator | smallint | 2 | 1 |  |  |  |
| factor_amount | float | 8 | 1 |  |  |  |
| cost_factor_estimation_method | smallint | 2 | 1 |  |  |  |

