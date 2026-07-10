# Azure.vwPOSOutbound_tax_item_group_styles_v3

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_tax_item_group_styles_v3"]
    POS_vwPOSOutbound_Products(["POS.vwPOSOutbound_Products"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| POS.vwPOSOutbound_Products |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_tax_item_group_styles_v3] AS


--with 
--usStyles as
--(
--select
--	s.style_code,
--	s.style_short_description,
--	s.style_long_description,
--	ti.tax_item_group_code,
--	ti.tax_item_group_description
--	-- @default_tax_item_group_id))+ @32commas,
--						--I think the default is 10...
--						--select o.tax_item_group_id
--						--  FROM line_object o, tax_item_group t
--						-- WHERE o.tax_item_group_id = t.tax_item_group_id
--							--o.line_object = @line_object
----into #xx
--FROM  bedrockdb01.auditworks.dbo.style_sa s
--join bedrockdb01.auditworks.dbo.class_sa c 
--	on s.upc_lookup_division=c.upc_lookup_division
--	AND  s.class_code=c.class_code
--join bedrockdb01.auditworks.dbo.tax_item u 
--	on s.upc_lookup_division=u.upc_lookup_division
--	and s.style_reference_id = u.style_reference_id
--join bedrockdb01.auditworks.dbo.sku_sa sku 
--	on u.upc_lookup_division=sku.upc_lookup_division
--	and u.sku_id=sku.sku
--join bedrockdb01.auditworks.dbo.tax_item_group ti on isnull(c.tax_item_group_id,10)=ti.tax_item_group_id
--where s.style_code not like '4%' and s.style_code not like '5%' and s.style_code not like '6%'
----and s.style_code in ('008432','030228')
--group by --if item has multiple tax_item rows, it seems to be due to having multiple upcs in the item_no field.. so we get distinct here
--	s.style_code,
--	s.style_short_description,
--	s.style_long_description,
--	ti.tax_item_group_code,
--	ti.tax_item_group_description
--	-- 68,991
--	), gc
--as
--(
--select styleCode
--from [stl-ssis-p-01].IntegrationStaging.pos.ProductCatalogMasterAttributesStage
----where stylecode in ('487109','087109','483500')
--where stylecode like '4%'
--and ItemType='Gift Card'
--group by styleCode
--)
--,
--ukStyles as
--(
--SELECT  
--	s.style_code,
--	s.style_short_description,
--	s.style_long_description,
--	--ti.tax_item_group_code,
--	 case when ti.tax_item_group_description in ('Clothing','Cookies','School Supplies') then 'Z'
--		 when s.style_short_description like '%Donation%' then 'Z'
--		  when s.style_short_description like '%BOOK%' then 'Z'
--          when ti.tax_item_group_description in ('Taxable','Digital Goods')  then
--				--case when c.class_short_description = 'UK-Gift Card' then 'Z' else 'S' end 
--				case when gc.stylecode is not null  then 'Z' else 'S' end 
--		  when ti.tax_item_group_description = 'Non-Taxable' then ' ' 
--          else RTRIM(LTRIM(ti.tax_item_group_description)) end as tax_item_group_code,
--case when s.style_short_description like '%Donation%' then 'Taxable'
--	else ti.tax_item_group_description end as tax_item_group_description
--	-- @default_tax_item_group_id))+ @32commas,
--						--I think the default is 10...
--						--select o.tax_item_group_id
--						--  FROM line_object o, tax_item_group t
--						-- WHERE o.tax_item_group_id = t.tax_item_group_id
--							--o.line_object = @line_object
----into #xx
----,gc.stylecode
--FROM  bedrockdb01.auditworks.dbo.style_sa s
--join bedrockdb01.auditworks.dbo.class_sa c on s.upc_lookup_division=c.upc_lookup_division AND  s.class_code=c.class_code
--join bedrockdb01.auditworks.dbo.tax_item u on s.upc_lookup_division=u.upc_lookup_division and s.style_reference_id = u.style_reference_id
--join bedrockdb01.auditworks.dbo.sku_sa sku on u.upc_lookup_division=sku.upc_lookup_division and u.sku_id=sku.sku
--join bedrockdb01.auditworks.dbo.tax_item_group ti on isnull(c.tax_item_group_id,10)=ti.tax_item_group_id
--left join gc on s.style_code =   gc.stylecode COLLATE SQL_Latin1_General_CP1_CI_AI
----where s.style_code in ('487109','087109','483500')
----where s.style_code like '4%' 
--where s.style_code like '4%' or s.style_code  like '5%' or s.style_code like '6%'
----and s.style_code in ('489200','489202','483500','480140')
--group by --if item has multiple tax_item rows, it seems to be due to having multiple upcs in the item_no field.. so we get distinct here
--	s.style_code,
--	s.style_short_description,
--	s.style_long_description,
--	ti.tax_item_group_code,
--	ti.tax_item_group_description,
--	gc.stylecode
--	--c.class_short_description
--	)

--	select * from usStyles
--	union
--	select * from ukStyles



	
select distinct ProductNumber as style_code, ItemDescription as style_short_description, ItemName as style_long_description,
--, tax_item_group_id, 
--tax_item_group_code, 
 --case when ti.tax_item_group_description in ('Clothing','Cookies','School Supplies') then 'Z'
 case when Department in ('School Supplies')  then 'Z'
      when Department in ('Human CLothes') then 'Z'
	  when Department in ('UK-Donations / Disc') then 'Z'
	  when Department in ('UK UK Mandated Fees') then ' '
	  when Department = 'UK-Gift Cards'then 'Z'
	  when ItemDescription like '%BOOK%' then 'Z' else 'S' end as tax_item_group_code,
 case when Department in ('School Supplies')  then 'School Supplies'
	  when Department in ('Human Clothes')  then'Clothing'
      when Department in ('UK-Donations / Disc','UK UK Mandated Fees') then 'Non-Taxable'
	 else 'Taxable' end as tax_item_group_description 
from [stl-ssis-p-01].[IntegrationStaging].[POS].[vwPOSOutbound_Products] 
where 1=1
--and stylecode = '421923'
--and stylecode in ('426048','426049', '483502','483503')
--and stylecode in ('083502','083503','183502','183503','483502','483503')
--and stylecode in ('421241','421233')
and ProductCountry in ('UK','IE')
--order by ProductNumber asc 

--select * from [stl-ssis-p-01].[IntegrationStaging].[POS].[vwPOSOutbound_Products]  where stylecode = '421923'
```

