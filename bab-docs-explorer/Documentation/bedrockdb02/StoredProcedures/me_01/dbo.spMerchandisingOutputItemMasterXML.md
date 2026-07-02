# dbo.spMerchandisingOutputItemMasterXML

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputItemMasterXML"]
    dbo_VW_WMItemMaster(["dbo.VW_WMItemMaster"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.VW_WMItemMaster |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputItemMasterXML]

as

-- =====================================================================================================
-- Name: spMerchandisingOutputItemMasterXML
--
-- Description:	Outputs XML files to WM for Item Master Bridge, only for new styles or styles updated 'today'
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/30/2015		Created proc
-- =====================================================================================================

set nocount on


--GET STYLE DATA, GROUP STYLES INTO GROUPS OF 5000 --the view only pulls styles updated 'today' but if the view needs to be modified for all styles, this ranking is necessary so the files are not too big for EIS
IF (Object_ID('tempdb..#ItemMaster') IS NOT NULL) DROP TABLE #ItemMaster
select a.*, 
	   case when a.rankID between 0 and 4000 then 1
			when a.rankID between 4001 and 8000 then 2
			when a.rankID between 8001 and 12000 then 3
			when a.rankID between 12001 and 16000 then 4
			when a.rankID between 16001 and 20000 then 5
			when a.rankID between 20001 and 24000 then 6
			when a.rankID between 24001 and 28000 then 7
			when a.rankID between 28001 and 32000 then 8
			when a.rankID between 32001 and 36000 then 9
			when a.rankID between 36001 and 40000 then 10
			when a.rankID between 40001 and 44000 then 11
		end as RankGroup
into #ItemMaster
from (select *, dense_rank() over (order by style) rankID
		from VW_WMItemMaster) as a
		
---LOOP THROUGH STYLE GROUPS, OUTPUT XML FILES IN GROUPS OF 5000
declare @query varchar(1000),
		@date varchar(52),
		@ItemMasterFile varchar(1000),
		@XMLout varchar(1000),
		@file_location varchar(1000),
		@file_destination varchar(1000),
		@server varchar(200),
		@database varchar(200),
		@bcp varchar(1000),
		@type varchar(1000),
		@delete varchar(1000),
		@move varchar(1000),
		@groups int,
		@rank varchar(2)

select @groups = count(distinct rankgroup) from #ItemMaster

while @groups > 0

BEGIN
	select @rank = min(RankGroup) from #ItemMaster

	---STORE XML DATA
	declare @xml xml

	select @xml = (select 
		co as [Item/SKUDefinition/Company], 
		div as [Item/SKUDefinition/Division],
		style as [Item/SKUDefinition/Style],
		sku_desc as [Item/ItemMasterFields/StyleDescription],
		sku_brcd as [Item/ItemMasterFields/PackageBarcode],
		carton_type as [Item/ItemMasterFields/CartonType],
		unit_price as [Item/ItemMasterFields/Price],
		retail_price as [Item/ItemMasterFields/RetailPrice],
		std_pack_qty as [Item/ItemMasterFields/InnerPackQuantity],
		std_case_qty as [Item/ItemMasterFields/StandardCaseQuantity],
		max_case_qty as [Item/ItemMasterFields/MaximumCaseQuantity],
		std_case_len as [Item/ItemMasterFields/StandardCaseLength],
		std_case_width as [Item/ItemMasterFields/StandardCaseWidth],
		std_case_ht as [Item/ItemMasterFields/StandardCaseHeight],
		std_pack_qty as [Item/ItemMasterFields/PackMultipleQuantity],
		unit_wt as [Item/ItemMasterFields/UnitWeight],
		unit_vol as [Item/ItemMasterFields/UnitVolume],
		std_pack_wt as [Item/ItemMasterFields/InnerPackWeight],
		std_pack_vol as [Item/ItemMasterFields/InnerPackVolume],
		std_case_wt as [Item/ItemMasterFields/StandardCaseWeight],
		std_case_vol as [Item/ItemMasterFields/StandardCaseVolume],
		commodity_code as [Item/ItemMasterFields/HarmonizedTariffSchedule],
		store_dept as [Item/ItemMasterFields/StoreDepartment],
		critcl_dim_1 as [Item/ItemMasterFields/CriticalDimension1],
		critcl_dim_2 as [Item/ItemMasterFields/CriticalDimension2],
		critcl_dim_3 as [Item/ItemMasterFields/CriticalDimension3],
		stat_code as [Item/ItemMasterFields/StatusCode],
		std_pack_width as [Item/ItemMasterFields/StandardInnerPackWidth],
		std_pack_len as [Item/ItemMasterFields/StandardInnerPackLength],
		std_pack_ht as [Item/ItemMasterFields/StandardInnerPackHeight],
		unit_width as [Item/ItemMasterFields/UnitWidth],
		unit_len as [Item/ItemMasterFields/UnitLength],
		unit_ht as [Item/ItemMasterFields/UnitHeight],
		exp_licn_nbr as [Item/ItemMasterFields/ExportLicenseNbr],
		eccn_nbr as [Item/ItemMasterFields/ExportControlClassNbr],
		exp_licn_nbr as [Item/ItemMasterFields/ExportLicenseExceptSymbol],
		orgn_cert_code as [Item/ItemMasterFields/OrgnCertCode],
		nmfc_code as [Item/ItemMasterFields/NMFCCode],
		frt_class as [Item/ItemMasterFields/FreightClass],
		commodity_code as [Item/ItemMasterFields/CommodityCode],
		commodity_level_desc as [Item/ItemMasterFields/CommodityLevelDesc],
		sku_profile_id as [Item/ItemMasterFields/SkuProfileID],
		whse as [ListOfItemWarehouses/ItemWarehouse/Warehouse],
		sku_profile_id as [ListOfItemWarehouses/ItemWarehouse/ItemWarehouseFields/SkuProfileID]
	from #ItemMaster
	where RankGroup = @rank
	for xml path ('ItemMaster'), root('ItemMasterBridge'))--, ELEMENTS XSINIL)

	IF (Object_ID('tempdb..##xml') IS NOT null) DROP TABLE ##xml
	create table ##xml
	(XMLData xml)

	insert ##xml
	select @xml

	set @query = 'select * from ##xml'
	set @date = replace(replace(replace(replace(convert(varchar, getdate(), 121), ' ', ''), '-', ''), ':', ''), '.', '')
	set @file_location = '\\kermode\FileRepository\MERCHANDISING\WM\OUTBOUND\ItemMaster\'
	set @file_destination = '\\wminteg01\interfaces\itemmaster\'
	set @ItemMasterFile = 'IIMitemmasterbridge.' + @date + '.' + @rank + '.xml'
	set @XMLout = 'XML' + @rank + '.out'
	set @server = 'bedrockdb02'
	set @database = 'me_01'
	set @bcp = 'bcp "' + @query + '" queryout "' + @file_location + @XMLout + '"  -T -w -S' + @server 

	exec master..xp_cmdshell @bcp --export xml file

	set @type = 'TYPE ' + @file_location + @XMLout + ' > ' + @file_location + @ItemMasterFile 
	exec master..xp_cmdshell @type --this is needed because wm eis couldn't read the xml file due to encoding(?)
			
	set @move = 'MOVE ' + @file_location + @ItemMasterFile  + ' ' + @file_destination
	exec master..xp_cmdshell @move
	
	set @delete = 'DEL ' + @file_location + @XMLout
	exec master..xp_cmdshell @delete

	delete from #ItemMaster
	where rankgroup = @rank

	select @groups = count(distinct rankgroup) from #ItemMaster

	if @groups < 1
		break
	else
		continue


END
```

