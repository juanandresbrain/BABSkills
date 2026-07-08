# dbo.upc_only_sa

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.upc_only_sa"]
    user_upc(["user_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| user_upc |

## View Code

```sql
create view dbo.upc_only_sa AS
SELECT u.upc_lookup_division, u.upc_no, u.style_reference_id
FROM user_upc u
```

