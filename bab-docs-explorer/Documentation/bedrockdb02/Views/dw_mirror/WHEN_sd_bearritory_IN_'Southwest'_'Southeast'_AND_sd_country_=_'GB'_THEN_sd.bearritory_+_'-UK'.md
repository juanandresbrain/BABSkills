# WHEN sd.bearritory IN ('Southwest'.'Southeast') AND sd.country = 'GB' THEN sd.bearritory + '-UK'

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WHEN sd.bearritory IN ('Southwest'.'Southeast') AND sd.country = 'GB' THEN sd.bearritory + '-UK'"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql

```

