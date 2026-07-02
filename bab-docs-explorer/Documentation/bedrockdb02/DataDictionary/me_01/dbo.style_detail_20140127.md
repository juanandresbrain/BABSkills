# dbo.style_detail_20140127

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_detail_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| total_inventory_units | int | 4 | 0 |  |  |  |
| last_net_po_cost | decimal | 9 | 1 |  |  |  |
| last_net_final_po_cost | decimal | 9 | 1 |  |  |  |
| mix_match_rule_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

