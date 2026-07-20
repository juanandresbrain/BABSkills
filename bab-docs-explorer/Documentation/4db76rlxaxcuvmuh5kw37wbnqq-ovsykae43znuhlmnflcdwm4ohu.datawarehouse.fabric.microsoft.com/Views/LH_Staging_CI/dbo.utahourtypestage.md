# dbo.utahourtypestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utahourtypestage"]
    dbo_utahourtypestage(["dbo.utahourtypestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utahourtypestage |

## View Code

```sql
; CREATE   VIEW [dbo].[utahourtypestage] AS SELECT [Htype_ID], [Htype_Name] COLLATE Latin1_General_CI_AS AS [Htype_Name] FROM [dbo].[utahourtypestage]
```

