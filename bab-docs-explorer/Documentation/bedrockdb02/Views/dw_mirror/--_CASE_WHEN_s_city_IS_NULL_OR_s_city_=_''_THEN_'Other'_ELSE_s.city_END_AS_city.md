# --.CASE WHEN s.city IS NULL OR s.city = '' THEN 'Other' ELSE s.city END AS city

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["--.CASE WHEN s.city IS NULL OR s.city = '' THEN 'Other' ELSE s.city END AS city"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql

```

