# dbo.spTruncateEJHistory

**Database:** EJ  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spTruncateEJHistory"]
    dbo_IMPORT_AUDIT(["dbo.IMPORT_AUDIT"]) --> SP
    dbo_SIGNATURES(["dbo.SIGNATURES"]) --> SP
    dbo_Tenders(["dbo.Tenders"]) --> SP
    dbo_Transactions(["dbo.Transactions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.IMPORT_AUDIT |
| dbo.SIGNATURES |
| dbo.Tenders |
| dbo.Transactions |

## Stored Procedure Code

```sql

```

