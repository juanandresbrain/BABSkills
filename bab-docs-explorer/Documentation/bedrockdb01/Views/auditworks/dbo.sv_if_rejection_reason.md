# dbo.sv_if_rejection_reason

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_if_rejection_reason"]
    if_rejection_rule(["if_rejection_rule"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| if_rejection_rule |

## View Code

```sql
create view dbo.sv_if_rejection_reason   as
SELECT if_rejection_reason, if_rejection_description FROM if_rejection_rule
```

