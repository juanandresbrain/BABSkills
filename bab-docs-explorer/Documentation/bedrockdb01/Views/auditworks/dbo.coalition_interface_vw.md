# dbo.coalition_interface_vw

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.coalition_interface_vw"]
    coalition_interface(["coalition_interface"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| coalition_interface |

## View Code

```sql
create view dbo.coalition_interface_vw
AS SELECT record_content
FROM coalition_interface
```

