# dbo.sp_BlitzCache

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_BlitzCache"]
    dbo_p(["dbo.p"]) --> SP
    n_query(["n.query"]) --> SP
    n_value(["n.value"]) --> SP
    QueryPlan_exist(["QueryPlan.exist"]) --> SP
    QueryPlan_value(["QueryPlan.value"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.p |
| n.query |
| n.value |
| QueryPlan.exist |
| QueryPlan.value |

## Stored Procedure Code

```sql

```

