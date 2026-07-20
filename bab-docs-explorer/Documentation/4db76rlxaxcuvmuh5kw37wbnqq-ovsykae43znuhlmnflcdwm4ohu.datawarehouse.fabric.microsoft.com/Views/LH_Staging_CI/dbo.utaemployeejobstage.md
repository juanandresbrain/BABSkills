# dbo.utaemployeejobstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaemployeejobstage"]
    dbo_utaemployeejobstage(["dbo.utaemployeejobstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaemployeejobstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaemployeejobstage] AS SELECT [Emp_ID], [Empjob_Start_Date], [Empjob_End_Date], [Job_ID] FROM [dbo].[utaemployeejobstage]
```

