# dbo.utatimecodestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utatimecodestage"]
    dbo_utatimecodestage(["dbo.utatimecodestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utatimecodestage |

## View Code

```sql
; CREATE   VIEW [dbo].[utatimecodestage] AS SELECT [TCODE_ID], [TCODE_NAME] COLLATE Latin1_General_CI_AS AS [TCODE_NAME], [TCODE_DESC] COLLATE Latin1_General_CI_AS AS [TCODE_DESC] FROM [dbo].[utatimecodestage]
```

