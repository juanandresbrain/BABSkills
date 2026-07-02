# dbo.deal_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deal_location_id | int | 4 | 0 | YES |  |  |
| deal_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| printed_status | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_prices_validation_$sp](../../StoredProcedures/me_01/dbo.copy_location_prices_validation_$sp.md)
- [me_01: dbo.copy_location_to_deals_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_deals_$sp.md)

