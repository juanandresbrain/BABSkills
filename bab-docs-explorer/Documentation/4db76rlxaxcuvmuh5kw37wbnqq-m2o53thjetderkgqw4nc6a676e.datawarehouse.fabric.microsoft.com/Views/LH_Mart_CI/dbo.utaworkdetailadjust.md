# dbo.utaworkdetailadjust

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkdetailadjust"]
    dbo_utaworkdetailadjust(["dbo.utaworkdetailadjust"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkdetailadjust |

## View Code

```sql
CREATE   VIEW [dbo].[utaworkdetailadjust] AS SELECT Wbt_ID, Wrkda_Work_Date, job_id, dept_id, Htype_ID, WRKDA_ID, wrkda_minutes, tcode_id, wrkda_adjust_date, InsertDate, UpdateDate, proj_ID FROM LH_Mart.dbo.utaworkdetailadjust;
```

