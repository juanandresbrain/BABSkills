# dbo.utaprojectstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaprojectstage"]
    dbo_utaprojectstage(["dbo.utaprojectstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaprojectstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaprojectstage] AS SELECT [PROJ_ID], [PROJ_NAME] COLLATE Latin1_General_CI_AS AS [PROJ_NAME], [PROJ_DESC] COLLATE Latin1_General_CI_AS AS [PROJ_DESC] FROM [dbo].[utaprojectstage]
```

