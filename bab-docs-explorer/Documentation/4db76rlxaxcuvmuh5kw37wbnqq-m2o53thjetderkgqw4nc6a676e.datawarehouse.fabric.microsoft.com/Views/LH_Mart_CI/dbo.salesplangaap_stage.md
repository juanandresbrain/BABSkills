# dbo.salesplangaap_stage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.salesplangaap_stage"]
    dbo_salesplangaap_stage(["dbo.salesplangaap_stage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.salesplangaap_stage |

## View Code

```sql
;

CREATE VIEW dbo.salesplangaap_stage AS SELECT store, actual_date, currency COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS currency, sales_plan FROM LH_Mart.dbo.salesplangaap_stage;;
```

