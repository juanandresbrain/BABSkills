# dbo.utaworkdetailstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkdetailstage"]
    dbo_utaworkdetailstage(["dbo.utaworkdetailstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkdetailstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworkdetailstage] AS SELECT [Wrks_ID], [Wrkd_ID], [Wrkd_Start_Time], [Wrkd_End_Time], [Wrkd_Minutes], [Wbt_ID], [Tcode_ID], [Htype_ID], [Wrkd_Rate], [Wrkd_Work_Date], [Job_ID], [Dept_ID], [proj_ID] FROM [dbo].[utaworkdetailstage]
```

