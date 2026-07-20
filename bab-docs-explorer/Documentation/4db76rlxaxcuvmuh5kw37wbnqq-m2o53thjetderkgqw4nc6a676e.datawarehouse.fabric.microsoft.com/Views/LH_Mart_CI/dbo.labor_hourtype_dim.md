# dbo.labor_hourtype_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.labor_hourtype_dim"]
    dbo_labor_hourtype_dim(["dbo.labor_hourtype_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_hourtype_dim |

## View Code

```sql
;

CREATE VIEW dbo.labor_hourtype_dim AS SELECT HourType_key, descr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS descr, abrv COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS abrv, wb_cd COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS wb_cd, isPaid, MULTPLIER, INS_DT, UPD_DT, ETL_LOG_ID, ETL_EVNT_ID FROM LH_Mart.dbo.labor_hourtype_dim;
```

