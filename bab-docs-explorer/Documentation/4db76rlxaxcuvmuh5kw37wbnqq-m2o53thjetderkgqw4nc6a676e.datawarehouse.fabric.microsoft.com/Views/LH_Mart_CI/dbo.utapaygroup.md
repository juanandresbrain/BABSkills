# dbo.utapaygroup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utapaygroup"]
    dbo_utapaygroup(["dbo.utapaygroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utapaygroup |

## View Code

```sql
;

CREATE VIEW dbo.utapaygroup AS SELECT PayGrp_ID, PayGrp_Name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PayGrp_Name, InsertDate, UpdateDate FROM LH_Mart.dbo.utapaygroup;
```

