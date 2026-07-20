# dbo.utaworkbrainteamstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkbrainteamstage"]
    dbo_utaworkbrainteamstage(["dbo.utaworkbrainteamstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkbrainteamstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworkbrainteamstage] AS SELECT [WBT_ID], [WBT_NAME] COLLATE Latin1_General_CI_AS AS [WBT_NAME], [WBT_PARENT_ID], [wbt_lft], [wbt_rgt] FROM [dbo].[utaworkbrainteamstage]
```

