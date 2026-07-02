# WHERE DATEDIFF(MI.pMonPrior.CheckDate

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WHERE DATEDIFF(MI.pMonPrior.CheckDate"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
pMon.CheckDate) BETWEEN 1 AND 60;
```

