# dbo.utaworkdetail

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworkdetail"]
    dbo_utaworkdetail(["dbo.utaworkdetail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworkdetail |

## View Code

```sql
CREATE   VIEW [dbo].[utaworkdetail] AS SELECT Wrks_ID, Wrkd_ID, Wrkd_Start_Time, Wrkd_End_Time, Wrkd_Minutes, Wbt_ID, Tcode_ID, Htype_ID, Wrkd_Rate, Wrkd_Work_Date, Job_ID, Dept_ID, InsertDate, UpdateDate, proj_ID FROM LH_Mart.dbo.utaworkdetail;
```

