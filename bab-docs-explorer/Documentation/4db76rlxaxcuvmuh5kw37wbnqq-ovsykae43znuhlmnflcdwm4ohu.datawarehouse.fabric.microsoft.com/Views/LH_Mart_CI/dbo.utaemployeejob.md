# dbo.utaemployeejob

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaemployeejob"]
    dbo_utaemployeejob(["dbo.utaemployeejob"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaemployeejob |

## View Code

```sql
; CREATE   VIEW [dbo].[utaemployeejob] AS     SELECT [Emp_ID], [Empjob_Start_Date], [Empjob_End_Date], [Job_ID], [InsertDate], [UpdateDate]     FROM [dbo].[utaemployeejob]
```

