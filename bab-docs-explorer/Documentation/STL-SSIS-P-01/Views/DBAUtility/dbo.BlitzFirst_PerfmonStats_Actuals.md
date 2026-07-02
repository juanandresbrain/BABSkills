# dbo.BlitzFirst_PerfmonStats_Actuals

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.BlitzFirst_PerfmonStats_Actuals"]
    dbo_BlitzFirst_PerfmonStats_Deltas(["dbo.BlitzFirst_PerfmonStats_Deltas"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.BlitzFirst_PerfmonStats_Deltas |

## View Code

```sql
CREATE VIEW [dbo].[BlitzFirst_PerfmonStats_Actuals] AS
```

