# dbo.utaworkbrainteam

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkbrainteam"]
    dbo_utaworkbrainteam(["dbo.utaworkbrainteam"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkbrainteam |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworkbrainteam] AS     SELECT [WBT_ID], [WBT_NAME] COLLATE Latin1_General_CI_AS AS [WBT_NAME], [WBT_PARENT_ID], [wbt_lft], [wbt_rgt], [InsertDate], [UpdateDate]     FROM [dbo].[utaworkbrainteam]
```

