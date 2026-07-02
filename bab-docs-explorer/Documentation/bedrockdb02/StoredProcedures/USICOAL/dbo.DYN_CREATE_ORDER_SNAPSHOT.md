# dbo.DYN_CREATE_ORDER_SNAPSHOT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DYN_CREATE_ORDER_SNAPSHOT"]
    dbo_DYN_GEN_INSTANCE_NO(["dbo.DYN_GEN_INSTANCE_NO"]) --> SP
    dbo_DYN_POPULATE_ORDER_SNAPSHOT(["dbo.DYN_POPULATE_ORDER_SNAPSHOT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DYN_GEN_INSTANCE_NO |
| dbo.DYN_POPULATE_ORDER_SNAPSHOT |

## Stored Procedure Code

```sql

```

