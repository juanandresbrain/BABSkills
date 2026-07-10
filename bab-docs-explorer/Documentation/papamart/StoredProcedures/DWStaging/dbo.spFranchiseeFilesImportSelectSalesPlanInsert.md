# dbo.spFranchiseeFilesImportSelectSalesPlanInsert

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spFranchiseeFilesImportSelectSalesPlanInsert"]
    dbo_FranchiseeSalesPlan(["dbo.FranchiseeSalesPlan"]) --> SP
    FranchiseeSalesPlanImport(["FranchiseeSalesPlanImport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FranchiseeSalesPlan |
| FranchiseeSalesPlanImport |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spFranchiseeFilesImportSelectSalesPlanInsert]
@Franchisee varchar(2)

as

set nocount on;

--Per the specification guide, 
--		Sales plan file should be submitted once per year to set the annual baseline sales plan by week and store.  
--		Revisions to the plan should be submitted on a weekly basis.  
--		This code will delete records by Franchisee, FiscalYear, FiscalWeek and StoreID, based on the existance of new data in the file

WITH 
DWSalesPlan (SalesPlanID)
AS (
	select distinct dw.SalesPlanID
	from DW.dbo.FranchiseeSalesPlan dw with (nolock)
	join FranchiseeSalesPlanImport i with (nolock)
		on cast (concat(dw.Franchisee, dw.FiscalYear, dw.FiscalWeek, dw.StoreID ) as varchar(25)) = cast (concat(i.Franchisee, i.FiscalYear, i.FiscalWeek, i.StoreID ) as varchar(25))
		--cast ( (s.Franchisee + s.FiscalYear + s.FiscalWeek + s.StoreID + convert(varchar, s.InsertDate, 112) ) as varchar(25) )
   ) 
Delete from DW.dbo.FranchiseeSalesPlan
where SalesPlanID in (select SalesPlanID from DWSalesPlan);


--WITH
--Errors (StoreID, FiscalYear, FiscalWeek)
--as (
--	select StoreID, FiscalYear, FiscalWeek from FranchiseeSalesPlanError with (nolock) where Franchisee = @Franchisee
--   )
select 
	  -- cast (
			--(
			--   s.Franchisee
			--   + s.FiscalYear
			--   + s.FiscalWeek
			--   + s.StoreID
			--   + convert(varchar, s.InsertDate, 112)
			--) as varchar(25) ) as SalesPlanID,
	   cast (concat(s.Franchisee, s.FiscalYear, s.FiscalWeek, s.StoreID) as varchar(25)) as SalesPlanID,
	   s.StoreID,
	   s.FiscalYear,
	   s.FiscalWeek,
	   s.PlannedSales,
	   s.InsertDate,
	   s.Franchisee
from FranchiseeSalesPlanImport s with (nolock)
where s.Franchisee = @Franchisee
--and not exists (select e.StoreID, e.FiscalYear, e.FiscalWeek from Errors e where s.StoreID = e.StoreID and s.FiscalYear = e.FiscalYear and s.FiscalWeek = s.FiscalWeek)
order by 2,3,1
```

