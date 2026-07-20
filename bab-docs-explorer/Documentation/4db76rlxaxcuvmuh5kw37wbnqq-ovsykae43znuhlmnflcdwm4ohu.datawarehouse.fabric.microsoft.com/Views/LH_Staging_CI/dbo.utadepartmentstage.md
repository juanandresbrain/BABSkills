# dbo.utadepartmentstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utadepartmentstage"]
    dbo_utadepartmentstage(["dbo.utadepartmentstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utadepartmentstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utadepartmentstage] AS SELECT [DEPT_ID], [DEPT_NAME] COLLATE Latin1_General_CI_AS AS [DEPT_NAME], [DEPT_DESC] COLLATE Latin1_General_CI_AS AS [DEPT_DESC] FROM [dbo].[utadepartmentstage]
```

