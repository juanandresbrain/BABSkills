# dbo.util_comparison_base_state_bkp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.util_comparison_base_state_bkp"]
    awl_comparison_base_state(["awl_comparison_base_state"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awl_comparison_base_state |

## View Code

```sql
create view dbo.util_comparison_base_state_bkp  as
select *
from auditworks_work..awl_comparison_base_state
```

