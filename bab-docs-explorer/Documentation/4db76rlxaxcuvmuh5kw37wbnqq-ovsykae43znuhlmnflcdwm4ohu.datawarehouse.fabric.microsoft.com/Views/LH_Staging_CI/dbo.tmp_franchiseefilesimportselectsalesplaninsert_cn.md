# dbo.tmp_franchiseefilesimportselectsalesplaninsert_cn

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselectsalesplaninsert_cn"]
    dbo_tmp_franchiseefilesimportselectsalesplaninsert_cn(["dbo.tmp_franchiseefilesimportselectsalesplaninsert_cn"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselectsalesplaninsert_cn |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselectsalesplaninsert_cn] AS SELECT [SalesPlanID] COLLATE Latin1_General_CI_AS AS [SalesPlanID], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [FiscalYear] COLLATE Latin1_General_CI_AS AS [FiscalYear], [FiscalWeek] COLLATE Latin1_General_CI_AS AS [FiscalWeek], [PlannedSales], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[tmp_franchiseefilesimportselectsalesplaninsert_cn]
```

