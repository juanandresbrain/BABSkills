# when country = 'UK' then RIGHT('000' + CAST(sd.store_id AS varchar).4) + ' ' + sd.store_name

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["when country = 'UK' then RIGHT('000' + CAST(sd.store_id AS varchar).4) + ' ' + sd.store_name"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql

```

