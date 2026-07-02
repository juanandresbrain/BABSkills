# esell.POPULATESKUDEMAND

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.POPULATESKUDEMAND"]
    dbo_batch_sku_demand_bak(["dbo.batch_sku_demand_bak"]) --> SP
    dbo_order_line_item(["dbo.order_line_item"]) --> SP
    dbo_orders(["dbo.orders"]) --> SP
    dbo_outlet_query_log(["dbo.outlet_query_log"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_sku_demand_bak |
| dbo.order_line_item |
| dbo.orders |
| dbo.outlet_query_log |
| dbo.sku |

## Stored Procedure Code

```sql
--END PopulateOrderSummary--
```

