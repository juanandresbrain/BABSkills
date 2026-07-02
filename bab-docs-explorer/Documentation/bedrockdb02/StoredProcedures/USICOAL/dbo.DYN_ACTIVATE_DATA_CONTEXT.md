# dbo.DYN_ACTIVATE_DATA_CONTEXT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DYN_ACTIVATE_DATA_CONTEXT"]
    dbo_DYN_CREATE_DATA_CONTEXT(["dbo.DYN_CREATE_DATA_CONTEXT"]) --> SP
    dbo_DYN_GEN_CONTEXT_HNDL(["dbo.DYN_GEN_CONTEXT_HNDL"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DYN_CREATE_DATA_CONTEXT |
| dbo.DYN_GEN_CONTEXT_HNDL |

## Stored Procedure Code

```sql

```

