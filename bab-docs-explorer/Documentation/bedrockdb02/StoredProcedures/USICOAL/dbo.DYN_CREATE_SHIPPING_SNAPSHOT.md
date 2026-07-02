# dbo.DYN_CREATE_SHIPPING_SNAPSHOT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DYN_CREATE_SHIPPING_SNAPSHOT"]
    dbo_DYN_GEN_INSTANCE_NO(["dbo.DYN_GEN_INSTANCE_NO"]) --> SP
    dbo_DYN_POPULATE_SHIPPING_SNAPSHOT(["dbo.DYN_POPULATE_SHIPPING_SNAPSHOT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DYN_GEN_INSTANCE_NO |
| dbo.DYN_POPULATE_SHIPPING_SNAPSHOT |

## Stored Procedure Code

```sql

```

