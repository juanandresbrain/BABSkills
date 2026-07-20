# dbo.utadepartment

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utadepartment"]
    dbo_utadepartment(["dbo.utadepartment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utadepartment |

## View Code

```sql
; CREATE   VIEW [dbo].[utadepartment] AS     SELECT [DEPT_ID], [DEPT_NAME] COLLATE Latin1_General_CI_AS AS [DEPT_NAME], [DEPT_DESC] COLLATE Latin1_General_CI_AS AS [DEPT_DESC], [InsertDate], [UpdateDate]     FROM [dbo].[utadepartment]
```

