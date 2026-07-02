# dbo.vwWMSPOStagedForDynamicsBAK20220801

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwWMSPOStagedForDynamicsBAK20220801"]
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_cost_factor(["dbo.cost_factor"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_po(["dbo.po"]) --> VIEW
    dbo_po_line(["dbo.po_line"]) --> VIEW
    dbo_po_line_cost_factor(["dbo.po_line_cost_factor"]) --> VIEW
    dbo_po_line_shipment(["dbo.po_line_shipment"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
    dbo_tpm_po_create_line_1(["dbo.tpm_po_create_line_1"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_set |
| dbo.cost_factor |
| dbo.entity_attribute_set |
| dbo.hierarchy_group |
| dbo.po |
| dbo.po_line |
| dbo.po_line_cost_factor |
| dbo.po_line_shipment |
| dbo.style |
| dbo.style_color |
| dbo.style_group |
| dbo.tpm_po_create_line_1 |

## View Code

```sql
CREATE view [dbo].[vwWMSPOStagedForDynamicsBAK20220801] as

--===================================================================================================
--	Dan Tweedie	2019-08-29	Created view, pulls from data pre-staged, will be sending to Dynamics
--===================================================================================================

with 
POLineNetFinalPrice as
	(
		select DISTINCT
			cast(po.po_no as varchar) as po_no,
			cast(pl.line_no as int) as POMainLine,
			cast (pl.net_final_cost as decimal (18,2)) as NetFinalPrice
		from po with (nolock)
		join po_line pl with (nolock) on po.po_id=pl.po_id
		join po_line_shipment pls with (nolock) on pls.po_id=po.po_id and pls.po_line_id=pl.po_line_id
		join po_line_cost_factor pcf with (nolock) on pcf.po_id=po.po_id and pl.po_line_id=pcf.po_line_id
		join cost_factor cf with (nolock) on cf.cost_factor_id=pcf.cost_factor_id
		join style_color sc with (nolock) on sc.style_color_id=pl.style_color_id
		join style s with (nolock) on s.style_id=sc.style_id
		where 1=1
		--and pcf.factor_amount > 0
	),
StyleFactoryCodes as
	(
		select 
			s.style_code,
			cast(attribute_set_code as varchar(10)) as FactoryCode
		from style s with (nolock)
		join entity_attribute_set easfact (nolock) 
			on s.style_id=easfact.parent_id
			and easfact.attribute_id = 122 
		join attribute_set ats on easfact.attribute_set_id = ats.attribute_set_id
	),
GiftCards as
	(
		select
			cast(s.style_code as varchar(6)) as Style
		from style s with (nolock)
		join style_group sg with (nolock) on s.style_id = sg.style_id
		join hierarchy_group hg with (nolock) on sg.hierarchy_group_id=hg.hierarchy_group_id
		where s.active_flag = 1
		--and substring(hg.hierarchy_group_code, 1,8) in ('R-B-D-80','R-B-U-80')
		and substring(hg.hierarchy_group_code, 1,8) in ('R-B-D-80')
	)
select distinct
	case 
		when po.ShipToID in (980,960,13) 
			then '1100'
		when po.ShipToID in (2970)
			then '2110'
		when po.ShipToID in (3970)
			then '3001'
		when po.ShipToID in (3980)
			then '1200'
	end as Company,
	case 
		po.ShipToID 
			when 980 then '9980'
			when 960 then '9960'
			when 13 then '1013'
			when 2970 then '9970'
			when 3970 then '9940'
			when 3980 then '9941'
	end as Warehouse,
	po.po_no as PONumber,
	po.OrderLine as POLineNumber,
	cast(po.ItemId as varchar(10)) as ItemNumber,
	po.CurrQty as Quantity,
	po.EndDeliverDateTime as DeliveryDate,
	po.StartShipDate as StartShipDate, 
	cast(po.CancelDate as date) CancelDate,
	cast(po.ShipFromID as varchar(10)) as VendorCode,
	po.UnitCost,
	sfc.FactoryCode, 
	nfp.NetFinalPrice,
	po.line_no as POMainLine
from tpm_po_create_line_1 po
join StyleFactoryCodes sfc on po.ItemID=sfc.Style_Code
join POLineNetFinalPrice nfp 
	on po.po_no=nfp.po_no
	and po.line_no=nfp.POMainLine
where 1=1
--and po.ShipToID in (980,960,13,2970,3970,3980)
and po.ShipToID in (980,13)
and po.TransactionType not in ( 'Deleted Line', 'Cancelled')
and po.ItemID not in (select Style from GiftCards) --excludes giftcards from going to Dynamics
UNION
select distinct
	case 
		when po.ShipToID in (980,960,13) 
			then '1100'
		when po.ShipToID in (2970)
			then '2110'
		when po.ShipToID in (3970)
			then '3001'
		when po.ShipToID in (3980)
			then '1200'
	end as Company,
	case 
		po.ShipToID 
			when 980 then '9980'
			when 960 then '9960'
			when 13 then '1013'
			when 2970 then '9970'
			when 3970 then '9940'
			when 3980 then '9941'
	end as Warehouse,
	po.po_no as PONumber,
	po.OrderLine as POLineNumber,
	NULL as ItemNumber,
	0 as Quantity,
	NULL as DeliveryDate,
	NULL as StartShipDate,
	NULL as CancelDate,
	cast(po.ShipFromID as varchar(10)) as VendorCode,
	0 as UnitCost,
	NULL as FactoryCode,
	isnull(nfp.NetFinalPrice,0) as NetFinalPrice,
	po.line_no as POMainLine
from tpm_po_create_line_1 po
left join POLineNetFinalPrice nfp 
	on po.po_no=nfp.po_no
	and po.line_no=nfp.POMainLine
where 1=1
--and po.ShipToID in (980,960,13,2970,3970,3980)
and po.ShipToID in (980,13)
and po.TransactionType in ( 'Deleted Line', 'Cancelled')
and po.ItemID not in (select Style from GiftCards) --excludes giftcards from going to Dynamics
```

