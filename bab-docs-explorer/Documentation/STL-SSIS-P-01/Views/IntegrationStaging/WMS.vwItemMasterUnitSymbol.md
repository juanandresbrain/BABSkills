# WMS.vwItemMasterUnitSymbol

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwItemMasterUnitSymbol"]
    WMS_ItemMaster(["WMS.ItemMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ItemMaster |

## View Code

```sql
CREATE VIEW [WMS].[vwItemMasterUnitSymbol]
AS
SELECT       ISNULL(ROW_NUMBER() OVER(ORDER BY ProductNumber), -1) AS ItemMasterID
            ,ProductNumber
			,InventoryUnitSymbol
			,Entity
FROM            WMS.ItemMaster

WMS,vwItemsCompareMerchvsDynamics,CREATE view WMS.vwItemsCompareMerchvsDynamics

as

With 
PreDynamics as --staged to load to dynamics
	(
		select 
			entity,
			ItemNumber,
			HarmonizedSystemCode,
			OriginCountryRegionID,
			PropertyID,
			NMFCCode
		from erp.ItemLoadtoD365 
	),
PostDynamics as --captured from dynamics... should be same as what was staged...
	(
		select 
			im.entity,
			p.ProductNumber,
			p.HarmonizedSystemCode,
			im.OriginCountryRegionID,
			im.NecessaryProductionWorkingTimeSchedulingPropertyId,
			p.nmfcCode
		from wms.ItemMasterProducts p with (nolock) 
		join wms.ItemMaster im with (nolock) on p.ProductNumber=im.ProductNumber
	)
select 
	pd.entity StagedEntity,
	pd.ItemNumber StagedItem,
	pd.HarmonizedSystemCode StagedHTS,
	pd.OriginCountryRegionID StagedCOO,
	pd.PropertyID StagedMerchVsSupplies,
	pd.NMFCCode StagedNMFC,
	pod.entity as DynamicsEntity,
	pod.ProductNumber DynamicsItemNumber,
	pod.HarmonizedSystemCode DynamicsHTS,
	pod.OriginCountryRegionID DynamicsCOO,
	pod.NecessaryProductionWorkingTimeSchedulingPropertyId DynamicsMerchVsSupplies,
	pod.nmfcCode DynamicsNMFC
from PreDynamics pd 
left join PostDynamics pod 
	on pd.entity=pod.entity
	and pd.ItemNumber=pod.ProductNumber
where pod.ProductNumber is null
or
	(
		pd.HarmonizedSystemCode is not null and pd.HarmonizedSystemCode <> isnull(pod.HarmonizedSystemCode,'')
		or
		isnull(pd.OriginCountryRegionID,'')<>isnull(pod.OriginCountryRegionID,'')
		or
		isnull(pd.PropertyID,'')<>isnull(pod.NecessaryProductionWorkingTimeSchedulingPropertyId,'')
		or
		isnull(pd.NMFCCode,'')<>isnull(pod.nmfcCode,'')
	)
```

