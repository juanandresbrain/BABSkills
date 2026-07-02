# dbo.c_stp_print_tickets_$sp

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.c_stp_print_tickets_$sp"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_c_stp_detail(["dbo.c_stp_detail"]) --> SP
    dbo_c_stp_header(["dbo.c_stp_header"]) --> SP
    dbo_c_stp_location(["dbo.c_stp_location"]) --> SP
    dbo_c_temp_ib_price(["dbo.c_temp_ib_price"]) --> SP
    dbo_c_temp_tp_results(["dbo.c_temp_tp_results"]) --> SP
    dbo_dist_detail(["dbo.dist_detail"]) --> SP
    dbo_distribution(["dbo.distribution"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_ib_inventory(["dbo.ib_inventory"]) --> SP
    dbo_ib_inventory_total(["dbo.ib_inventory_total"]) --> SP
    dbo_ib_price(["dbo.ib_price"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_price_change(["dbo.price_change"]) --> SP
    dbo_price_change_style(["dbo.price_change_style"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_spt_values(["dbo.spt_values"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_retail(["dbo.style_retail"]) --> SP
    dbo_transfer(["dbo.transfer"]) --> SP
    dbo_transfer_detail(["dbo.transfer_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.c_stp_detail |
| dbo.c_stp_header |
| dbo.c_stp_location |
| dbo.c_temp_ib_price |
| dbo.c_temp_tp_results |
| dbo.dist_detail |
| dbo.distribution |
| dbo.entity_attribute_set |
| dbo.ib_inventory |
| dbo.ib_inventory_total |
| dbo.ib_price |
| dbo.jurisdiction |
| dbo.location |
| dbo.price_change |
| dbo.price_change_style |
| dbo.sku |
| dbo.spt_values |
| dbo.style |
| dbo.style_retail |
| dbo.transfer |
| dbo.transfer_detail |

## Stored Procedure Code

```sql

```

