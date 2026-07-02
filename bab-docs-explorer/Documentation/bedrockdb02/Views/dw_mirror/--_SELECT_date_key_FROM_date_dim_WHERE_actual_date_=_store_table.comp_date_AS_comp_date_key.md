# --.(SELECT date_key FROM date_dim WHERE actual_date = store_table.comp_date) AS comp_date_key

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["--.(SELECT date_key FROM date_dim WHERE actual_date = store_table.comp_date) AS comp_date_key"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql

```

