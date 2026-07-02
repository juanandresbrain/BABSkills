# dbo.deleted_style_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_location_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_id | smallint | 2 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| mix_match_rule_id1 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id2 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id3 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id4 | decimal | 9 | 1 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)

