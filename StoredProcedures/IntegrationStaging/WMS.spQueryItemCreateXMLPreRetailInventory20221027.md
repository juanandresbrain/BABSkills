# WMS.spQueryItemCreateXMLPreRetailInventory20221027

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spQueryItemCreateXMLPreRetailInventory20221027"]
    ERP_ItemLoadtoD365(["ERP.ItemLoadtoD365"]) --> SP
    wms_ItemMaster(["wms.ItemMaster"]) --> SP
    wms_ItemMasterProducts(["wms.ItemMasterProducts"]) --> SP
    WMS_ItemUOMStageForDynamics(["WMS.ItemUOMStageForDynamics"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.ItemLoadtoD365 |
| wms.ItemMaster |
| wms.ItemMasterProducts |
| WMS.ItemUOMStageForDynamics |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spQueryItemCreateXMLPreRetailInventory20221027]
@Entity varchar(4)




as

set nocount on

		select
			--=====VALUES WILL ALWAYS COME FROM MERCH=========================================================
			e.entity,
			e.ITEMNUMBER, 
			e.PRODUCTNUMBER, 
			e.PRODUCTDESCRIPTION,	
			e.PRODUCTNAME,	
			isnull(e.SEARCHNAME,'') as SEARCHNAME,
			isnull(e.HARMONIZEDSYSTEMCODE,'') as HARMONIZEDSYSTEMCODE,
			isnull(e.ORIGINCOUNTRYREGIONID,'') as ORIGINCOUNTRYREGIONID,
			--================================================================================================
			--=====VALUES WILL ALWAYS BE HARD-CODED===========================================================
			'Merchandise' as PRODUCTCATEGORYNAME, 
			'Procurement Categories' as PRODUCTCATEGORYHIERARCHYNAME, 
			'0' as UNDERDELIVERYPCT, 
			--case when e.ITEMMODELGROUPID='SERV' then 'Service' else 'Merch' end as 'PROPERTYID',
			'Merch' as PROPERTYID, 
			'0' as OVERDELIVERYPCT, 
			'MERCH' as ITEMGROUPID, 
			--case when e.ITEMMODELGROUPID='SERV' then 2 else 1 end as 'PRODUCTTYPE',
			'1' as PRODUCTTYPE,	
			'1' as PRODUCTSUBTYPE
			--================================================================================================
		into #UpdatesAndHardCoded
		FROM ERP.ItemLoadtoD365 e
		where 1=1
		and e.SendData = 1
		and e.Entity = @Entity
		

		
		select 
			--=====WILL SEND DATA PRODUCT DATA DOWNLOADED FROM DYNAMICS===================
			im.entity,
			im.ProductNumber,
			im.ItemNumber,
			im.PRODUCTSEARCHNAME,		
			case 
				when im.TRACKINGDIMENSIONGROUPNAME=''
					then NULL
				else im.TRACKINGDIMENSIONGROUPNAME
			end as TRACKINGDIMENSIONGROUPNAME,	
			case
				when im.STORAGEDIMENSIONGROUPNAME=''
					then NULL
				else im.STORAGEDIMENSIONGROUPNAME
			end as STORAGEDIMENSIONGROUPNAME,
			im.UNITCOSTQUANTITY, 	
			im.UNITCOST, 	
			im.SALESUNITSYMBOL,	
			im.SALESUNDERDELIVERYPERCENTAGE,	
			im.SALESPRICEQUANTITY,	
			im.SALESPRICE,
			im.SALESOVERDELIVERYPERCENTAGE,	
			im.PURCHASEUNITSYMBOL, 
			im.PURCHASEUNDERDELIVERYPERCENTAGE,	
			im.PURCHASEPRICEQUANTITY, 
			im.PURCHASEPRICE,	
			im.PURCHASEOVERDELIVERYPERCENTAGE,	
			case 
				when im.ITEMMODELGROUPID =''
					then NULL
				else im.ITEMMODELGROUPID
			end as ITEMMODELGROUPID,	
			im.INVENTORYUNITSYMBOL,
			case
				when im.ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED='yes'
					then 1
				else 0
			end as ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED,
			p.NMFCCODE,
			case 
				when p.ISPRODUCTKIT='yes' 
					then 1
				else 0
			end as ISPRODUCTKIT,
			case 
				when im.UNITCONVERSIONSEQUENCEGROUPID =''
					then NULL
				else im.UNITCONVERSIONSEQUENCEGROUPID
			end as UNITCONVERSIONSEQUENCEGROUPID,
			--im.UNITCONVERSIONSEQUENCEGROUPID,
			case 
				when im.WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2 = '' 
					then NULL 
				else im.WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2
			end as WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2,
			case 
				when im.PRODUCTGROUPID=''
					then NULL
				else im.PRODUCTGROUPID
			end as PRODUCTGROUPID, 
			case 
				when im.INVENTORYRESERVATIONHIERARCHYNAME=''
					then NULL
				else im.INVENTORYRESERVATIONHIERARCHYNAME
			end as INVENTORYRESERVATIONHIERARCHYNAME
			--============================================================================
		into #DynamicsData
		from wms.ItemMaster im 
		join wms.ItemMasterProducts p on im.ItemNumber=p.ProductNumber
		where 1=1
		and isnumeric(im.ItemNumber)=1
		and exists (select u.ProductNumber from #UpdatesAndHardCoded u where u.ProductNumber=p.ProductNumber and u.entity=im.entity)
		

		select  
			i.entity,
			i.ProductNumber,
			i.ProductName as 'PRODUCTNAME',
			i.ProductDescription as 'PRODUCTDESCRIPTION',
			isnull(i.SalesPrice,0) as 'SALESPRICE',
			isnull(i.PurchasePrice,0) as 'PURCHASEPRICE',
			i.ProductSearchName as 'PRODUCTSEARCHNAME',
			1 as 'PRODUCTTYPE',
			--case when i.ITEMMODELGROUPID='SERV' then 2 else 1 end as 'PRODUCTTYPE',
			'1' as 'PRODUCTSUBTYPE',
			i.HierarchyGroup as 'PRODUCTCATEGORYNAME',
			'Retail Product Hierarchy' as 'PRODUCTCATEGORYHIERARCHYNAME',
			'FAK70' as 'NMFCCODE',
			'0' as 'ISPRODUCTKIT',
			'NEW' as 'WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2',
			'1' as 'UNITCOSTQUANTITY',
			'0' as 'UNITCOST',
			--'EAIPCS' as 'UNITCONVERSIONSEQUENCEGROUPID',
			i.UNITCONVERSIONSEQUENCEGROUPID,
			'100' as 'UNDERDELIVERYPCT',
			'NONE' as 'TRACKINGDIMENSIONGROUPNAME',
			 --case when i.ITEMMODELGROUPID='SERV' then 'SERVICE' else 'BABWMS' end as 'STORAGEDIMENSIONGROUPNAME',
			 'BABWMS' as 'STORAGEDIMENSIONGROUPNAME',
			'EA' as 'SALESUNITSYMBOL',
			'100' as 'SALESUNDERDELIVERYPERCENTAGE',
			'1' as 'SALESPRICEQUANTITY',
			'0' as 'SALESOVERDELIVERYPERCENTAGE',
			'EA' as 'PURCHASEUNITSYMBOL',
			'100' as 'PURCHASEUNDERDELIVERYPERCENTAGE',
			'1' as 'PURCHASEPRICEQUANTITY',
			'0' as 'PURCHASEOVERDELIVERYPERCENTAGE',
			 --case when i.ITEMMODELGROUPID='SERV' then 'Service' else 'Merch' end as 'PROPERTYID',
			 'Merch' as 'PROPERTYID',
			'Merch' as 'PRODUCTGROUPID',
			'0' as 'OVERDELIVERYPCT',
			i.ITEMMODELGROUPID as 'ITEMMODELGROUPID',
			i.ITEMGROUP as 'ITEMGROUPID',
			'EA' as 'INVENTORYUNITSYMBOL',
			 --case when i.ITEMMODELGROUPID='SERV' then '' else 'BABW' end as 'INVENTORYRESERVATIONHIERARCHYNAME', 
			'BABW' as 'INVENTORYRESERVATIONHIERARCHYNAME',
			'1' as 'ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED',
			i.ItemNumber as 'ITEMNUMBER'
		into #OriginalNewAndHardCoded
		FROM ERP.ItemLoadtoD365 i
		join #UpdatesAndHardCoded u 
			on i.entity=u.entity
			and i.ProductNumber=u.ProductNumber
		group by 
			i.entity, 
			i.ProductNumber,
			i.ItemNumber,
			i.ProductName,
			i.ProductDescription,
			isnull(i.SalesPrice,0),
			isnull(i.PurchasePrice,0),
			i.ProductSearchName,
			--case when i.ITEMMODELGROUPID='SERV' then 2 else 1 end ,
			i.HierarchyGroup,
			i.ITEMMODELGROUPID,
			i.ITEMGROUP,
			i.UNITCONVERSIONSEQUENCEGROUPID
		
		


		select 
			--UPDATES AND HARD-CODES
			u.ProductNumber as PRODUCT_NUMBER,
			u.ITEMNUMBER,	
			u.PRODUCTNUMBER,	
			u.PRODUCTDESCRIPTION,	
			u.PRODUCTNAME,	
			u.SEARCHNAME,	
			u.HARMONIZEDSYSTEMCODE,	
			u.ORIGINCOUNTRYREGIONID,	
			u.PRODUCTCATEGORYNAME,	
			u.PRODUCTCATEGORYHIERARCHYNAME,	
			u.UNDERDELIVERYPCT,	
			u.PROPERTYID,	
			u.OVERDELIVERYPCT,	
			u.ITEMGROUPID,	
			u.PRODUCTTYPE,	
			u.PRODUCTSUBTYPE,	
			--IF NO DYNAMICS DATA, THEN ORIGINAL HARD-CODED
			cast(isnull(dd.PRODUCTSEARCHNAME,o.PRODUCTSEARCHNAME) as nvarchar(100)) as PRODUCTSEARCHNAME,
			cast(isnull(dd.TRACKINGDIMENSIONGROUPNAME,o.TRACKINGDIMENSIONGROUPNAME) as varchar(4)) as TRACKINGDIMENSIONGROUPNAME,	
			cast(isnull(dd.STORAGEDIMENSIONGROUPNAME,o.STORAGEDIMENSIONGROUPNAME) as varchar(6)) as STORAGEDIMENSIONGROUPNAME,	
			isnull(dd.UNITCOSTQUANTITY,o.UNITCOSTQUANTITY) as UNITCOSTQUANTITY,	
			isnull(dd.UNITCOST,o.UNITCOST) as UNITCOST,	
			cast(isnull(dd.SALESUNITSYMBOL,o.SALESUNITSYMBOL) as varchar(2)) as SALESUNITSYMBOL,	
			cast(isnull(dd.SALESUNDERDELIVERYPERCENTAGE,o.SALESUNDERDELIVERYPERCENTAGE) as int) as SALESUNDERDELIVERYPERCENTAGE,	
			isnull(dd.SALESPRICEQUANTITY,o.SALESPRICEQUANTITY) as SALESPRICEQUANTITY,	
			isnull(dd.SALESPRICE,o.SALESPRICE) as SALESPRICE,	
			cast(isnull(dd.SALESOVERDELIVERYPERCENTAGE,o.SALESOVERDELIVERYPERCENTAGE) as int) as SALESOVERDELIVERYPERCENTAGE,	
			cast(isnull(dd.PURCHASEUNITSYMBOL,o.PURCHASEUNITSYMBOL) as varchar(2)) as PURCHASEUNITSYMBOL,	
			cast(isnull(dd.PURCHASEUNDERDELIVERYPERCENTAGE,o.PURCHASEUNDERDELIVERYPERCENTAGE) as int) as PURCHASEUNDERDELIVERYPERCENTAGE,	
			isnull(dd.PURCHASEPRICEQUANTITY,o.PURCHASEPRICEQUANTITY) as PURCHASEPRICEQUANTITY,	
			isnull(dd.PURCHASEPRICE,o.PURCHASEPRICE) as PURCHASEPRICE,	
			cast(isnull(dd.PURCHASEOVERDELIVERYPERCENTAGE,o.PURCHASEOVERDELIVERYPERCENTAGE) as int) as PURCHASEOVERDELIVERYPERCENTAGE,	
			cast(isnull(dd.ITEMMODELGROUPID,o.ITEMMODELGROUPID) as varchar(7)) as ITEMMODELGROUPID,	
			cast(isnull(dd.INVENTORYUNITSYMBOL,o.INVENTORYUNITSYMBOL) as varchar(2)) as INVENTORYUNITSYMBOL,	
			isnull(dd.ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED,o.ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED) as ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED,	
			cast(isnull(dd.NMFCCODE,o.NMFCCODE) as varchar(5)) as NMFCCODE,	
			isnull(dd.ISPRODUCTKIT,o.ISPRODUCTKIT) as ISPRODUCTKIT,
			cast(isnull(dd.UNITCONVERSIONSEQUENCEGROUPID,o.UNITCONVERSIONSEQUENCEGROUPID) as varchar(10)) as UNITCONVERSIONSEQUENCEGROUPID,
			--cast(o.UNITCONVERSIONSEQUENCEGROUPID as varchar(10)) as UNITCONVERSIONSEQUENCEGROUPID,
			cast(isnull(dd.WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2,o.WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2) as varchar(10)) as WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2,
			cast(isnull(dd.PRODUCTGROUPID,o.PRODUCTGROUPID) as varchar(10)) as PRODUCTGROUPID, 
			cast(isnull(dd.INVENTORYRESERVATIONHIERARCHYNAME,o.INVENTORYRESERVATIONHIERARCHYNAME) as varchar(10)) as INVENTORYRESERVATIONHIERARCHYNAME
		into #Prestage
		from #UpdatesAndHardCoded u
		left join #DynamicsData dd 
			on u.entity=dd.entity
			and u.ProductNumber=dd.ItemNumber
		join #OriginalNewAndHardCoded o 
			on u.entity=o.entity
			and u.ProductNumber=o.ProductNumber
		
		
		select 
			PRODUCTTYPE,	--UPDATES NOT ALLOWED - If inventory item 1							 -------->>PRESENTLY HARD CODED TO 1
			PRODUCTSUBTYPE,	--UPDATES NOT ALLOWED -- HARD-CODED TO 1							---------->>PRESENTLY HARD CODED TO 1
			PRODUCTSEARCHNAME,																	------------->>>PRESENTLY DYNAMICS DATA ELSE VALUE FROM ERP.ItemLoadtoD365 (me_01..style.long_desc)
			PRODUCTNAME,	--UPDATES ALLOWED															-->>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (me_01..style.long_desc)
			PRODUCTDESCRIPTION,	--UPDATES ALLOWED												------------>>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (me_01..style.long_desc)
			PRODUCTCATEGORYNAME,	--UPDATES ALLOWED --Hardcoded to Merchandise				---------->>PRESENTLY USING Merchandise
			PRODUCTCATEGORYHIERARCHYNAME,	--UPDATES NOT ALLOWED -- Hardcoded to  Procurement Catagory ----->>PRESENTLY USING 'Procurement Categories'
			NMFCCODE,	--UPDATES ALLOWED --Hardcoded to FAK70									----------->>PRESENTLY USING DYNAMICS, ELSE FAK70
			ISPRODUCTKIT,																		--------->>PRESENTLY USING DYNAMICS, ELSE '0'
			HARMONIZEDSYSTEMCODE,	--UPDATES ALLOWED											---------->>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (cast(left(substring(isnull(att.attribute_set_label,''),1,12), 7) as varchar(7)) for attributes UKTRF, USTRF)
			PRODUCTNUMBER,	--UPDATES NOT ALLOWED												---------->>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (me_01..style.style_code)
			PRODUCT_NUMBER,	--not really used
			WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2,	--updates not allowed -- Hardcoded to NEW   ------------->>>PRESENTLY DYNAMICS DATA ELSE 'NEW'
			UNITCOSTQUANTITY,	--UPDATES NOT ALLOWED -- Hardcoded to 1							------------->>>PRESENTLY DYNAMICS DATA ELSE '1'
			cast(UNITCOST as numeric(38,2)) as UNITCOST,	--UPDATES NOT ALLOWED				------------->>>PRESENTLY DYNAMICS DATA ELSE '0'
			UNITCONVERSIONSEQUENCEGROUPID,	--UPDATES NOT ALLOWED --						------ ------------->>>PRESENTLY DYNAMICS DATA ELSE VALUE FROM ERP.ItemLoadtoD365 -- (case 	when isnull(s.order_multiple,0)=isnull(s.distribution_multiple,0) then 'EACS' else 'EAIPCS'
			--------^^^^^^^^^^^^^^^If Order Multiple = Distribution Multiple -- EACS ------If Order Multiple ≠ Distribution Multiple --EAIPCS
			cast('100' as int) as UNDERDELIVERYPCT,	--UPDATES NOT ALLOWED -- Hardcoded to 100 --- ------------>>PRESENTLY HARD CODED AS '100'
			TRACKINGDIMENSIONGROUPNAME,	--UPDATES NOT ALLOWED -- Hardcoded to None					------------->>>PRESENTLY DYNAMICS DATA ELSE 'NONE'
			STORAGEDIMENSIONGROUPNAME,	--UPDATES NOT ALLOWED -- If inventory item BABWMS			------------->> PRESENTLY DYNAMICS DATA ELSE 'BABWMS' 
			SEARCHNAME,	--UPDATES ALLOWED															------------->>	PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (me_01..style.long_desc)
			SALESUNITSYMBOL,	--UPDATES NOT ALLOWED -- Hardcoded to EA							-------------->> PRESENTLY DYNAMICS ELSE 'EA'
			cast('100' as int) as SALESUNDERDELIVERYPERCENTAGE,	--UPDATES NOT ALLOWED --Hardcoded to 100 --------->>PRESENTLY HARD CODED AS '100'
			SALESPRICEQUANTITY,	--UPDATES NOT ALLOWED - - Hardcoded to 1							-------------->>PRESENTLY DYNAMICS ELSE '1'
			cast(SALESPRICE as numeric(38,2)) as SALESPRICE, --UPDATES NOT ALLOWED					-------------->>PRESENTLY DYNAMICS ELSE VALUE FROM ERP.ItemLoadtoD365 ( case when j.Entity = '1200' then (sr.current_selling_retail / 6.5) 	else sr.current_selling_retail
			cast('0' as int) as SALESOVERDELIVERYPERCENTAGE, --UPDATES NOT ALLOWED -- Hardcoded to 0 -------------->> PRESENTLY USING '0'
			PURCHASEUNITSYMBOL,	--UPDATES NOT ALLOWED - Hardcoded to EA									-------------->>PRESENTLY DYNAMICS ELSE 'EA'
			cast('100' as int) as PURCHASEUNDERDELIVERYPERCENTAGE,	--UPDATES NOT ALLOWED -- Hardcoded to 100 -------------->>PRESENTLY USING '100'
			PURCHASEPRICEQUANTITY,	--UPDATES NOT ALLOWED - Hardcoded to 1								-------------->>PRESENTLY DYNAMICS ELSE '1'
			cast(PURCHASEPRICE as numeric(38,2)) as PURCHASEPRICE, --UPDATES ALLOWED					-------------->>PRESENTLY DYNAMICS ELSE VALUE FROM ERP.ItemLoadtoD365 (me_01..style_vendor.current_price)
			cast('0' as int) as PURCHASEOVERDELIVERYPERCENTAGE,	--UPDATES NOT ALLOWED -- Hardcoded to 0 -------------->> PRESENTLY USING '0'
			PROPERTYID,	--UPDATES NOT ALLOWED															-------------->>PRESENTLY USING 'MERCH'	
			PRODUCTGROUPID,																				-------------->> PRESENTLY DYNAMICS ELSE 'MERCH'
			cast('0' as int) as OVERDELIVERYPCT,	--UPDATES NOT ALLOWED --  Hardcoded to 0			-------------->> PRESENTLY USING '0'
			ORIGINCOUNTRYREGIONID,	--UPDATES ALLOWED													-------------->> PRESENTLY VALUE FROM ERP.ItemLoadtoD365 (me_01..attribute.... 'COO')
			ITEMMODELGROUPID,	--UPDATES NOT ALLOWED -- If inventory item MOV_AVG						-------------->>>PRESENTLY USING DYNAMICS, ELSE VALUE FROM ERP.ItemLoadtoD365 (WHEN SERVIC ATTRIBUTE then 'SERV' else 'MOV-AVG'
			ITEMGROUPID,	---UPDATES NOT ALLOWED --  ------>>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 ----------->>> PRESENTLY USING 'MERCH'
		----^^^^^^^^^If gift card item GIFTCARD - If inventory item MERCH - If non-inventory item SERV --
			INVENTORYUNITSYMBOL,	---UPDATES NOT ALLOWED -- SHOULD BE HARD-CODED AS EA					----------->> PRESENTLY USING VALUE FROM DYNAMICS, ELSE EA
			INVENTORYRESERVATIONHIERARCHYNAME,	--UPDATES NOT ALLOWED - If Inventory item BABW			--------------->> PRESENTLY USING DYNAMICS ELSE case when i.ITEMMODELGROUPID='SERV' then '' else 'BABW'
			ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED,	--UPDATES NOT ALLOWED -- Hardcoded to 1		--------------->> PRESENTLY DYNAMICS ELSE '1'
			ITEMNUMBER --UPDATES NOT ALLOWED															--------------->>PRESENTLY USING VALUE FROM ERP.ItemLoadtoD365 (ME_01..style.style_code)
		into #PS2
		from #PreStage
		where ItemNumber not in ('081678')


;
with

XMLStage (xml) as
	(
		select 
			ps.PRODUCTNUMBER as '@PRODUCTNUMBER',		
			ps.HARMONIZEDSYSTEMCODE as '@HARMONIZEDSYSTEMCODE',
			ps.ISPRODUCTKIT as '@ISPRODUCTKIT',
			ps.NMFCCODE as '@NMFCCODE',
			ps.PRODUCTDESCRIPTION as '@PRODUCTDESCRIPTION',
			ps.PRODUCTNAME as '@PRODUCTNAME',
			ps.PRODUCTSEARCHNAME as '@PRODUCTSEARCHNAME',
			ps.PRODUCTSUBTYPE as '@PRODUCTSUBTYPE',
			ps.PRODUCTTYPE as '@PRODUCTTYPE',
					(	
						select 	
							ps1.ProductNumber as '@PRODUCTNUMBER',
							ps1.PRODUCTCATEGORYNAME as '@PRODUCTCATEGORYNAME',	
							ps1.PRODUCTCATEGORYHIERARCHYNAME as '@PRODUCTCATEGORYHIERARCHYNAME',
							cast('0.000000' as numeric(7,6)) as '@DISPLAYORDER'
						--from #PreStage ps1
						from #PS2 ps1
						where ps1.ProductNumber=ps.ProductNumber
						for xml path('EcoResProductCategoryAssignmentEntity'), type
					),
			(
				select
					ps2.ITEMNUMBER as '@ITEMNUMBER',
					ps2.ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED as '@ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED',
					ps2.INVENTORYRESERVATIONHIERARCHYNAME as '@INVENTORYRESERVATIONHIERARCHYNAME',
					ps2.INVENTORYUNITSYMBOL as '@INVENTORYUNITSYMBOL',
					ps2.ITEMGROUPID as '@ITEMGROUPID',
					ps2.ITEMMODELGROUPID as '@ITEMMODELGROUPID',
					case when @Entity=3001 then '' else isnull(ps2.ORIGINCOUNTRYREGIONID,'') end as '@ORIGINCOUNTRYREGIONID',
					--ps2.ORIGINCOUNTRYREGIONID as '@ORIGINCOUNTRYREGIONID',
					cast('0' as numeric(38,4)) as '@OVERDELIVERYPCT',	
					ps2.PRODUCTNUMBER as '@PRODUCTNUMBER',
					ps2.PROPERTYID as '@PROPERTYID',	
					cast('0' as numeric(38,4)) as '@PURCHASEOVERDELIVERYPERCENTAGE',
					cast(ps2.PURCHASEPRICE as numeric(38,4)) as '@PURCHASEPRICE',
					cast(ps2.PURCHASEPRICEQUANTITY as numeric(38,4)) as '@PURCHASEPRICEQUANTITY',
					cast('100' as numeric(38,4)) as '@PURCHASEUNDERDELIVERYPERCENTAGE',
					ps2.PURCHASEUNITSYMBOL as '@PURCHASEUNITSYMBOL',	
					cast('0' as numeric(38,4)) as '@SALESOVERDELIVERYPERCENTAGE',
					cast(ps2.SALESPRICE as numeric(38,4)) as '@SALESPRICE',
					cast(ps2.SALESPRICEQUANTITY as numeric(38,4)) as '@SALESPRICEQUANTITY',
					cast('100' as numeric(38,4)) as '@SALESUNDERDELIVERYPERCENTAGE',
					ps2.SALESUNITSYMBOL as '@SALESUNITSYMBOL',
					ps2.SEARCHNAME as '@SEARCHNAME',
					ps2.STORAGEDIMENSIONGROUPNAME as '@STORAGEDIMENSIONGROUPNAME',
					ps2.TRACKINGDIMENSIONGROUPNAME as '@TRACKINGDIMENSIONGROUPNAME',
					cast('100' as numeric(38,4)) as '@UNDERDELIVERYPCT',
					ps2.UNITCONVERSIONSEQUENCEGROUPID as '@UNITCONVERSIONSEQUENCEGROUPID',
					cast(ps2.UNITCOST as numeric(38,4)) as '@UNITCOST',
					cast(ps2.UNITCOSTQUANTITY as numeric(38,4)) as '@UNITCOSTQUANTITY',
					ps2.WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2 as '@WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2',
						( --UOM - ONLY INCLUDE ON THE FIRST PASS / ITEM CREATE
								select 
									cast(uom.style_code as varchar(6)) as '@PRODUCTNUMBER',
									uom.FROMUNITSYMBOL as '@FROMUNITSYMBOL',
									uom.TOUNITSYMBOL as '@TOUNITSYMBOL',
									uom.DENOMINATOR as '@DENOMINATOR',
									uom.FACTOR as '@FACTOR',
									'0.000000' as '@INNEROFFSET',
									'1' as '@NUMERATOR',
									'0.000000' as '@OUTEROFFSET',
									'0' as '@ROUNDING'
								from WMS.ItemUOMStageForDynamics uom with (nolock)
								where uom.style_code in (
															select e.ItemNumber
															from ERP.ItemLoadtoD365 e
															where 1=1
															and e.SendData = 1 --this is only set on insert or update
															and e.UpdateDate is null --this is only set on update, means this is the first time item is flowing
															and e.entity=1100
															and e.ItemNumber=ps.ProductNumber
															group by e.ItemNumber
														) --ONLY INCLUDE UOM IF THE ITEM IS NEW
								and uom.style_code=ps.ProductNumber
								--and uom.style_code='025855'
								for xml path ('EcoResProductSpecificUnitOfMeasureConversionEntity'), TYPE
						),
						(
							select NULL as '@x'
							for xml path ('WHSItemPhysicalDimensionDetailEntity'), TYPE
						)
					--from #PreStage ps2 
					from #PS2 ps2
					where ps2.ProductNumber=ps.ProductNumber
					for xml path('BABMerchItemCreateEcoResReleasedProductV2Entity'), TYPE
				)
		--from #PreStage ps
		from #PS2 ps
		where 1=1
		--and ps.ProductNumber in ('025855')
		for xml path ('BABMerchItemCreateEcoResProductV2Entity'), root('Document'), TYPE
	)
select cast(XML as xml) as XMLData
from XMLStage
;
```

