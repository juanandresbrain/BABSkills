# dbo.utaworkdetailadjuststagerejects

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkdetailadjuststagerejects"]
    dbo_utaworkdetailadjuststagerejects(["dbo.utaworkdetailadjuststagerejects"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkdetailadjuststagerejects |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworkdetailadjuststagerejects] AS SELECT [Wbt_ID] COLLATE Latin1_General_CI_AS AS [Wbt_ID], [Wrkda_Work_Date] COLLATE Latin1_General_CI_AS AS [Wrkda_Work_Date], [Htype_ID] COLLATE Latin1_General_CI_AS AS [Htype_ID], [WRKDA_ID] COLLATE Latin1_General_CI_AS AS [WRKDA_ID], [wrkda_minutes] COLLATE Latin1_General_CI_AS AS [wrkda_minutes], [tcode_id] COLLATE Latin1_General_CI_AS AS [tcode_id], [wrkda_adjust_date] COLLATE Latin1_General_CI_AS AS [wrkda_adjust_date], [ErrorCode], [ErrorColumn], [RejectDate], [proj_id] FROM [dbo].[utaworkdetailadjuststagerejects]
```

