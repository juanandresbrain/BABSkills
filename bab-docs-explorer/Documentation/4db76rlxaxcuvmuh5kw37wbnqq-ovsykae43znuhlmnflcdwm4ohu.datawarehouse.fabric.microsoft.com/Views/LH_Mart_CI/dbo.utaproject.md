# dbo.utaproject

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaproject"]
    dbo_utaproject(["dbo.utaproject"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaproject |

## View Code

```sql
; CREATE   VIEW [dbo].[utaproject] AS     SELECT [PROJ_ID], [PROJ_NAME] COLLATE Latin1_General_CI_AS AS [PROJ_NAME], [PROJ_DESC] COLLATE Latin1_General_CI_AS AS [PROJ_DESC], [InsertDate], [UpdateDate]     FROM [dbo].[utaproject]
```

