# dbo.spUSICOALTransCountCheck

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spUSICOALTransCountCheck"]
    dbo_notification_history(["dbo.notification_history"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.notification_history |
| dbo.RETAIL_TRANSACTION |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql

```

