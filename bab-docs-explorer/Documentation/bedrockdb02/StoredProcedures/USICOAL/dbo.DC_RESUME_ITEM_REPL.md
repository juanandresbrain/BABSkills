# dbo.DC_RESUME_ITEM_REPL

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RESUME_ITEM_REPL"]
    dbo_RPL_PUB_SUB(["dbo.RPL_PUB_SUB"]) --> SP
    dbo_RPL_RUN_DISTR_AGENTS(["dbo.RPL_RUN_DISTR_AGENTS"]) --> SP
    dbo_RPL_RUN_SNAPSHOT_AGENTS_SYNC(["dbo.RPL_RUN_SNAPSHOT_AGENTS_SYNC"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RPL_PUB_SUB |
| dbo.RPL_RUN_DISTR_AGENTS |
| dbo.RPL_RUN_SNAPSHOT_AGENTS_SYNC |

## Stored Procedure Code

```sql

```

