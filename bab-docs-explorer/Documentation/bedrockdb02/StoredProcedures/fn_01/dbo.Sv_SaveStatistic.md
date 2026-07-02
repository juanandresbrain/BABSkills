# dbo.Sv_SaveStatistic

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_SaveStatistic"]
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Sv_Object(["dbo.Sv_Object"]) --> SP
    dbo_Sv_Statistic(["dbo.Sv_Statistic"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_GetNextID |
| dbo.Sv_Object |
| dbo.Sv_Statistic |

## Stored Procedure Code

```sql

```

