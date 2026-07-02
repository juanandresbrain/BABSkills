# dbo.spTSM_Not_Posting

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spTSM_Not_Posting"]
    dbo_retail_transaction(["dbo.retail_transaction"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.retail_transaction |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql

```

