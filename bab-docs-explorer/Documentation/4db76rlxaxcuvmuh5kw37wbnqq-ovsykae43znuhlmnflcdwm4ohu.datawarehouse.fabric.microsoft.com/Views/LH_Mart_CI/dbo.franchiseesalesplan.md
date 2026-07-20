# dbo.franchiseesalesplan

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[franchiseesalesplan] AS     SELECT [SalesPlanID] COLLATE Latin1_General_CI_AS AS [SalesPlanID], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [FiscalYear] COLLATE Latin1_General_CI_AS AS [FiscalYear], [FiscalWeek] COLLATE Latin1_General_CI_AS AS [FiscalWeek], [PlannedSales], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID]     FROM [dbo].[franchiseesalesplan]
```

