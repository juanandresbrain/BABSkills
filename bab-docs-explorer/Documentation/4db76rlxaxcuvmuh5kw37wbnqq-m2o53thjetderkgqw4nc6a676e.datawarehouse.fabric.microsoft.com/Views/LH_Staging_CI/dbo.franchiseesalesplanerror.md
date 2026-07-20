# dbo.franchiseesalesplanerror

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseesalesplanerror"]
    dbo_franchiseesalesplanerror(["dbo.franchiseesalesplanerror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseesalesplanerror |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseesalesplanerror]
AS
    SELECT [SalesPlanID] COLLATE Latin1_General_CI_AS AS [SalesPlanID], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [FiscalYear] COLLATE Latin1_General_CI_AS AS [FiscalYear], [FiscalWeek] COLLATE Latin1_General_CI_AS AS [FiscalWeek], [PlannedSales] COLLATE Latin1_General_CI_AS AS [PlannedSales], [InsertDate] COLLATE Latin1_General_CI_AS AS [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc], [ErrorSource] COLLATE Latin1_General_CI_AS AS [ErrorSource]
    FROM LH_Staging.[dbo].[franchiseesalesplanerror]
```

