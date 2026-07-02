# dbo.BlitzFirst_WaitStats_Deltas

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.BlitzFirst_WaitStats_Deltas"]
    dbo_BlitzFirst_WaitStats(["dbo.BlitzFirst_WaitStats"]) --> VIEW
    dbo_BlitzFirst_WaitStats_Categories(["dbo.BlitzFirst_WaitStats_Categories"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.BlitzFirst_WaitStats |
| dbo.BlitzFirst_WaitStats_Categories |

## View Code

```sql
CREATE VIEW [dbo].[BlitzFirst_WaitStats_Deltas] AS
```

