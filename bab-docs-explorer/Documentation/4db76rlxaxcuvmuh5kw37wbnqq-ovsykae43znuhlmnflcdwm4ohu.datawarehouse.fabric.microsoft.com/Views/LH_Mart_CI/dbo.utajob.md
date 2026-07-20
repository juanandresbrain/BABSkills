# dbo.utajob

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utajob"]
    dbo_utajob(["dbo.utajob"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utajob |

## View Code

```sql
; CREATE   VIEW [dbo].[utajob] AS     SELECT [Job_ID], [Job_Name] COLLATE Latin1_General_CI_AS AS [Job_Name], [Job_Desc] COLLATE Latin1_General_CI_AS AS [Job_Desc], [InsertDate], [UpdateDate]     FROM [dbo].[utajob]
```

