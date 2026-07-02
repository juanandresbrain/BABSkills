# dbo.spES_Aged_Orders_Check

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spES_Aged_Orders_Check"]
    dbo_notification_history(["dbo.notification_history"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    esell_batch_order_status(["esell.batch_order_status"]) --> SP
    esell_order_state(["esell.order_state"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.notification_history |
| dbo.sp_send_dbmail |
| esell.batch_order_status |
| esell.order_state |

## Stored Procedure Code

```sql

```

