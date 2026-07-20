# dbo.laborcredits

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.laborcredits"]
    dbo_laborcredits(["dbo.laborcredits"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.laborcredits |

## View Code

```sql
;

CREATE VIEW dbo.laborcredits AS SELECT DateSubmitted, StoreNumber, Month COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Month, WeekNumber, Credit, Reason COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Reason, RequestedBy COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS RequestedBy, InsertDate, UpdateDate FROM LH_Mart.dbo.laborcredits;;
```

