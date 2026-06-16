# ERP.spItemLoadReleasedProductsXML

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ERP.spItemLoadReleasedProductsXML"]
    ERP_ItemLoadtoD365(["ERP.ItemLoadtoD365"]) --> SP
    erp_ItemMaster(["erp.ItemMaster"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.ItemLoadtoD365 |
| erp.ItemMaster |

## Stored Procedure Code

```sql
CREATE proc [ERP].[spItemLoadReleasedProductsXML]
@Entity nvarchar(10)

as

-------------------------------------------------------------------------------
--2017-08-16	-	Dan Tweedie	- Created view to output ItemLoad XML for D365
-------------------------------------------------------------------------------
WITH
XMLStage (XMLData) as 
	(
		select 
			e.PURCHASEPRICE,
			e.INVENTORYUNITSYMBOL,
			e.ISPURCHASEPRICEAUTOMATICALLYUPDATED,
			e.ITEMMODELGROUPID,
			e.ITEMNUMBER,
			e.PRODUCTDESCRIPTION,
			e.PRODUCTGROUPID,
			e.PRODUCTNUMBER,
			e.PRODUCTSUBTYPE,
			e.PRODUCTTYPE,
			e.PURCHASEUNITSYMBOL,
			e.SALESUNITSYMBOL,
			e.SEARCHNAME,
			e.STORAGEDIMENSIONGROUPNAME,
			e.TRACKINGDIMENSIONGROUPNAME,
			e.SALESPRICE,
			e.UNITCONVERSIONSEQUENCEGROUPID,
			e.UNITCOST,
			e.UNITCOSTQUANTITY
		FROM ERP.ItemLoadtoD365 e
		where 
			e.Entity = @Entity 
			and 
			(
				e.SendData = 1
				or not exists (select distinct im.ProductNumber from erp.ItemMaster im where im.ItemNumber = e.ProductNumber and im.Entity = @Entity)
			)
		for xml path('EcoResReleasedProductEntity'), root('Document'), Type
	)
select XMLData
from XMLStage
```

