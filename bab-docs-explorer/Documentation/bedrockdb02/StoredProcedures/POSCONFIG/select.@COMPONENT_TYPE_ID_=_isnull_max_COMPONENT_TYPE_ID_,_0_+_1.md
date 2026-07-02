# select.@COMPONENT_TYPE_ID = isnull(max(COMPONENT_TYPE_ID), 0) + 1

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["select.@COMPONENT_TYPE_ID = isnull(max(COMPONENT_TYPE_ID), 0) + 1"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql

```

