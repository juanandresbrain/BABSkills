# dbo.utadepartmentstagerejects

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utadepartmentstagerejects"]
    dbo_utadepartmentstagerejects(["dbo.utadepartmentstagerejects"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utadepartmentstagerejects |

## View Code

```sql
; CREATE   VIEW [dbo].[utadepartmentstagerejects] AS SELECT [DEPT_ID], [DEPT_NAME] COLLATE Latin1_General_CI_AS AS [DEPT_NAME], [DEPT_DESC] COLLATE Latin1_General_CI_AS AS [DEPT_DESC], [ErrorCode], [ErrorColumn], [RejectDate] FROM [dbo].[utadepartmentstagerejects]
```

