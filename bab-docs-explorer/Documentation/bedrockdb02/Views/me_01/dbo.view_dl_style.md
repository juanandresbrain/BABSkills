# dbo.view_dl_style

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style"]
    dbo_dl_style(["dbo.dl_style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style |

## View Code

```sql
create view dbo.view_dl_style 
AS
SELECT dl_style_id,
   record_no,
   style_code,
   hierarchy_group_code,
   merch_type,
   style_status,
   long_desc,
   short_desc,
   season_code,
   calendar_year_code,
   ticket_format_code,
   weight,
   height,
   width,
   depth,
   plu_desc,
   position_code,
   promo_flag,
   inhouse_upc_flag,
   vendor_upc_flag,
   reorder_flag,
   fashion_flag,
   consignment_flag,
   replenishable_flag,
   create_date,
   order_multiple,
   distribution_multiple,
   target_selling_from_week,
   target_selling_from_year,
   target_selling_to_week,
   target_selling_to_year,
   original_selling_retail,
   original_price_status_code,
   compare_at_retail,
   size_grid_code,
   vendor_code,
   vendor_style,
   current_cost,
   current_cost_currency_code,
   active_flag,
   mix_match_rule_code_1,
   mix_match_rule_code_2,
   mix_match_rule_code_3,
   mix_match_rule_code_4,
   current_selling_retail,
   current_price_status_code,
   last_net_final_po_cost,
   last_receipt_date,
   allow_customer_back_order_flag,
   resulting_po_predistrib_type
FROM dl_style
```

