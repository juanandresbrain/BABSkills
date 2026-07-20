# dbo.tmp_franchiseefilesimportselectsalesplaninsert_cl

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselectsalesplaninsert_cl"]
    dbo_tmp_franchiseefilesimportselectsalesplaninsert_cl(["dbo.tmp_franchiseefilesimportselectsalesplaninsert_cl"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselectsalesplaninsert_cl |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselectsalesplaninsert_cl] AS SELECT [SalesPlanID] COLLATE Latin1_General_CI_AS AS [SalesPlanID], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [FiscalYear] COLLATE Latin1_General_CI_AS AS [FiscalYear], [FiscalWeek] COLLATE Latin1_General_CI_AS AS [FiscalWeek], [PlannedSales], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[tmp_franchiseefilesimportselectsalesplaninsert_cl]
```

