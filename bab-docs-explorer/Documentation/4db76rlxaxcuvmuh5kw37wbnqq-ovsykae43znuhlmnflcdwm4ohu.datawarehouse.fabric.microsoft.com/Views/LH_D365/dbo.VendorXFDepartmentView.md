# dbo.VendorXFDepartmentView

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VendorXFDepartmentView"]
    dbo_VendorNameView(["dbo.VendorNameView"]) --> VIEW
    dbo_d365LocationMapping_View(["dbo.d365LocationMapping_View"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_inventdim(["dbo.inventdim"]) --> VIEW
    dbo_product_dim_le(["dbo.product_dim_le"]) --> VIEW
    dbo_purchline(["dbo.purchline"]) --> VIEW
    dbo_purchtable(["dbo.purchtable"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.VendorNameView |
| dbo.d365LocationMapping_View |
| dbo.date_dim |
| dbo.inventdim |
| dbo.product_dim_le |
| dbo.purchline |
| dbo.purchtable |

## View Code

```sql
/****** Object:  View [dbo].[VendorXFDepartmentView]    Script Date: 2/27/2026 2:46:45 PM ******/ /****** Object:  View [dbo].[VendorXFDepartmentView]    Script Date: 2/25/2026 10:47:36 PM ******/   CREATE   VIEW [dbo].[VendorXFDepartmentView]   AS  with src as (  select YEAR(purchline.babshipdate) as 'Year',  		pd.departmentLabel as DepartmentLabel, 		pd.departmentLabel 		+ ' ' + 		LEFT(         SUBSTRING(pd.department, CHARINDEX('(', pd.department) + 1, LEN(pd.department)),         CHARINDEX('-', SUBSTRING(pd.department, CHARINDEX('(', pd.department) + 1, LEN(pd.department)) + '-') - 1) AS DeptFormatted, 		MONTH(purchline.babshipdate) as 'Month', 		purchline.purchqty as 'PurchQty', 		purchline.lineamount as 'TotalCost', 		pd.current_retail * purchline.purchqty as 'TotalRetail'     FROM         LH_D365.dbo.purchline purchline         INNER JOIN LH_D365.dbo.purchtable purchtable ON purchtable.purchid = purchline.purchid AND purchtable.dataareaid = purchline.dataareaid 		INNER JOIN LH_MART.dbo.date_dim  dd on dd.actual_date = purchline.babshipdate         INNER JOIN dbo.inventdim idm ON purchline.inventdimid = idm.inventdimid And purchline.dataareaid = idm.dataareaid         INNER JOIN LH_D365.dbo.VendorNameView vendorName ON vendorName.accountnum = purchtable.invoiceaccount AND vendorName.dataareaid = purchline.dataareaid         LEFT JOIN dbo.d365LocationMapping_View locationMapping ON idm.inventlocationid = locationMapping.inventlocationid AND locationMapping.legalentity = purchline.dataareaid         LEFT JOIN LH_D365.dbo.product_dim_le pd ON pd.style_code = purchline.itemid AND pd.jurisdiction_code = locationMapping.JurisidictionCode And purchline.dataareaid = pd.LegalEntity      WHERE         purchline.createddatetime >= DATEADD(MONTH, -48, GETDATE())  		and pd.department is not null 		and purchline.babshipdate is not null 		and purchline.babshipdate != '1900-01-01 00:00:00.000000' 		and purchline.babshipdate >= DATEADD(MONTH, -48, GETDATE()) 		and dd.date_key != '0' 		and dd.date_key != '-99'	 		and purchline.purchstatus <> 4 -- exclude cancelled POs 		and purchtable.intercompanyorder = 0 -- only non-intercompany orders   		)  		select [Year],case when grouping(DepartmentLabel) = 1 then 'All Departments' else DepartmentLabel end as DepartmentLabel, 			case when grouping(DepartmentLabel) = 1 and grouping(DeptFormatted) = 1 then 'All Departments' else DeptFormatted end as 'DepartmentName', 			cast(case when grouping(DepartmentLabel) = 1 and grouping (DeptFormatted) = 1 then 0 else 1 end as int) as 'DeptSortKey', 			FLOOR(sum(case when [Month] = 1 then PurchQty else 0 end)) as 'Jan', 			FLOOR(sum(case when [Month] = 2 then PurchQty else 0 end)) as 'Feb', 			FLOOR(sum(case when [Month] = 3 then PurchQty else 0 end)) as 'Mar', 			FLOOR(sum(case when [Month] = 4 then PurchQty else 0 end))  as 'Apr', 			FLOOR(sum(case when [Month] = 5 then PurchQty else 0 end))  as 'May', 			FLOOR(sum(case when [Month] = 6 then PurchQty else 0 end))  as 'Jun', 			FLOOR(sum(case when [Month] = 7 then PurchQty else 0 end))  as 'Jul', 			FLOOR(sum(case when [Month] = 8 then PurchQty else 0 end)) as 'Aug', 			FLOOR(sum(case when [Month] = 9 then PurchQty else 0 end))  as 'Sep', 			FLOOR(sum(case when [Month] = 10 then PurchQty else 0 end)) as 'Oct', 			FLOOR(sum(case when [Month] = 11 then PurchQty else 0 end)) as 'Nov', 			FLOOR(sum(case when [Month] = 12 then PurchQty else 0 end))  as 'Dec', 			FLOOR(sum(case when [Month] in (1,2,3) then PurchQty else 0 end))  as 'QTR1', 			FLOOR(sum(case when [Month] in (4,5,6) then PurchQty else 0 end))  as 'QTR2', 			FLOOR(sum(case when [Month] in (7,8,9) then PurchQty else 0 end)) as 'QTR3', 			FLOOR(sum(case when [Month] in (10,11,12) then PurchQty else 0 end))  as 'QTR4', 			FLOOR(sum(PurchQty))  as 'Total Year', 			FLOOR(sum(TotalCost)) as 'Total Cost', 			FLOOR(sum(TotalRetail)) as 'Total Retail', 			case when nullif(sum(TotalRetail),0) IS NULL THEN 0 ELSE (FLOOR(SUM(TotalRetail)) - FLOOR(SUM(TotalCost))) / FLOOR(SUM(TotalRetail)) end as 'MU'     FROM         src  	group by grouping sets (([Year],DepartmentLabel,DeptFormatted), 			([Year]) );
```

