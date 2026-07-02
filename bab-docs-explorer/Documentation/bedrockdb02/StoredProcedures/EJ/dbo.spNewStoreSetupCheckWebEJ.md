# dbo.spNewStoreSetupCheckWebEJ

**Database:** EJ  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spNewStoreSetupCheckWebEJ"]
    dbo_notification_history(["dbo.notification_history"]) --> SP
    dbo_POLLING_STORES(["dbo.POLLING_STORES"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_STORES(["dbo.STORES"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.notification_history |
| dbo.POLLING_STORES |
| dbo.sp_send_dbmail |
| dbo.STORES |

## Stored Procedure Code

```sql

```

