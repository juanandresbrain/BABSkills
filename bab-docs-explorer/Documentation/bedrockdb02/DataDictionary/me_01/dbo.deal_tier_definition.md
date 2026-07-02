# dbo.deal_tier_definition

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deal_tier_definition_id | int | 4 | 0 | YES |  |  |
| deal_id | int | 4 | 0 |  |  |  |
| deal_discount_id | int | 4 | 0 |  |  |  |
| threshold_type | nvarchar | 8 | 1 |  |  |  |
| threshold_qty | int | 4 | 1 |  |  |  |
| threshold_amt | decimal | 9 | 1 |  |  |  |
| disc_type | nvarchar | 8 | 1 |  |  |  |
| disc_pct | decimal | 5 | 1 |  |  |  |
| disc_amt | decimal | 9 | 1 |  |  |  |
| disc_applies_to | nvarchar | 8 | 1 |  |  |  |
| disc_qty | tinyint | 1 | 1 |  |  |  |
| add_info | nvarchar | 500 | 1 |  |  |  |

