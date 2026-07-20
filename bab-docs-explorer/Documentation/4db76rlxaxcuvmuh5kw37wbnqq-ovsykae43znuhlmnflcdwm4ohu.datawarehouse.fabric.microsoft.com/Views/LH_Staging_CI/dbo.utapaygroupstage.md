# dbo.utapaygroupstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utapaygroupstage"]
    dbo_utapaygroupstage(["dbo.utapaygroupstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utapaygroupstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utapaygroupstage] AS SELECT [PayGrp_ID], [PayGrp_Name] COLLATE Latin1_General_CI_AS AS [PayGrp_Name] FROM [dbo].[utapaygroupstage]
```

