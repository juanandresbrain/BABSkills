# dbo.utaemployee

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaemployee"]
    dbo_utaemployee(["dbo.utaemployee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaemployee |

## View Code

```sql
;

CREATE VIEW dbo.utaemployee AS SELECT Emp_ID, Emp_Fullname COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Emp_Fullname, Emp_Name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Emp_Name, Calcgrp_ID, Emp_Base_Rate, InsertDate, UpdateDate FROM LH_Mart.dbo.utaemployee;;
```

