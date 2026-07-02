# dbo.DYN_POPULATE_PLU_SNAPSHOT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DYN_POPULATE_PLU_SNAPSHOT"]
    dbo_DM_CONFIG(["dbo.DM_CONFIG"]) --> SP
    dbo_DM_DATABASE_BLANK(["dbo.DM_DATABASE_BLANK"]) --> SP
    dbo_DM_DATABASE_INSTANCE(["dbo.DM_DATABASE_INSTANCE"]) --> SP
    dbo_DYN_CREATE_BLANK_DATABASES_SYNC(["dbo.DYN_CREATE_BLANK_DATABASES_SYNC"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DM_CONFIG |
| dbo.DM_DATABASE_BLANK |
| dbo.DM_DATABASE_INSTANCE |
| dbo.DYN_CREATE_BLANK_DATABASES_SYNC |

## Stored Procedure Code

```sql

```

