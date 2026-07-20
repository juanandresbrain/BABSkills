# dbo.franchiseesalesplan

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseesalesplan"]
    dbo_franchiseesalesplan(["dbo.franchiseesalesplan"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseesalesplan |

## View Code

```sql
;

CREATE VIEW dbo.franchiseesalesplan AS SELECT SalesPlanID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SalesPlanID, Franchisee COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Franchisee, StoreID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS StoreID, FiscalYear COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FiscalYear, FiscalWeek COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FiscalWeek, PlannedSales, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BatchID FROM LH_Mart.dbo.franchiseesalesplan;;
```

