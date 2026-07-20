# dbo.utatimecodestagerejects

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utatimecodestagerejects"]
    dbo_utatimecodestagerejects(["dbo.utatimecodestagerejects"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utatimecodestagerejects |

## View Code

```sql
; CREATE   VIEW [dbo].[utatimecodestagerejects] AS SELECT [TCODE_ID] COLLATE Latin1_General_CI_AS AS [TCODE_ID], [TCODE_NAME] COLLATE Latin1_General_CI_AS AS [TCODE_NAME], [TCODE_DESC] COLLATE Latin1_General_CI_AS AS [TCODE_DESC], [ErrorCode], [ErrorColumn], [RejectDate] FROM [dbo].[utatimecodestagerejects]
```

