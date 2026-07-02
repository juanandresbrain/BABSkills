# SELECT sd.store_key.sd.store_id

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["SELECT sd.store_key.sd.store_id"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
sd.store_name
```

