# dbo.utacalcgroup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utacalcgroup"]
    dbo_utacalcgroup(["dbo.utacalcgroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utacalcgroup |

## View Code

```sql
;

CREATE VIEW dbo.utacalcgroup AS SELECT Calcgrp_ID, Calcgrp_Name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Calcgrp_Name, InsertDate, UpdateDate FROM LH_Mart.dbo.utacalcgroup;
```

