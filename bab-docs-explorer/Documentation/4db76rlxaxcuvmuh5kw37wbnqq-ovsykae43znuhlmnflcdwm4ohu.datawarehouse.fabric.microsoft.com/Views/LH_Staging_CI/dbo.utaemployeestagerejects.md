# dbo.utaemployeestagerejects

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaemployeestagerejects"]
    dbo_utaemployeestagerejects(["dbo.utaemployeestagerejects"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaemployeestagerejects |

## View Code

```sql
; CREATE   VIEW [dbo].[utaemployeestagerejects] AS SELECT [Emp_ID] COLLATE Latin1_General_CI_AS AS [Emp_ID], [Emp_Fullname] COLLATE Latin1_General_CI_AS AS [Emp_Fullname], [Emp_Name] COLLATE Latin1_General_CI_AS AS [Emp_Name], [Calcgrp_ID] COLLATE Latin1_General_CI_AS AS [Calcgrp_ID], [Emp_Base_Rate] COLLATE Latin1_General_CI_AS AS [Emp_Base_Rate], [ErrorCode], [ErrorColumn], [RejectDate] FROM [dbo].[utaemployeestagerejects]
```

