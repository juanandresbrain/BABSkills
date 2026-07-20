# dbo.utajobstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utajobstage"]
    dbo_utajobstage(["dbo.utajobstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utajobstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utajobstage] AS SELECT [Job_ID], [Job_Name] COLLATE Latin1_General_CI_AS AS [Job_Name], [Job_Desc] COLLATE Latin1_General_CI_AS AS [Job_Desc] FROM [dbo].[utajobstage]
```

