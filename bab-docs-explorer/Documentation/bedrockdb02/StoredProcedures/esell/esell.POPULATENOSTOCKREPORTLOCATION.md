# esell.POPULATENOSTOCKREPORTLOCATION

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.POPULATENOSTOCKREPORTLOCATION"]
    dbo_batch_no_stock_location_bak(["dbo.batch_no_stock_location_bak"]) --> SP
    dbo_batch_no_stock_t_location_bak(["dbo.batch_no_stock_t_location_bak"]) --> SP
    dbo_event_reason(["dbo.event_reason"]) --> SP
    dbo_order_fulfillment(["dbo.order_fulfillment"]) --> SP
    dbo_order_line_item(["dbo.order_line_item"]) --> SP
    dbo_orders(["dbo.orders"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_no_stock_location_bak |
| dbo.batch_no_stock_t_location_bak |
| dbo.event_reason |
| dbo.order_fulfillment |
| dbo.order_line_item |
| dbo.orders |
| dbo.sku |

## Stored Procedure Code

```sql
--END POPULATENOSTOCKREPORT--
```

