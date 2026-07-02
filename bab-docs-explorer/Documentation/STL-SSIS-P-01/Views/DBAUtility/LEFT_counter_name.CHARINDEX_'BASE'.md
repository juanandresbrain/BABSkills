# LEFT(counter_name.CHARINDEX('BASE'

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["LEFT(counter_name.CHARINDEX('BASE'"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
UPPER(counter_name))-1) AS counter_join
```

