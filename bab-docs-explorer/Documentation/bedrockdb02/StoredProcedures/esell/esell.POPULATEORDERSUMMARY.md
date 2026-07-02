# esell.POPULATEORDERSUMMARY

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.POPULATEORDERSUMMARY"]
    dbo_batch_order_summary_bak(["dbo.batch_order_summary_bak"]) --> SP
    dbo_event_reason(["dbo.event_reason"]) --> SP
    dbo_order_line_item(["dbo.order_line_item"]) --> SP
    dbo_order_state(["dbo.order_state"]) --> SP
    dbo_ORDERS(["dbo.ORDERS"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_order_summary_bak |
| dbo.event_reason |
| dbo.order_line_item |
| dbo.order_state |
| dbo.ORDERS |

## Stored Procedure Code

```sql
--END POPULATEORDERSTATUS--
```

