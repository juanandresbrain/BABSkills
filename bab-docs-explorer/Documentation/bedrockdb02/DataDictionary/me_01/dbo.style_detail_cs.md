# dbo.style_detail_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_detail_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| total_inventory_units | int | 4 | 1 |  |  |  |
| last_net_po_cost | decimal | 9 | 1 |  |  |  |
| last_net_final_po_cost | decimal | 9 | 1 |  |  |  |
| mix_match_rule_flag | bit | 1 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

