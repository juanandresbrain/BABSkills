# esell.POPULATEORDERSTATUS

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.POPULATEORDERSTATUS"]
    dbo_batch_order_status_bak(["dbo.batch_order_status_bak"]) --> SP
    dbo_order_fulfillment(["dbo.order_fulfillment"]) --> SP
    dbo_order_fulfillment_extn(["dbo.order_fulfillment_extn"]) --> SP
    dbo_order_line_item(["dbo.order_line_item"]) --> SP
    dbo_ORDER_STATE(["dbo.ORDER_STATE"]) --> SP
    dbo_orders(["dbo.orders"]) --> SP
    dbo_Route_History(["dbo.Route_History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_order_status_bak |
| dbo.order_fulfillment |
| dbo.order_fulfillment_extn |
| dbo.order_line_item |
| dbo.ORDER_STATE |
| dbo.orders |
| dbo.Route_History |

## Stored Procedure Code

```sql
--Start 146561
```

