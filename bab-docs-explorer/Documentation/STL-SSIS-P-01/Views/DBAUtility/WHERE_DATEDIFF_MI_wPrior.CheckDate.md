# WHERE DATEDIFF(MI.wPrior.CheckDate

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WHERE DATEDIFF(MI.wPrior.CheckDate"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
w.CheckDate) BETWEEN 1 AND 60
```

