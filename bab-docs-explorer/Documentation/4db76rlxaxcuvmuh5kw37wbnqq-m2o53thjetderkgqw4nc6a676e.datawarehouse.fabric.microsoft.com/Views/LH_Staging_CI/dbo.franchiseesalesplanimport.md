# dbo.franchiseesalesplanimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseesalesplanimport"]
    dbo_franchiseesalesplanimport(["dbo.franchiseesalesplanimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseesalesplanimport |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseesalesplanimport]
AS
    SELECT [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [FiscalYear] COLLATE Latin1_General_CI_AS AS [FiscalYear], [FiscalWeek] COLLATE Latin1_General_CI_AS AS [FiscalWeek], [PlannedSales], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee]
    FROM LH_Staging.[dbo].[franchiseesalesplanimport]
```

