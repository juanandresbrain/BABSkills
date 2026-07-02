# WEB.vwStoreInventoryCSV

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwStoreInventoryCSV"]
    WEB_InventoryFact(["WEB.InventoryFact"]) --> VIEW
    Web_LocationStage(["Web.LocationStage"]) --> VIEW
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> VIEW
    WEB_StoreInventoryBuffers(["WEB.StoreInventoryBuffers"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.InventoryFact |
| Web.LocationStage |
| WEB.ProductCatalogMasterAttributes |
| WEB.StoreInventoryBuffers |

## View Code

```sql
CREATE view [WEB].[vwStoreInventoryCSV]

as

--------------------------------------------------------------------------------------------------
--Dan Tweedie	2020-04-09	Created View for sending Store Inventory to Deck for Buy Online / Ship from Store.
--Lizzy Timm	2024-02-20	Added date filter to Buffers CTE.
--							Note that location exclusion requests come from the business; reach out to Kasey or StoreOps instead of Stacey or Digital
---------------------------------------------------------------------------------------------------

with 
Buffers as
	(
		select 
			pcma.UPC as GTIN,
			invF.LocationCode,
			invF.StyleCode,
			invF.SKUDescription,
			invF.UnbufferedQty,
			isnull(isnull(isnull(StoreSku.BufferQty,StoreDept.BufferQty),Dept.BufferQty),pcma.InventoryBuffer) as StoreInventoryBuffer
		from WEB.InventoryFact invF with (nolock)
		join WEB.ProductCatalogMasterAttributes pcma with (nolock) on invF.StyleCode=pcma.BABWProductID and pcma.StoreFrontEligible = 1
		left join WEB.StoreInventoryBuffers StoreSku with (nolock) 
			on cast(invF.LocationCode as int)=StoreSku.StoreNumber
			and cast(invF.StyleCode as int)=cast(StoreSku.ItemNumber as int)
			and invF.LocationCode not in ('0013','2013')
		left join WEB.StoreInventoryBuffers StoreDept with (nolock) 
			on cast(invF.LocationCode as int)=StoreDept.StoreNumber
			and left(pcma.HierarchyGroupCode,8)=StoreDept.Department
			and invF.LocationCode not in ('0013','2013')
		left join WEB.StoreInventoryBuffers Dept with (nolock) 
			on left(pcma.HierarchyGroupCode,8)=Dept.Department
			and Dept.StoreNumber is NULL
			and Dept.ItemNumber is NULL
			and invF.LocationCode not in ('0013','2013')
		WHERE
			-- isnull(invF.UpdateDate,invF.InsertDate) >= dateadd(dd,-7, getdate())
			(
				datepart(hh, getdate()) = 0
				--AND datepart(mi, getdate()) < 30
				AND isnull(invF.UpdateDate, invF.InsertDate) >= dateadd(dd, - 7, getdate())
				)
			OR (
				datepart(hh, getdate()) <> 0
				-- AND datepart(mi, getdate()) > 30
				AND isnull(invF.UpdateDate, invF.InsertDate) >= dateadd(hh, - 1, getdate())
				)
			OR invF.UnbufferedQty >= 99999

	),
Inventory as
	(
		select 
			GTIN,
			case 
				when (UnbufferedQty - StoreInventoryBuffer) <0
					then 0
				else (UnbufferedQty - StoreInventoryBuffer)
			end as Qty,
			LocationCode,
			StyleCode,
			SKUDescription
		from Buffers
	)
select 
	cast(i.GTIN as nvarchar) as 'GTIN',
	cast(sum(i.QTY) as int) as 'TotalQuantity',
	cast(0 as int) as 'ProtectedQuantity',
	cast(i.LocationCode as nvarchar) as 'WarehouseCode',
	cast(i.StyleCode as nvarchar) as 'CustomerSKU',
	cast(i.StyleCode as nvarchar) as 'ProductCode',
	cast(left(i.SKUDescription, 50) as nvarchar) as 'Attribute1',
	cast(0 as nvarchar) as PreBackOrderQuantity, 
	convert(nvarchar, getdate(), 121) as InStockDateUTC, 
	cast('' as nvarchar) as InventoryType
from Inventory i
where isnull(i.GTIN,'') <> ''
and i.LocationCode not in ('0013', '2013','2019','2079','2080') -- no getting good inventory for the stores '2019','2079','2080'
and i.StyleCode not in ('089173', '080187','081678') --gala tickets
and exists (select wl.Code from Web.LocationStage wl where wl.Code=i.LocationCode)
and i.LocationCode not in --PER ART 12/31/2024
	(
		'0018',
		--'0091',
		--'0212',
		'0244',
		'0274',
		'0327',
		--'0354',
		'0355',
		'0356',
		--'0385',
		'0416',
		'0417',
		'0530',
		'0528',
		'0550',
		'0552'
		--,'0567'
	)
and i.LocationCode not in --PER STACEY K 2025-02-05
	(
		'0805',
		'0801',
		'0548',
		'0806',
		'0812',
		'0804',
		'0813',
		'0803',
		'0568',
		'0810',
		'0437',
		--'0562',
		'0569',
		'0807',
		'0547',
		'0478',
		'2083',
		'0545',
		'0546',
		'0558',
		'0570',
		'2082',
		'2088',
		'0476',
		'0802',
		'0575',
		'0800',
		'0477',
		--'0561',
		'0811',
		'2087',
		'0809',
		'0816',
	--	'0572',
		'0814',
		'0808'--,
	--	'0566',
	--	'2081'
	)
and i.LocationCode not in --PER STACEY K 2025-02-12
	(
		--'0001',
		--'0032',
		--'0034',
		--'0077',
		--'0089',
		--'0105',
		--'0115',
		--'0123',
		--'0132',
		--'0142',
		--'0162',
		--'0167',
		--'0173',
		--'0178',
		--'0181',
		'0202',
		--'0206',
		--'0207',
		--'0222',
		--'0245',
	--	'0247',
	--	'0253',
	--	'0264',
	--	'0278',
	--	'0286',
	--	'0294',
	--	'0297',
	--	'0298',
	--	'0299',
	--	'0324',
	--	'0350',
		'0351',
		--'0363',
	--	'0603',
		--'0610',
		--'0613',
		--'0614',
		'0619',
		--'0218',
		--'0361',
	--	'0364',
	--	'0366',
		--'0368',
	--	'0370',
	--	'0382',
		--'0371',
	--	'0402',
		'0411',
		--'0407',
	--	'0415',
	--	'0422',
	--	'0447',
	--	'0448',
	--	'0451',
	--	'0452',
	--	'0453',
	--	'0459',
	--	'0526',
		--'0449',
		--'0441',
		'0527',
		'0539'--,
		--'0549',
		--'0553',
		--'0554'
	)
	and i.LocationCode not in ('0817')--PER STACEY K 2025-06-03
	and i.LocationCode not in ('2081','2085')--PER STACEY K 2025-09-10
group by 
	i.GTIN,
	i.LocationCode,
	i.StyleCode,
	i.StyleCode,
	left(i.SKUDescription, 50)
```

