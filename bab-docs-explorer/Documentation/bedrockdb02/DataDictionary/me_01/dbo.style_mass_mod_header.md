# dbo.style_mass_mod_header

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| long_desc | nvarchar | 240 | 1 |  |  |  |
| short_desc | nvarchar | 100 | 1 |  |  |  |
| plu_desc | nvarchar | 100 | 1 |  |  |  |
| season_id | smallint | 2 | 1 |  |  |  |
| calendar_year_id | smallint | 2 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| ticket_format_id | decimal | 9 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| resulting_po_predistrib_type | smallint | 2 | 1 |  |  |  |
| replenishable_flag | bit | 1 | 1 |  |  |  |
| inhouse_upc_flag | bit | 1 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| consignment_flag | bit | 1 | 1 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 1 |  |  |  |
| promo_flag | bit | 1 | 1 |  |  |  |
| fashion_flag | bit | 1 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| remove_selling_period | bit | 1 | 1 |  |  |  |
| target_selling_from_week | tinyint | 1 | 1 |  |  |  |
| target_selling_to_week | tinyint | 1 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| remove_measurements | bit | 1 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| eom_available_to_sell_datetime | datetime | 8 | 1 |  |  |  |
| allow_customer_back_order | smallint | 2 | 1 |  |  |  |
| protected_flag | bit | 1 | 1 |  |  |  |

