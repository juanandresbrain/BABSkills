# dbo.actualvearnedadjustedweeks

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.actualvearnedadjustedweeks"]
    dbo_actualvearnedadjustedweeks(["dbo.actualvearnedadjustedweeks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.actualvearnedadjustedweeks |

## View Code

```sql
;

CREATE VIEW dbo.actualvearnedadjustedweeks AS SELECT store COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS store, year, week, startDate, dpc, law, hoo, eqv, spp, msc, ffh, wbt_id FROM LH_Mart.dbo.actualvearnedadjustedweeks;;
```

