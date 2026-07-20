# dbo.utaworkdetailadjuststage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkdetailadjuststage"]
    dbo_utaworkdetailadjuststage(["dbo.utaworkdetailadjuststage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkdetailadjuststage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworkdetailadjuststage] AS SELECT [Wbt_ID], [Wrkda_Work_Date], [job_id], [dept_id], [Htype_ID], [WRKDA_ID], [wrkda_minutes], [tcode_id], [wrkda_adjust_date], [proj_ID] FROM [dbo].[utaworkdetailadjuststage]
```

