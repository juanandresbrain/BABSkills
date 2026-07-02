# esell.POPULATEFULFILLMENTRATES

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.POPULATEFULFILLMENTRATES"]
    dbo_batch_fulfillment_rates_bak(["dbo.batch_fulfillment_rates_bak"]) --> SP
    dbo_order_fulfillment(["dbo.order_fulfillment"]) --> SP
    dbo_order_state(["dbo.order_state"]) --> SP
    dbo_ORDERS(["dbo.ORDERS"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_fulfillment_rates_bak |
| dbo.order_fulfillment |
| dbo.order_state |
| dbo.ORDERS |

## Stored Procedure Code

```sql

```

