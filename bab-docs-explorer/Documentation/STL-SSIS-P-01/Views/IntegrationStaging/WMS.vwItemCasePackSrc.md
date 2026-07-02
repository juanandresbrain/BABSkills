# WMS.vwItemCasePackSrc

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwItemCasePackSrc"]
    WMS_ItemCasePackStage(["WMS.ItemCasePackStage"]) --> VIEW
    wms_ItemMaster(["wms.ItemMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ItemCasePackStage |
| wms.ItemMaster |

## View Code

```sql
CREATE VIEW [WMS].[vwItemCasePackSrc]
AS

WITH Styles AS (
select  im.ProductNumber,
		im.Entity
	from wms.ItemMaster im with (nolock) 
	where isnumeric(im.ProductNumber) = 1
		AND im.NecessaryProductionWorkingTimeSchedulingPropertyId <> 'Supplies'
		AND CAST(LEFT(im.ProductNumber,1) AS int) IN (0,8,9)
		AND im.Entity = '3001'
)
SELECT p.BaseId
	, p.StyleCode
	, p.OrderMultiple
	, p.DistribMultiple
	, p.ItemDesc
  FROM WMS.ItemCasePackStage p with(nolock) -- Imported from PLM HSE
  JOIN Styles s ON p.StyleCode = s.ProductNumber
```

